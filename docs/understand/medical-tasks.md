# 医学任务为什么不能照搬自然图像分类

医学多模态输出可能是诊断答案、描述性报告、证据定位、物理测量、患者沟通或图像编辑。把这些任务统一成一个类别标签会丢失重要结构。

## 双轴任务模型

- **执行轴**决定调用哪个模型方法：`understanding`、`generation`、`editing`。
- **医学语义轴**描述临床研究意图，例如发现识别、解剖定位、诊断推理、报告生成、纵向比较或患者沟通。

例如：

| 请求 | 执行任务 | 医学语义 | 合适指标 |
|---|---|---|---|
| 判断胸片是否有积液 | understanding | finding recognition | 闭集准确率、校准 |
| 生成结构化影像报告 | understanding | report generation | 事实、否定、矛盾、关键发现 |
| 标出病灶位置 | understanding | anatomy localization | IoU、pointing accuracy |
| 测量病灶直径 | understanding | measurement | 单位感知 MAE、容差准确率 |
| 生成研究用合成影像 | generation | synthetic image generation | 专用生成指标与人工审查 |

## 缺失标注不是零分

如果数据没有框、物理单位或结构化事实，相关指标应标为 unavailable，而不是默认为模型答错。这个原则避免把数据缺失误报成模型性能。

