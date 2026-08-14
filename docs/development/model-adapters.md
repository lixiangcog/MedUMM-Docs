# 真实模型适配与验收

## “进入目录”不等于“已经支持”

MedUMM 将模型支持拆成三个独立结论：

1. **cataloged**：有来源、许可、访问级别、固定 revision、任务和环境规格；
2. **adapter-defined**：有明确模型类、处理器、提示协议和执行器；
3. **runtime-validated**：固定真实权重在分配的 GPU 上通过公共接口，并保存证据。

v1.4 的 32 款模型全部达到前两项，7 款达到第三项。其余 25 款仍是后续工程队列，不能把注册名、可下载权重或导入成功写成“跑通”。

## 查看与预检

```bash
medumm models list
medumm models show medvlm_r1
medumm models audit

medumm models preflight medvlm_r1 \
  --model-path /models/medvlm-r1 \
  --revision d256f2cfdf98c6872c1dc9f20b7dd52f49374fe9
```

预检会检查：模型 revision 是否精确匹配、快照是否存在、受限条款是否已接受、官方源码 checkout 与 commit 是否匹配，以及隔离环境中的必要导入。任一项失败都会返回非就绪状态。

## v1.4 新增真实运行

最终 Slurm 作业 `437526` 在单张 NVIDIA A800-SXM4-80GB 上完成，退出码 0。四款模型均使用独立 Python 3.10 环境、Torch 2.7.1+cu126 和 MedUMM 1.4.0。

| 模型 | 执行器 | 推理时间 | 峰值显存 |
|---|---|---:|---:|
| PLIP | Transformers contrastive | 280.73 ms | 588.12 MiB |
| QuiltNet | Transformers contrastive | 279.15 ms | 588.10 MiB |
| MedVLM-R1 | Qwen2-VL chat | 1702.38 ms | 4337.41 MiB |
| BiomedCLIP | OpenCLIP HF Hub | 230.59 ms | 777.61 MiB |

输入使用已准备的真实 PathVQA 图像。这里的文字和候选分数只证明接口、权重、处理器与 GPU 数据流正确，不代表临床质量或完整基准性能。

## 实跑发现的三个问题

- QuiltNet 固定版本实际公开原生 Transformers `CLIPModel`，因此环境从 OpenCLIP 路线纠正为 Transformers 对比路线。
- BiomedCLIP 的 OpenCLIP 配置内部依赖 Hugging Face 文本编码器，环境锁新增 `transformers`、`tokenizers`，并单独固定 BiomedBERT 配置与 tokenizer。
- MedVLM-R1 的生成配置将 `use_cache` 留为 `null`，官方 demo 却显式传入 `use_cache=True`。首次作业 `437506` 因 attention mask 长度不一致失败；按官方路径修正后，最终作业通过。

## 复现边界

当前集群计算节点没有外部 DNS。因此固定权重和依赖应在有网络的登录/构建节点准备，A800 作业只读取本地资产并设置 Hugging Face 离线模式。最终验证器要求每条结果具备正确模型名、固定 revision、显式 executor、CUDA 设备、相同 Slurm job ID、非空输出和实测延迟。

机器可读证据位于 MedUMM 代码仓库的 `docs/results/v1.4-real-model-adapters.json`。下一批优先验证 CheXagent、Fleming/InternVL、MedGemma、M3D-LaMed 和一款 LLaVA-Qwen 模型，再进入 Flamingo、RadFM、VILA、XrayGPT 及多 GPU 大模型。
