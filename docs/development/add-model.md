# 添加模型

## 1. 声明能力

模型必须继承 `ModelAdapter`，并在加载权重前声明 `ModelCapabilities`：任务、输入/输出模态、架构、批处理、最大图像数、后端、CFG 和并行方式。

```python
class MyMedicalModel(ModelAdapter):
    name = "my_medical_model"
    capabilities = ModelCapabilities(
        tasks=frozenset({TaskType.UNDERSTANDING}),
        input_modalities=frozenset({Modality.TEXT, Modality.IMAGE}),
        output_modalities=frozenset({Modality.TEXT}),
        architecture=ArchitectureFamily.AUTOREGRESSIVE,
        supports_batching=True,
        supported_backends=frozenset({"native"}),
    )
```

## 2. 实现生命周期

实现 `load(config, runtime)` 和对应的批量方法。只实现真实支持的任务；未支持方法使用基类的明确错误。`runtime_info()` 返回非秘密、机器可读的模型和环境标识。

## 3. 注册

在 builtins 中添加惰性 factory，或由外部包调用注册表。目录查询不得导入模型框架或分配 GPU。

## 4. 固定与治理

- 远程权重必须提供不可变 revision。
- `trust_remote_code` 必须显式记录。
- 许可证和访问条件必须进入资源规格。
- 官方 runtime 与共享 Transformers executor 不兼容时，使用隔离 bridge。

## 5. 验收

至少测试能力校验、输入模态、批处理、失败组合、结果 schema 和关闭资源。若宣称 runtime validated，还要提交真实 GPU 作业、环境、非空输出和固定 revision 证据。

