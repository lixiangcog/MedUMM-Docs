# 三条主流程

## 推理

```{mermaid}
sequenceDiagram
  participant User as YAML / API
  participant Pipe as InferencePipeline
  participant Task as TaskPipeline
  participant Model as ModelAdapter
  User->>Pipe: requests + backbone
  Pipe->>Task: 按任务分组与批处理
  Task->>Task: 校验任务/模态/数量
  Task->>Model: understand/generate/edit_batch
  Model-->>Pipe: InferenceResult
  Pipe-->>User: 恢复原始顺序
```

同一批请求可以包含不同任务；执行器会分组执行，但最终保持输入顺序。每个结果具有统一 schema，包含文本、文件、分数、元数据和耗时。

## 评测

```{mermaid}
stateDiagram-v2
  [*] --> Audit
  Audit --> Generate: 数据通过治理与结构检查
  Generate --> Score: 预测与指纹已保存
  Score --> Report: 指标与协议已解析
  Report --> [*]
```

`audit`、`generate`、`score`、`full` 是显式模式。生成与评分分离，使昂贵推理可以复用，又能由指纹阻止错误缓存。

## 后训练

后训练有两类入口：

1. 通用医学对齐：SFT、DPO、SimPO、ORPO、clinical DPO，支持 LoRA/QLoRA。
2. 研究路线：BAGEL SFT、RecA、Uni-CoT、IRG、UniGame、UniPath、LatentUMM。

研究路线保留自己的阶段图和原生运行时。`--plan` 只验证并生成计划；只有固定源码、审计数据、许可和输出均满足条件时才允许 launch。

