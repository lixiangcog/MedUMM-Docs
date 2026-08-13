# 后训练开发

## 通用医学对齐

平台把三个合同分开：

- 数据合同：监督或偏好样本、来源、许可、去标识化与混合权重。
- 目标合同：completion-only SFT、DPO、SimPO、ORPO、clinical DPO。
- 适配合同：LoRA/QLoRA、基础模型 revision、数据指纹与 PEFT 制品。

## 七条研究路线

| 路线 | 关键阶段 |
|---|---|
| BAGEL SFT | joint SFT |
| RecA | reconstruction alignment |
| Uni-CoT | hierarchical CoT SFT |
| IRG | think/generate → reflect/refine |
| UniGame | self-adversarial update |
| UniPath | four executors → planner |
| LatentUMM | latent alignment → latent dynamics |

发现与计划：

```bash
medumm post-train --list-methods
medumm post-train --template reca > reca-medical.yaml
medumm post-train --config reca-medical.yaml --plan
```

## 证据等级

- `paper_profile_plan`：原生入口和阶段图可以解析。
- `contract_execution`：CLI、子进程、阶段依赖和制品合同执行成功。
- `paper_runtime`：固定官方/参考实现、真实数据和模型完成训练。

前两者不得被描述成第三者。真实医学训练还要补充下游医学评测和安全审计。

