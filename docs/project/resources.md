# 模型与数据资源体系

资源目录的作用是把扩展规模变成可查询、可治理的工程对象，而不是一张“支持列表”。

## 当前规模

- 32 个医学多模态模型 release。
- 34 个医学评测数据集。
- 覆盖医学生成式 VLM、对比编码器、2D、多视图、3D 切片与医学视频边界。
- 覆盖 VQA、推理、安全、公平性、报告、定位、测量、皮肤、眼科、病理、放射和手术视频。

## 每条资源必须记录

模型包括 artifact、来源、论文、官方代码、许可、访问级别、执行器家族、任务、输入模态、领域、参数量、语言、revision 策略和状态。

数据集包括 artifact、来源、论文、官方代码、许可、访问级别、adapter family、benchmark、任务、模态、领域、语言、指标、revision 策略和状态。

## 常用命令

```bash
medumm resources list --kind model
medumm resources list --kind dataset
medumm resources show lingshu_7b --kind model
medumm resources template pathvqa --kind dataset
medumm resources validate
```

## 访问并不等于授权

`open`、`gated`、`credentialed`、`request` 是不同访问等级。平台保存链接和条件不代表用户自动获得数据使用权。MIMIC-CXR、CheXpert 等资源仍需遵守各自凭证、协议和用途限制。

完整目录以 [MedUMM 源码](https://github.com/lixiangcog/MedUMM/tree/main/src/medumm/resources/catalog) 为准。

