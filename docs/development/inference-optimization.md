# 推理优化

## 后端边界

| 路径 | 连续批处理 | 并行 | Emu3.5 原生 CFG |
|---|---:|---|---:|
| native adapter | 模型决定 | 模型决定 | 否 |
| vLLM OpenAI server | 是 | TP/PP/DP | 否 |
| SGLang OpenAI server | 是 | TP/PP/DP | 否 |
| Emu3.5 patched vLLM | 是 | TP | 是 |

标准 OpenAI 请求无法表达 Emu3.5 的 `uncond_prompt_token_ids`。因此 MedUMM 对 HTTP/SGLang 路线的 Emu3.5 CFG 失败关闭，而不是静默运行另一种算法。

## 服务计划

```bash
medumm serve --config configs/inference/serve_vllm.yaml --plan
medumm serve --config configs/inference/serve_sglang.yaml --plan
```

计划会解析精确启动命令、固定 revision、world size、可见 GPU、调度限额和后端安装状态。将 `server.execution` 改为 `launch` 才会真正启动服务。

## 性能测试

```bash
medumm benchmark-inference \
  --config configs/inference/benchmark_openai_vllm_v1.2.yaml
```

报告包括请求/Token 吞吐、mean/p50/p95/p99 延迟、迭代壁钟时间，以及后端可提供时的 TTFT、排队和引擎延迟。

## Emu3.5 特殊要求

必须使用 Python 3.12、vLLM 0.11.0、Transformers 4.56.1、FlashAttention 2.8.3、固定官方源码和完整 20 补丁。通用 vLLM server 应与打补丁的 Emu3.5 环境隔离。

v1.2.0 只完成补丁运行时预检，未完成权重级生成，请勿引用不存在的 Emu3.5 性能数据。

