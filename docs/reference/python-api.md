# Python API

公共入口位于 `medumm.api`：

```python
from medumm import catalog, evaluate, infer, post_train, resources
```

## 推理

```python
from medumm import infer

results = infer({
    "schema_version": "1.0",
    "inference": {
        "backbone": "medical_reference",
        "requests": [{
            "request_id": "case-001",
            "task": "understanding",
            "prompt": "Describe the findings.",
        }],
    },
})
print(results[0].to_dict())
```

## 评测与后训练

`evaluate(config)` 返回 `EvaluationResult`；`post_train(config)` 返回 `TrainingResult`。二者接受与 CLI 相同的内存配置，并可以显式传入 `RuntimeContext`。

## 目录

`catalog()` 返回已注册执行组件。`resources(kind)` 返回审计过的模型/数据规格，不导入重量级模型库。

## 稳定对象

- `InferenceRequest`
- `InferenceResult`, `EvaluationResult`, `TrainingResult`, `Artifact`
- `ModelCapabilities`
- `ModelAdapter`, `DatasetAdapter`, `BenchmarkAdapter`, `MetricSuite`, `PostTrainer`

这些对象的公共字段属于 schema 1.0 兼容面。模型特有 `config` 与 `parameters` 由插件拥有。

