# 统一配置参考

配置 schema 版本当前为 `1.0`。文件通常包含 `schema_version`、`runtime` 和一个执行块。

## 推理

```yaml
schema_version: "1.0"
runtime:
  seed: 42
  device: auto
inference:
  backbone: medical_reference
  batch_size: 2
  config: {}
  requests:
    - request_id: case-001
      task: understanding
      medical_task: diagnostic_reasoning
      prompt: Describe the relevant findings.
      images: [data/case-001.png]
  output_json: outputs/inference/results.json
```

## 评测

```yaml
schema_version: "1.0"
evaluation:
  benchmark: medical_vqa
  mode: full
  data:
    adapter: vqa_rad
    path: data/vqa_rad/test.jsonl
    image_root: data/vqa_rad/images
    source_revision: IMMUTABLE_REVISION
  model:
    backbone: llava_med_v1_5_7b
    config:
      model_path: /absolute/pinned/model
  output_directory: outputs/evaluation/vqa_rad
```

## 后训练

后训练配置使用 `post_training` 块。研究路线模板应通过 CLI 生成，再补全固定源码、数据 manifest、provenance、license、去标识化状态、原生 entrypoint 和 checkpoint。

## 推理后端

后端配置包含 `name`、`mode`、`parallel`、`scheduler`、endpoint 和 timeout。`world_size = TP × PP × DP`。

不要把密码或 token 写进 YAML；只保存环境变量名。

