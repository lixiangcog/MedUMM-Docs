# 当前项目状态

本文档对应 MedUMM `v1.4.0`。

## 已建立的平台能力

- 四类稳定插件接口与惰性注册表。
- 统一请求、推理结果、评测结果和训练结果 schema 1.0。
- 理解、生成、编辑与跨任务评测。
- 医学数据审计、指纹、分布式分片、预测合并和报告。
- 32 个模型、34 个数据集资源规格。
- 5 类临床相关评测套件。
- 通用 SFT/偏好优化与 7 条研究后训练路线。
- vLLM/SGLang 服务、连续批处理、多 GPU 启动和性能基准。
- 32 个模型的逐模型环境契约、完整依赖锁、Docker/Apptainer 和 Modal 映射。
- 32 个模型的显式 adapter 配方、模型类、处理器、提示协议和上游入口。

## 重要真实运行证据

| 版本 | 垂直切片 | 证据边界 |
|---|---|---|
| v0.8 | LLaVA-Med + VQA-RAD，A800 | 目录别名、数据来源、真实推理与小样本评测 |
| v0.9 | Lingshu + SLAKE；PubMedCLIP + PneumoniaMNIST | 架构多样性与两类执行器 |
| v1.0 | Lingshu + balanced PathVQA，A800 | 病理 VQA answer-type 协议 |
| v1.1 | 7 条后训练路线，13 阶段 | CLI/阶段/制品 contract，不是论文级训练 |
| v1.2 | vLLM/SGLang + Qwen2.5-VL-3B，2×A800 | TP=2、连续批处理、性能报告 |
| v1.3 | 32 个模型环境，Linux/Python 3.10 | 32/32 依赖图解析；160 个生成制品无漂移 |
| v1.4 | PLIP、QuiltNet、MedVLM-R1、BiomedCLIP，A800 | 4 款固定权重通过公共接口；总计 7/32 GPU 验证 |

## v1.2 性能验收

| 后端 | 顺序吞吐 | 八路并发吞吐 | 比率 |
|---|---:|---:|---:|
| vLLM 0.11.0 | 7.487907 req/s | 39.173504 req/s | 5.231569× |
| SGLang 0.5.4.post3 | 7.144201 req/s | 41.789132 req/s | 5.849378× |

硬件为 2×NVIDIA A800-SXM4-80GB，模型为固定 revision 的 Qwen2.5-VL-3B-Instruct。每个 profile 计量 24 个请求、576 个输出 token。这是工程负载结果，不是医疗模型效果分数。

## 当前主要缺口

- Emu3.5 完整权重生成与 FlashAttention 2.8.3 验收。
- 多节点后端和长时间稳定性压测。
- 专家标注报告生成、定位和测量真实切片。
- 临床安全偏好数据上的真实后训练。
- 更多目录资源从 interface validated 升级为 runtime validated。
- 为其余 25 个模型逐一完成容器构建、导入和真实权重任务验证。
