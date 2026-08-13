# 术语表

Adapter
: 将模型或数据源接入稳定平台接口的薄层。

Audit
: 在昂贵执行前检查数据结构、来源、许可、访问和去标识化。

CFG
: Classifier-Free Guidance。Emu3.5 使用条件/无条件 token 流和定制调度器。

Continuous batching
: 解码过程中持续接纳新请求，由推理引擎动态组成批次。

Fingerprint
: 由数据、模型或评测协议内容生成的稳定身份，用于拒绝错误缓存。

Official bridge
: 调用隔离的官方模型运行时，而不把第三方内部实现复制进 MedUMM。

PP / TP / DP
: Pipeline / Tensor / Data Parallelism。总 world size 通常是三者乘积。

Runtime validated
: 固定真实资产已经在声明硬件上完成验收；不等于临床有效。

Smoke test
: 小规模、低成本检查接口和编排，不能代表论文复现或模型质量。

Vertical slice
: 一个模型、一个数据集、一个医学协议、一个可复现配方和一份证据组成的端到端闭环。

