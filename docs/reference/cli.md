# CLI 参考

| 命令 | 用途 | 常用参数 |
|---|---|---|
| `medumm infer` | 理解、生成或编辑 | `--config`, `--set`, `--output-json` |
| `medumm evaluate` / `eval` | 运行医学基准 | `--config`, `--set` |
| `medumm post-train` / `train` | 后训练或计划 | `--config`, `--plan`, `--list-methods`, `--template` |
| `medumm catalog` | 查看执行组件 | `--json` |
| `medumm resources` | 查看/验证医学资源 | `list`, `show`, `template`, `validate` |
| `medumm backends` | 查看推理后端 | `--json` |
| `medumm serve` | 计划或启动 vLLM/SGLang | `--config`, `--plan`, `--set` |
| `medumm benchmark-inference` | 推理性能基准 | `--config`, `--set` |
| `medumm merge-predictions` | 严格合并分布式预测 | `--shards`, `--output`, `--expected-count` |
| `medumm report` | 生成排行榜 | `--scores`, `--output-directory` |

## 配置覆盖

```bash
medumm infer --config run.yaml \
  --set inference.batch_size=4 \
  --set runtime.device=cuda
```

覆盖项使用点路径。复杂或需要审计的改动应保存为新 YAML，而不是只留在 shell 历史中。

## 退出行为

配置错误、治理门禁、子进程失败、缺少检查点或预测合并不一致应返回非零退出码，以便 Slurm 和 CI 正确判定失败。

