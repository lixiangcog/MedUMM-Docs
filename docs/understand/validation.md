# 如何理解“已支持”

MedUMM 使用分级证据，防止把接口、安装和真实实验混为一谈。

| 等级 | 含义 | 可以声称 | 不能声称 |
|---|---|---|---|
| cataloged | 来源、许可、访问和能力元数据存在 | 已纳入资源规划 | 已经可运行 |
| interface validated | 有独立注册、规范化接口、模板和测试 | 平台接口已接入 | 权重已加载或结果可信 |
| runtime preflight | 固定依赖、源码、资产和 CUDA 检查通过 | 环境具备运行条件 | 模型完成任务 |
| backend runtime | 固定真实模型在真实 GPU 完成请求 | 工程链路跑通 | 医学质量或临床安全 |
| task runtime | 模型 + 数据 + 协议完成垂直切片 | 该切片可复现 | 全数据集或跨中心泛化 |
| clinical evidence | 需要更严格外部研究与合规流程 | 只能按实际研究结论表述 | 自动由工具包赋予 |

## v1.2.0 的例子

<span class="validation-badge">backend runtime passed</span> vLLM 与 SGLang 已在同一 Qwen2.5-VL-3B 模型上完成双 A800、TP=2 的顺序与八路并发验收。

<span class="validation-badge">preflight only</span> Emu3.5 的固定源码与 20 个 vLLM 补丁检查通过，但完整权重和 FlashAttention 依赖未就绪，因此没有真实生成或 token/s 声明。

## 阅读结果时问五个问题

1. 使用的是哪个不可变模型和数据 revision？
2. 样本数是 smoke slice 还是完整测试集？
3. 指标协议、分组和阈值是否记录？
4. 是接口测试、GPU 工程验收，还是医学质量实验？
5. 失败尝试和未完成边界是否被保留？

