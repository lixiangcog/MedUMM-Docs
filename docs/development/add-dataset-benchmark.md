# 添加数据集与评测

## 数据集 adapter

`DatasetAdapter` 将外部记录规范化为稳定样本，并实现由内容与选择参数共同决定的 fingerprint。原始数据通常留在仓库外。

最低治理字段：

- 官方来源与不可变 revision；
- 许可与访问条件；
- 去标识化状态；
- split 与选择规则；
- 图像/视频/体数据的本地解析边界；
- 样本 ID 与参考答案来源。

## Benchmark adapter

`BenchmarkAdapter` 负责：

1. 把规范化样本转成 `EvaluationItem`；
2. 构造模型请求；
3. 解析模型输出；
4. 调用版本化 `MetricSuite`；
5. 汇总并返回 `EvaluationResult`。

除非任务无法拆分，基准应支持 `audit`、`generate`、`score`、`full`。

从 v1.6 起，只有数据资源注册不算完成 benchmark。新增独立 benchmark 还必须固定：

- 兼容的 dataset adapter family；
- 必需 annotation/choices/candidate scores；
- 医学 prompt template；
- 不允许被配置静默替换的版本化 metric suite；
- 来源、去标识化、媒体、组别或配对完整性审计；
- 可单独运行的 YAML、测试和报告证据。

先用以下命令检查现有 contract：

```bash
medumm benchmarks list
medumm benchmarks show medical_temporal_reasoning
medumm benchmarks template medical_temporal_reasoning
medumm benchmarks audit
```

## 医学指标原则

- 报告要检查事实、否定、矛盾、关键发现与结构完整性。
- 定位要明确像素坐标或归一化坐标。
- 测量要识别单位并使用来源定义的容差。
- 校准需要保留全部候选概率，只有最终标签不够。
- 分组差异需要最小样本门槛，不能自动解释为因果公平性。

## 验收

先以小而平衡的真实切片验证 wiring 和协议覆盖，再运行完整数据。小切片结果必须明确不是质量估计。
