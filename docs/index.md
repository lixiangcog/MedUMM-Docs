# MedUMM 文档

<div class="medumm-hero">
<strong>MedUMM</strong> 是面向医学统一多模态模型的开放研究平台，覆盖推理、医学评测、报告、资源治理和后训练。本文档对应代码版本 <strong>v1.4.0</strong>。
</div>

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} 我想先理解 MedUMM
:link: understand/what-is-medumm
:link-type: doc

从“为什么需要它”开始，理解四层架构、三条主流程、医学任务与自然图像任务的区别，以及“支持”到底代表什么。
:::

:::{grid-item-card} 我要参与项目开发
:link: project/requirements
:link-type: doc

查看项目需求、范围、里程碑、验收标准、稳定接口，以及添加模型、数据集、评测和后训练方法的规范。
:::

:::{grid-item-card} 我要直接跑起来
:link: getting-started/quickstart
:link-type: doc

安装 MedUMM，运行无权重快速示例，再进入真实模型、评测、服务或后训练流程。
:::

:::{grid-item-card} 我要查命令与配置
:link: reference/cli
:link-type: doc

快速查阅 CLI、统一 YAML、Python API、输出文件和术语。
:::
::::

## 当前版本一览

| 能力 | v1.4.0 状态 | 说明 |
|---|---|---|
| 统一推理 | 已实现 | understanding / generation / editing |
| 医学评测 | 已实现 | audit → generate → score → report |
| 医学资源目录 | 66 项 | 32 个模型、34 个数据集，验证等级不同 |
| 后训练 | 已接入 | SFT、DPO/SimPO/ORPO 与 7 条研究路线 |
| 推理引擎 | 已实机验证 | vLLM、SGLang 双 A800、TP=2 |
| Emu3.5 CFG | 接口与补丁预检通过 | 完整权重生成仍受资产下载阻塞 |
| 环境隔离 | 32/32 契约与解析通过 | 每模型独立锁、Docker、Apptainer 与 Modal 镜像 |
| 真实模型适配 | 32/32 显式配方，7/32 GPU 证据 | 新增 PLIP、QuiltNet、MedVLM-R1、BiomedCLIP A800 验收 |

:::{warning}
MedUMM 是研究软件，不是医疗器械。工程验收、基准分数和模型输出均不能替代临床验证、医生判断或合规审批。
:::

```{toctree}
:maxdepth: 2
:caption: 快速开始

getting-started/quickstart
getting-started/first-workflow
```

```{toctree}
:maxdepth: 2
:caption: 理解 MedUMM

understand/what-is-medumm
understand/architecture
understand/workflows
understand/medical-tasks
understand/validation
```

```{toctree}
:maxdepth: 2
:caption: 项目文档

project/requirements
project/status
project/resources
project/roadmap
```

```{toctree}
:maxdepth: 2
:caption: 开发指南

development/contributing
development/add-model
development/add-dataset-benchmark
development/post-training
development/inference-optimization
development/model-environments
development/model-adapters
development/release-evidence
```

```{toctree}
:maxdepth: 2
:caption: 参考手册

reference/cli
reference/configuration
reference/python-api
reference/outputs
reference/glossary
```
