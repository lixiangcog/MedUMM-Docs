# 快速开始

## 1. 获取代码

```bash
git clone https://github.com/lixiangcog/MedUMM.git
cd MedUMM
python3 -m venv .venv
.venv/bin/python -m pip install -e ".[baseline,test]"
```

建议使用 Python 3.12。基础平台支持 Python 3.10+，但 Emu3.5 的固定 vLLM 路径要求 Python 3.12。

## 2. 查看平台组件

```bash
.venv/bin/medumm --version
.venv/bin/medumm catalog
.venv/bin/medumm backends --json
.venv/bin/medumm resources validate
```

这些命令不会下载大型权重。`catalog` 展示已注册执行组件；`resources` 展示医学资源规格及其验证等级。

## 3. 跑无权重推理

```bash
.venv/bin/medumm infer \
  --config configs/inference/medical_reference_workflow.yaml
```

这条路线用于检查配置、任务分发、结果序列化与输出目录，不能代表真实模型质量。

## 4. 跑评测状态机

```bash
.venv/bin/medumm evaluate \
  --config configs/evaluation/medical_vqa_linear_smoke.yaml
```

真实评测建议先运行 `mode: audit`，确认数据来源、许可、去标识化、字段完整性和指纹，再进入 `generate` 与 `score`。

## 5. 选择下一条路线

- 真实医学 VLM：从 Lingshu、LLaVA-Med 或资源目录中的已验证条目开始。
- 高吞吐服务：阅读 [推理优化](../development/inference-optimization.md)。
- 医学评测：阅读 [数据集与基准接入](../development/add-dataset-benchmark.md)。
- 后训练：先使用 `medumm post-train --list-methods` 和 `--plan`。

:::{tip}
第一次使用时先跑 reference/smoke 配置，再安装重量级依赖。MedUMM 的不同官方模型桥可能需要互相隔离的环境。
:::

