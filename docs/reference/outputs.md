# 输出与运行制品

## 推理结果

`InferenceResult` 包含 schema version、request ID、任务、模型名、文本、文件制品、候选分数、元数据和耗时。

## 评测目录

典型输出包括：

- `dataset_audit.json`：来源、治理和结构审计；
- `predictions.jsonl`：带模型/数据指纹的预测；
- `results.jsonl`：逐样本评分；
- `score.json`：协议与聚合指标；
- CSV/leaderboard：便于浏览的汇总；
- run manifest：解析后的组件、环境和结果。

## 后训练目录

包含 preflight、redacted command、stage log、checkpoint、result 和依赖关系。敏感配置值不得写入日志。

## 性能报告

`benchmark.json` 包含 warm-up/计量设置、请求与 Token 吞吐、延迟分位数、每次迭代、后端配置和环境快照。

输出文件用于审计与复现；不要依赖未记录的终端文本作为唯一证据。

