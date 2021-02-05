# CaCl2

## 一、CaCl2 简介
CaCl2（CaCl2: Chinese Lexicon）中文名称：CA中文语言词库，源于某国内金融行业NLP项目，通过分析既有语料获得海量词条数据，同时按金融行业标准进行词条编目和分类，在自然语言处理NLP过程中，可以用于分词，关键词提取、内容摘要，实体识别等用途。

CaCl2项目目标在于向互联网提供行业性的、完整的、准确的的词库，完成中文语言NLP的基础性工作，让用户将更多精力投入业务研究。

CaCl2是开放项目CaOCl（CA开放中文词法分析工具包）重要组成部分。

#### CaCl2的统计数据：
[CaCl2开放状态统计](https://github.com/limccn/cacl2/blob/master/STATUES.md)


## 二、快速开始

### 1.Clone或按需下载CaCl2词库
```shell
git clone https://github.com/limccn/cacl2.git
```

### 2.导入和配置词库
CaCl2公开的词库支持在多种分词工具和环境中使用。
#### 2.1 在[jieba分词](https://github.com/fxsjy/jieba/)使用示例

```python
import jieba
dict_name = '480000.txt'
jieba.load_userdict(os.path.join(BASE_PATH_TO_DICT), dict_name))
```

### 3.测试和开始使用CaCl2，Enjoy！


## 三、词库开源计划
### 1.已开源
|  No. | 词库名称 | 词条数量 | 公开时间 | 当前版本 | 格式 | 下载地址 |
| :----: | :---- | :----:  | :----: | :----: | :----: | :----: |
| 480000 | 银行-通用 | 10000 | 2021-02-01 | v0.2 | txt  | [480000.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480000.zip) |
| 480100 | 银行-银行 | 10000 | 2021-02-01 | v0.2 | txt | [480100.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480100.zip) |
| 490000 | 非银金融-通用 | 10000 | 2021-02-01 | v0.2 | txt | [490000.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/490000.zip) |
| 490100 | 非银金融-证券 | 10000 | 2021-02-01 | v0.2 | txt | [490100.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/490100.zip) |
| 490200 | 非银金融-保险 | 10000 | 2021-02-01 | v0.2 | txt | [480200.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480200.zip) |

### 2.计划开源
|  No.  |  词库名称 | 词条数量 | 计划公开时间 | 当前版本  | 格式 | 下载地址 |
| :----:  | :----  |  :----:  | :----: | :----: | :----: | :----: |
| 490300 | 非银金融-多元金融 | 10000 | 2021-02-01 | v0.2 | txt | [480300.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480300.zip) |

### 3.预览版
|  No.  |  词库名称 | 收录数量 | 格式 | 下载地址 |
| :----:  | :----  |  :----:  | :----: | :----: |
| 110000 | 农林牧渔-通用 | 10000 | txt | [110000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/110000.zip) |
| 210000 | 采掘-通用 | 10000 | txt | [210000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/210000.zip) |
| 220000 | 化工-通用 | 10000 | txt | [220000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/220000.zip) |
| 230000 | 钢铁-通用 | 10000 | txt | [230000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/230000.zip) |
| 240000 | 有色金属-通用 | 10000 | txt | [240000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/240000.zip) |
| 270000 | 电子-通用 | 10000 | txt | [270000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/270000.zip) |
| 280000 | 汽车-通用 | 10000 | txt | [280000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/280000.zip) |
| 330000 | 家用电器-通用 | 10000 | txt | [330000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/330000.zip) |
| 340000 | 食品饮料-通用 | 10000 | txt | [340000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/340000.zip) |
| 350000 | 纺织服装-通用 | 10000 | txt | [350000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/350000.zip) |
| 360000 | 轻工制造-通用 | 10000 | txt | [360000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/360000.zip) |
| 370000 | 医药生物-通用 | 10000 | txt | [370000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/370000.zip) |
| 410000 | 公用事业-通用 | 10000 | txt | [410000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/410000.zip) |
| 420000 | 交通运输-通用 | 10000 | txt | [420000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/420000.zip) |
| 430000 | 房地产-通用 | 10000 | txt | [430000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/430000.zip) |
| 450000 | 商业贸易-通用 | 10000 | txt | [450000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/450000.zip) |
| 460000 | 休闲服务-通用 | 10000 | txt | [460000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/460000.zip) |
| 480000 | 银行-通用 | 10000 | txt | [480000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/480000.zip) |
| 490000 | 非银金融-通用 | 10000 | txt | [490000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/490000.zip) |
| 510000 | 综合-通用 | 10000 | txt | [510000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/510000.zip) |
| 610000 | 建筑材料-通用 | 10000 | txt | [610000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/610000.zip) |
| 620000 | 建筑装饰-通用 | 10000 | txt | [620000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/620000.zip) |
| 630000 | 电气设备-通用 | 10000 | txt | [630000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/630000.zip) |
| 640000 | 机械设备-通用 | 10000 | txt | [640000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/640000.zip) |
| 650000 | 国防军工-通用 | 10000 | txt | [650000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/650000.zip) |
| 710000 | 计算机-通用 | 10000 | txt | [710000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/710000.zip) |
| 720000 | 传媒-通用 | 10000 | txt | [720000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/720000.zip) |
| 730000 | 通信-通用 | 10000 | txt | [730000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/730000.zip) |


#### **详细的开放状态请参考以下链接地址
[CaCl2开放状态统计](https://github.com/limccn/cacl2/blob/master/STATUES.md)


## 四、使用效果
### 1.工具测试对比
#### 1.1 使用XXXX标准词库和XXXX词库测试XXXX结果对比（@CaoWJ）
![使用XXXX标准词库和XXXX词库测试XXXX结果对比]()
#### 1.2 使用CaCl2的XXX词库对XXXX进行分词（@CaoWJ）
![使用CaCl2的XXX词库对XXXX进行分词]()
#### 1.3 使用CaCl2的XXX词库对XXXX提出摘要（@CaoWJ）
![使用CaCl2的XXX词库对XXXX提出摘要]()

### 2.指标和得分
#### 2.1 行业数据集测试
##### 2.1.1 金融行业，XXXX测试
##### 2.1.2 金融行业，XXXX测试
#### 2.2 标准数据集测试
##### 2.2.1 标准数据集Chinese Treebank（CTB5）上测试分词，[链接](https://www.cs.brandeis.edu/~clp/ctb/)
##### 2.2.2 标准数据集International Chinese Word Segmentation Bakeoff（ICWB2）上测试分词，[链接](http://sighan.cs.uchicago.edu/bakeoff2005/)


## 五、历史和变更日志
### 1.定期发布版本
| 版本 | 发布时间 | 变更日志 |
| :----: | :----: | :---- |
| 0.1 | 2020 | XXXX |
| 0.2 | 2020 | XXXX |

### 2.自动发布版本
| 最新版本 | 发布周期 | 发布时间 | 变更日志 |
| :----: | :----: | :----: | :---- |
| v0.2.21.01 | monthly | 2021-02-01 | XXXX |
| v0.2.20.12 | monthly | 2021-01-01 | XXXX |
| v0.2.20.11 | monthly | 2020-12-01 | XXXX |
#### **历史自动发布版本请参考以下链接地址
[链接地址](http://)

## 六、License 许可证
### 1.开源软件许可证
CaCl2的源代码在[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)许可下开源。
```
    Copyright 2021 limc.cn All rights reserved.
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
```

### 2.共同创作许可证
CaCl2开放的词库，语料，模型等资料沿用[Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)知识共享许可协议。

![CC BY-NC-SA](https://github.com/limccn/cacl2/blob/master/docs/images/cc_by_nc_sa.png)


## 七、贡献和贡献者
### 1.如何贡献？
#### 1.1 Fork或Star我们的CaCl2
#### 1.2 在Github上参与CaCl2社区讨论

### 2.贡献者
@CaoWJ


## 八、常见问题FAQ


## 九、其他说明
CaCl2的部分内容来自互联网公开的信息和数据资料，CaCl2不保证数据的完整性和正确性，不构成任何建议。


## 十、参考资料
1.[申银万国研究院行业分类标准.2014](https://github.com/limccn/cacl2/blob/master/references/申银万国研究院行业分类标准.pdf)
