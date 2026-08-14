# 数据集不等于 Benchmark

这是理解 MedUMM v1.6 最重要的边界之一。

- **Dataset resource** 回答“数据从哪里来、怎么访问、什么许可、怎样规范化”。
- **Benchmark** 回答“用哪些样本、怎样问模型、需要哪些标注、怎么评分、如何审计和报告”。
- **Metric suite** 是 benchmark 固定使用的逐样本评分和聚合实现。
- **Cross-task runner** 组合已有 benchmark，本身不创造新的医学评分协议。

所以 34 个数据资源不能写成 34 个完整评测。当前真实结构是：

| 对象 | 数量 | 含义 |
|---|---:|---|
| 数据资源 | 34 | 可发现、带治理元数据的数据来源 |
| 专用医学 benchmark | 13 | 固定数据/标注/提示/指标的独立执行协议 |
| 通用 benchmark | 2 | `medical_vqa`、`medical_tasks` |
| 独立 benchmark 合计 | 15 | 可以分别 audit、推理、评分、报告 |
| 组合 runner | 1 | `cross_task` |

## 13 个专用协议

| Benchmark | 评测重点 | 主要评分 |
|---|---|---|
| `pathology_vqa` | 病理图像问答 | yes/no、free-form、overall accuracy |
| `medical_mcqa` | 医学多选推理 | strict choice accuracy、无效回答率 |
| `medical_image_classification` | 类别不平衡的单标签识别 | balanced accuracy、macro F1/AUC、confusion matrix |
| `medical_multilabel_findings` | 多个并存医学发现 | micro/macro F1、exact match |
| `radiology_report_generation` | 报告事实与结构 | factuality、contradiction、critical recall、sections |
| `medical_grounding` | 框/点定位 | IoU、IoU@0.5、point distance/accuracy |
| `medical_measurement` | 带单位测量 | MAE/MRE、tolerance、unit errors |
| `medical_temporal_reasoning` | 手术/纵向序列 | exact sequence、edit similarity、phase/transition |
| `medical_retrieval` | 医学图文检索 | Recall@1/5/10、MRR |
| `medical_calibration` | 置信度与选择性预测 | ECE、Brier、NLL、coverage/accuracy |
| `medical_fairness` | 分组表现差异 | worst-group、max-min、DP/EO gaps |
| `medical_safety` | 拒答与不安全服从 | safe completion、over-refusal、unsafe compliance |
| `medical_robustness` | 配对扰动稳定性 | accuracy drop、prediction consistency |

每个协议都把所需标注写入 contract。例如 `medical_grounding` 要求 `annotations.grounding`，`medical_retrieval` 要求候选、正例和模型产生的候选分数，`medical_robustness` 要求 baseline 与至少一个 perturbation 组成完整 pair。缺失时数据审计直接失败，不会用不相关指标凑一个分数。

## 一次评测怎样流动

```{mermaid}
flowchart LR
    A["固定 revision 的源数据"] --> B["规范化 Dataset Adapter"]
    B --> C["Benchmark 数据与治理审计"]
    C --> D["医学 Prompt / Candidate 构造"]
    D --> E["统一模型推理接口"]
    E --> F["专用 Metric Suite"]
    F --> G["逐样本结果"]
    F --> H["聚合 JSON / CSV 报告"]
```

Metric suite 名称和版本进入运行 fingerprint。某个 benchmark 不能在 YAML 中被静默换成更容易得到高分的通用指标。

## 怎么看验证等级

仓库里的 v1.6 合成矩阵会对 13 项分别执行审计、推理、专用评分和报告，证明软件路径能走通。它没有患者数据，也不代表医学效果。

该矩阵已在 `node15` 以 Slurm 作业 `437789` 完成：13 个协议、21 个合成样本全部产生对齐的预测和结果，作业退出码为 `0:0`。运行使用 `medical_reference`，因此这是 CPU 软件 contract 证据，不是 GPU 真实模型证据。

要升级为真实 runtime evidence，还必须同时具备：

1. 固定 revision 和许可/访问记录的真实数据；
2. 固定权重与独立环境的真实模型；
3. 源数据支持的标注，不凭空生成临床标签；
4. Slurm/CUDA、预测、分数和报告证据；
5. 对样本规模和统计意义的诚实说明。

即使是真实模型加真实小切片，也通常只证明 wiring；完整数据和临床评审才可能支持更强的质量结论。

## 查询与运行

```bash
medumm benchmarks list
medumm benchmarks show medical_grounding
medumm benchmarks audit
medumm evaluate --config configs/evaluation/benchmarks_v1.6/medical_grounding.yaml
```

一次完整运行会生成 `dataset_audit.json`、`predictions.jsonl`、`results.jsonl`、`score.json` 和 `metrics.csv`。
