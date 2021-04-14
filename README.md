# H&S气象

## 气象预测以及实时气象动态展示

#### 1 项目介绍：

​		初步研发了一套基于机器学习方法Scikit-learn(sklearn)与Python结合实现的气象预报以及气象动态展示系统，本系统分为两个模块，第一个模块为气象信息动态展示模块。使用Python作为后端语言，JavaScript、Html、CSS作为前端基本框架，实现天气动态展示。主要原理为：使用Python爬虫爬取天气数据到数据库中并通过JavaScript动态显示到前端页面。页面展示中国地图，单击即可进入省份地图，鼠标移动到即可显示当前城市的相关信息以及出行建议。第二个模块为气象预测模块，本模块主要采用随机树森林（RandomForest）作为场景模型，使用MAE（Mean_Absolute_Error）平均错误数值方法作为系统的评估方法。主要原理为：使用python爬虫，爬取去年相关天气数据做训练集和训练验证集，爬取当前日期半个月前到现在的每日天气数据做预测数据集，系统进行数据预处理后训练模型，模型基于最近前十五天的天气数据，对气温，降雨量，风力等参数作出预测，并将预测结果存入数据库，导入Html页面动态显示。通过测试分析试验，对比分析了青岛市的气象预测数据，各项数据误差在可接受范围之内，系统运行正常。

#### 2.效果：

①主页面：

![效果图2](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/效果图.png)

②光标经过省份

![效果图2](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/效果图2.png)

③点击省份

![效果图3](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/效果图3.png)

④光标经过市

![效果图4](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/效果图4.png)

#### 3 所用技术栈：

1. Python（3.9.0）结合Flask框架（1.1.2）。
2. 涉及到的机器学习相关库：Sklearn（0.24.0）、Panda（0.3.1）、Seaborn（0.11.1）、Joblib（1.0.0）。
3. 引擎：Apache-ECharts（5.0.0）。
4. 场景模型：随机树森林（RandomForest）。
5. 评估方法：MAE（Mean_Absolute_Error）平均错误数值方法。
6. 数据访问层：MySQL--connector 驱动。
7. 数据库：MySQL。
9. 前端相关:JavaScript、HTML、CSS、Ajax等。
10. 数据传输与保存格式：JSON。
11. 训练集于结果集数据来源：meteomanz.com。

#### 4 主要功能：

1. 全国实时天气动态展示（基于中国天气网每日四次更新）
2. 动态地图查询效果更直观
3. 内容包括出行建议/穿衣建议/紫外线指数等多项，实用且方便
4. 基于之前气象数据通过机器学习建立气象模型并训练、验证
5. 绘制未来一周气象折线图
6. 实现气象的未来七天的实时预测（平均气温、最高温度、最低温度、降雨量、风力）

#### 5 详情：

①城市数据库表结构

![城市数据库表结构](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/城市数据库表结构.png)

②预测数据库表结构

![预测数据库表结构](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/预测数据库表结构.png)

③目录结构

![目录结构](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/目录结构.png)

④JSON数据样式

![Json数据2](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/Json数据2.png)

⑤气象预测功能实现

![气象预测](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/气象预测.png)

⑥主界面详细1

![效果图5](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/效果图5.png)

⑦主界面详细2

![效果图6](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/效果图6.png)

⑧气象预测折线图

![效果图7](https://cdn.jsdelivr.net/gh/ZhsKevin/cdn/projects/weather/效果图7.png)





