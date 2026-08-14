# 逐模型环境隔离

MedUMM 的 32 个模型横跨 Gemma、Qwen、InternVL、LLaVA、OpenFlamingo、3D 医学栈和对比学习编码器，不能安全地塞进同一个 Python 环境。v1.3 为每个模型建立了独立、可审计的环境契约。

## 一个模型对应什么

每个模型都有以下信息：

- Python、CUDA 与精确包版本；
- 固定摘要的基础镜像；
- 完整传递依赖锁；
- 固定模型 revision 与官方源码 commit；
- 权重访问级别、GPU 建议和导入探针；
- 独立 Dockerfile、Apptainer 定义及 Modal 镜像。

兼容模型可以共享“配方族”，但不会共享可变虚拟环境；任一模型升级都只改变自己的锁和环境指纹。

## 常用操作

```bash
# 查看全部模型环境
medumm environments list

# 查看一个模型的所有版本与硬件约束
medumm environments show lingshu_7b

# 建立独立虚拟环境
bash scripts/setup_model_env.sh lingshu_7b

# 在 Slurm 上提交
sbatch --export=ALL,MODEL_NAME=lingshu_7b \
  scripts/slurm_model_environment.sh
```

受限模型默认拒绝安装。只有在上游网站接受条款后，才能显式添加 `--accept-terms`，访问凭证仍通过环境变量或平台 secret 注入，不能写进 Git 或镜像。

## 五级验证

| 等级 | 代表什么 |
|---|---|
| contract validated | 字段齐全、版本不可变、生成文件一致 |
| lock resolved | 目标 Linux/Python 上的完整依赖图可解析 |
| container built | 容器从头构建成功 |
| import validated | 隔离环境中的核心模块可以导入 |
| runtime validated | 固定权重完成真实任务并保存证据 |

目前 32 个模型均通过前两级。LLaVA-Med、Lingshu-7B、PubMedCLIP、PLIP、QuiltNet、MedVLM-R1、BiomedCLIP、MedMO-4B、MedMO-8B、Lingshu-I-8B 和 Fleming-VL-8B 共 11 款具有固定权重 GPU 证据；其余 21 个不能因为“已经有 Dockerfile”就宣称跑通。

## 服务器边界

验收服务器已确认 Singularity 能拉取并运行 OCI 镜像，但当前账号没有 `fakeroot` 的 subordinate-ID 映射，也没有可用的远程构建器。因此从 definition 构建 SIF 仍需管理员开放 `fakeroot`、remote builder 或批准的 `sudo` 之一。这个限制不会影响已构建镜像的拉取和运行。

## 修改环境

环境源文件变更后依次执行：

```bash
python scripts/resolve_model_environments.py
python scripts/generate_model_environments.py
python scripts/generate_model_environments.py --check
pytest tests/test_model_environments.py
```

专用 CI 会检查 32/32 覆盖、所有依赖图、160 个生成制品、不可变 pin、访问闸门及脚本语法。
