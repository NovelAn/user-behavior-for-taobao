# 淘宝用户行为分析

- 项目报告分享：[CSDN](https://blog.csdn.net/novelan/article/details/115235914)
- 项目源码链接：[Github Repo](https://github.com/NovelAn/user-behavior-for-taobao)
```shell
## 下载源码，请使用以下命令在你的本地上克隆repo

git init
git clone [项目源码链接]

```

## 项目简介
随着移动互联网技术的飞速发展和大众人均收入的增长，电商行业也随着技术的发展迅速崛起又快速分化。在当下大众消费需求日趋多样化的时代背景下，移动互联网行业特别是电商行业不再依靠用户红利实现业务增长，开始从粗放型的经营模式转向精细化管理，需要结合市场、渠道、用户行为等数据分析，对用户展开有针对性的运营活动，提供个性化、差异化的经营策略，从而实现运营目的。  
本项目使用Python分析淘宝平台2017年11月25日至2017年12月3日的用户行为数据，通过对网站流量、用户活跃率、用户行为转化漏斗、用户行为偏好等特征的分析，提供有针对性的运营策略。

## 工具库及版本要求

- python - <3.5+>
- numpy  --<1.16.5>
- pandas --<0.25.1>
- matplotlib.pyplot --<3.1.1>
- plotly --<4.12.0>

## 数据来源

本项目数据来源于阿里天池[User Behavior Data](https://tianchi.aliyun.com/dataset/dataDetail?dataId=649)，为了快速分析项目模型，项目仅截取完整数据集`UserBehavior`(3.41GB)的迷你数据集`UB_split_10.csv`(171.7MB)作为本项目的分析数据集。

## 分析步骤
- 提出问题
- 数据评估与清洗
- 探索性分析
- 结论和建议

## 评估指标
<img src='.\评估指标.png'>

## 分析框架
<img src='.\淘宝用户行为分析模型.png'>

## 特别说明
考虑到本项目使用的数据量较大，如果将整个分析过程放到同一个脚本下运行，项目会因为`Memory Error`强制中断。为了保证项目的流畅运行，编写另外一个脚本`UserBehavior_Taobao_wragledata.ipynb`来执行数据评估和清理这一步骤，完成后导出供本项目探索性分析和建模的数据集`updated_valid_df.csv`。整个探索性分析和建模的结果将展示在`UserBehavior_Taobao_EDA.ipynb`
