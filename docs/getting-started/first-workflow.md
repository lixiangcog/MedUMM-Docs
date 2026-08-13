# 第一条完整工作流

一条可审计的医学多模态实验，不只是“模型能返回答案”。推荐顺序如下：

```{mermaid}
flowchart LR
  A[固定模型/数据版本] --> B[数据审计]
  B --> C[生成预测]
  C --> D[独立评分]
  D --> E[报告与证据]
  E --> F[再决定是否扩规模]
```

## 固定版本

远程模型和数据必须使用不可变 revision；本地模型应来自可追溯快照。不要把 `main`、`latest` 或未经记录的缓存当成实验版本。

## 数据审计

```yaml
evaluation:
  benchmark: medical_vqa
  mode: audit
  data:
    adapter: vqa_rad
    path: data/vqa_rad/test.jsonl
    image_root: data/vqa_rad/images
    source_revision: REPLACE_WITH_IMMUTABLE_REVISION
```

审计通过不代表可以公开数据；它只证明当前配置满足平台声明的来源、许可、去标识化和结构要求。

## 生成与评分分离

`generate` 产生带指纹的预测，`score` 只对匹配的预测和参考答案评分。这样可以复用昂贵推理，同时避免错误地给旧预测套用新数据或新协议。

## 保存证据

保留配置、环境、模型与数据 revision、运行清单、预测、逐样本结果、聚合指标和失败记录。发布时说明验证等级和样本规模。

