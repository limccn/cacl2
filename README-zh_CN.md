# CaCl2

其他语言版本: [简体中文](https://github.com/limccn/cacl2/blob/master/README-zh_CN.md), [English](https://github.com/limccn/cacl2/blob/master/README.md)

CaCl2词库和NLP自然语言处理相关技术交流QQ群现已开通，欢迎加入。群号：482671237

## 一、CaCl2 简介
CaCl2（CaCl2: Chinese Lexicon）中文名称：CA中文语言词库，源于某国内金融行业NLP项目，通过分析既有语料获得海量词条数据，同时按金融行业标准进行词条编目和分类，在自然语言处理NLP过程中，可以用于分词，关键词提取、内容摘要，实体识别等用途。

CaCl2项目目标在于向互联网提供行业性的、完整的、准确的的词库，完成中文语言NLP的基础性工作，让用户将更多精力投入业务研究。

CaCl2是开放项目CaOCl（CA开放中文词法分析工具包）重要组成部分。

## 统计数据

#### 1.词条数

|  时间 |  总词条数 | 候选词条 | 已公开词条 | 预览版词条 |
| :----: | :----: |  :----: | :----: | :----: | 
| 2021-10-01 | 约21,000,000 | 约3,000,000 | 11,955,321 | 280,000 |

#### 2.行业字典数
|  时间 | 行业 | 词典数 | 已公开  | 预览版 | 未公开  | 
| :----: | :----: |  :----: | :----: | :----: | :----: |
| 2021-02-01 | 一级行业 |  28  |  2 | 26 | 0 |
| 2021-02-01 | 二级行业 |  104 |  5 | 99 | 0 |


**详细统计状态，请参考链接：[CaCl2开放状态统计](https://github.com/limccn/cacl2/blob/master/STATUES-zh_CN.md)



## 二、快速开始

### 1.Clone或按需下载CaCl2词库
Clone
```shell
git clone https://github.com/limccn/cacl2.git
```
下载
```shell
wget https://github.com/limccn/cacl2/blob/master/archive/v0.2/[字典代码].zip
```

### 2.导入和配置词库
CaCl2公开的词库支持在多种分词工具和环境中使用。
#### 2.1 在[jieba分词](https://github.com/fxsjy/jieba/)使用示例

```python
import jieba
dict_name = '480000.txt'
jieba.load_userdict(os.path.join(BASE_PATH_TO_DICT), dict_name))
```

#### 2.2 在 [IK Analyzer](https://code.google.com/archive/p/ik-analyzer/)使用示例

```xml
<properties>   
  <entry key="ext_dict">480000.txt;480100.txt;</entry>  
</properties> 
```

### 3.测试和开始使用CaCl2，Enjoy！


## 三、词库开源进度表
### 1.已开源
|  行业代码 | 词库名称 | 词条数量 | 公开时间 | 当前版本 | 格式 | 下载地址 |
| :----: | :---- | :----:  | :----: | :----: | :----: | :----: |
| 480000 | 银行-通用 | 52,105 | 2021-02 | v0.2 | txt  | [480000.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480000.zip) |
| 480100 | 银行-银行 | 232,434 | 2021-02 | v0.2 | txt | [480100.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480100.zip) |
| 490000 | 非银金融-通用 | 365,878 | 2021-02 | v0.2 | txt | [490000.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/490000.zip) |
| 490100 | 非银金融-证券 | 338,428 | 2021-02 | v0.2 | txt | [490100.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/490100.zip) |
| 490200 | 非银金融-保险 | 45,388 | 2021-02 | v0.2 | txt | [480200.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480200.zip) |

### 2.计划开源
|  行业代码  |  词库名称 | 词条数量 | 计划公开时间 | 当前版本  | 格式 | 下载地址 |
| :----:  | :----  |  :----:  | :----: | :----: | :----: | :----: |
| 490300 | 非银金融-多元金融 | 10,000 | 2Q 2021 | v0.2 | txt | [490300.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/490300.zip) |

### 3.技术预览版
公开发布词典前，我们提供28个一级行业的各1万个词条的技术预览，词典实际包含的词条数量，请参考链接：[CaCl2开放状态统计](https://github.com/limccn/cacl2/blob/master/STATUES-zh_CN.md)

|  行业代码  |  词库名称 | 收录数量 | 格式 | 下载地址 |
| :----:  | :----  |  :----:  | :----: | :----: |
| 110000 | 农林牧渔-通用 | 10,000 | txt | [110000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/110000.zip) |
| 210000 | 采掘-通用 | 10,000 | txt | [210000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/210000.zip) |
| 220000 | 化工-通用 | 10,000 | txt | [220000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/220000.zip) |
| 230000 | 钢铁-通用 | 10,000 | txt | [230000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/230000.zip) |
| 240000 | 有色金属-通用 | 10,000 | txt | [240000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/240000.zip) |
| 270000 | 电子-通用 | 10,000 | txt | [270000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/270000.zip) |
| 280000 | 汽车-通用 | 10,000 | txt | [280000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/280000.zip) |
| 330000 | 家用电器-通用 | 10,000 | txt | [330000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/330000.zip) |
| 340000 | 食品饮料-通用 | 10,000 | txt | [340000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/340000.zip) |
| 350000 | 纺织服装-通用 | 10,000 | txt | [350000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/350000.zip) |
| 360000 | 轻工制造-通用 | 10,000 | txt | [360000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/360000.zip) |
| 370000 | 医药生物-通用 | 10,000 | txt | [370000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/370000.zip) |
| 410000 | 公用事业-通用 | 10,000 | txt | [410000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/410000.zip) |
| 420000 | 交通运输-通用 | 10,000 | txt | [420000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/420000.zip) |
| 430000 | 房地产-通用 | 10,000 | txt | [430000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/430000.zip) |
| 450000 | 商业贸易-通用 | 10,000 | txt | [450000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/450000.zip) |
| 460000 | 休闲服务-通用 | 10,000 | txt | [460000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/460000.zip) |
| 480000 | 银行-通用 | 10,000 | txt | [480000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/480000.zip) |
| 490000 | 非银金融-通用 | 10,000 | txt | [490000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/490000.zip) |
| 510000 | 综合-通用 | 10,000 | txt | [510000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/510000.zip) |
| 610000 | 建筑材料-通用 | 10,000 | txt | [610000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/610000.zip) |
| 620000 | 建筑装饰-通用 | 10,000 | txt | [620000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/620000.zip) |
| 630000 | 电气设备-通用 | 10,000 | txt | [630000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/630000.zip) |
| 640000 | 机械设备-通用 | 10,000 | txt | [640000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/640000.zip) |
| 650000 | 国防军工-通用 | 10,000 | txt | [650000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/650000.zip) |
| 710000 | 计算机-通用 | 10,000 | txt | [710000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/710000.zip) |
| 720000 | 传媒-通用 | 10,000 | txt | [720000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/720000.zip) |
| 730000 | 通信-通用 | 10,000 | txt | [730000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/730000.zip) |



**原始格式的词条，请参考：[/dicts](https://github.com/limccn/cacl2/tree/master/dicts)

**详细的开放状态，请参考链接：[CaCl2开放状态统计](https://github.com/limccn/cacl2/blob/master/STATUES-zh_CN.md)


## 四、使用效果
### 1.工具测试对比
#### 1.1 使用CaCl2标准词库和Jieba标准库测试分词结果对比

##### 测试分词文本内容
```python
text = """
A股今日迎来4月开门红，三大指数集体收涨，其中沪指上涨0.71%，收报3466.33点；深证成指上涨1.46%，收报13979.69点；
创业板指上涨2.06%，收报2815.41点。市场成交量持续低迷，两市合计成交6577亿元，行业板块涨跌互现，钢铁板块强势领涨。
东吴证券指出，目前3月行情已经收官，进入4月份后，一季报的炒作情绪将进一步升温，因此未来市场风格将以估值修复和业绩成长轮动呈现，
投资者可重点关注环比业绩增长的品种以及顺周期板块。
中原证券认为，核心资产持续上涨的动力不足，场外资金入市做多的信心不强，沪指继续围绕半年线震荡整固的格局依然未改。
建议投资者继续关注政策面以及资金面的变化情况。

"""
```
##### Jieba标准库分词（代码示例）
```python
import jieba
seg_list = jieba.cut(text, cut_all=False)
print("jieba: " + "/ ".join(seg_list))
```
##### Jieba输出结果:
```
/ A股/ 今日/ 迎来/ 4/ 月/ 开门红/ ，/ 三大/ 指数/ 集体/ 收涨/ ，/ 其中/ 沪/ 指/ 上涨/ 0.71%/ ，/ 收报/ 3466.33/ 点/ ；/ 深证/ 成指/ 上涨/ 1.46%/ ，/ 收报/ 13979.69/ 点/ ；/ 
/ 创业板/ 指/ 上涨/ 2.06%/ ，/ 收报/ 2815.41/ 点/ 。/ 市场/ 成交量/ 持续/ 低迷/ ，/ 两市/ 合计/ 成交/ 6577/ 亿元/ ，/ 行业/ 板块/ 涨跌互现/ ，/ 钢铁/ 板块/ 强势/ 领涨/ 。/ 
/ 东吴/ 证券/ 指出/ ，/ 目前/ 3/ 月/ 行情/ 已经/ 收官/ ，/ 进入/ 4/ 月份/ 后/ ，/ 一/ 季报/ 的/ 炒作/ 情绪/ 将/ 进一步/ 升温/ ，/ 因此/ 未来/ 市场/ 风格/ 将/ 以/ 估值/ 修复/ 和/ 业绩/ 成长/ 轮动/ 呈现/ ，/ 
/ 投资者/ 可/ 重点/ 关注/ 环比/ 业绩/ 增长/ 的/ 品种/ 以及/ 顺/ 周期/ 板块/ 。/ 
/ 中原/ 证券/ 认为/ ，/ 核心/ 资产/ 持续/ 上涨/ 的/ 动力/ 不足/ ，/ 场外/ 资金/ 入市/ 做/ 多/ 的/ 信心/ 不/ 强/ ，/ 沪/ 指/ 继续/ 围绕/ 半年线/ 震荡/ 整固/ 的/ 格局/ 依然/ 未改/ 。/ 
/ 建议/ 投资者/ 继续/ 关注/ 政策/ 面/ 以及/ 资金面/ 的/ 变化/ 情况/ 。/ 
```
##### CaCl2标准词库分词（代码示例）
```python
import jieba
dict_name = '490000.txt'
jieba.load_userdict(dict_name)
seg_list = jieba.cut(text, cut_all=False)
print("cacl2: " + "/ ".join(seg_list))
```
##### CaCl2输出结果:
```
/ A股/ 今日/ 迎来/ 4/ 月/ 开门红/ ，/ 三大指数/ 集体/ 收涨/ ，/ 其中/ 沪指/ 上涨/ 0.71%/ ，/ 收报/ 3466.33/ 点/ ；/ 深证成指/ 上涨/ 1.46%/ ，/ 收报/ 13979.69/ 点/ ；/ 
/ 创业板指/ 上涨/ 2.06%/ ，/ 收报/ 2815.41/ 点/ 。/ 市场/ 成交量/ 持续/ 低迷/ ，/ 两市/ 合计/ 成交/ 6577/ 亿元/ ，/ 行业板块/ 涨跌互现/ ，/ 钢铁板块/ 强势/ 领涨/ 。/ 
/ 东吴证券/ 指出/ ，/ 目前/ 3/ 月/ 行情/ 已经/ 收官/ ，/ 进入/ 4/ 月份/ 后/ ，/ 一/ 季报/ 的/ 炒作/ 情绪/ 将/ 进一步/ 升温/ ，/ 因此/ 未来/ 市场/ 风格/ 将/ 以/ 估值/ 修复/ 和/ 业绩/ 成长/ 轮动/ 呈现/ ，/ 
/ 投资者/ 可/ 重点/ 关注/ 环比/ 业绩/ 增长/ 的/ 品种/ 以及/ 顺/ 周期/ 板块/ 。/ 
/ 中原证券/ 认为/ ，/ 核心资产/ 持续/ 上涨/ 的/ 动力/ 不足/ ，/ 场外资金/ 入市/ 做多/ 的/ 信心/ 不/ 强/ ，/ 沪指/ 继续/ 围绕/ 半年线/ 震荡/ 整固/ 的/ 格局/ 依然/ 未改/ 。/ 
/ 建议/ 投资者/ 继续/ 关注/ 政策面/ 以及/ 资金面/ 的/ 变化/ 情况/ 。/ 
```
##### 对比Jieba标准库测试分词结果对比图

![对比Jieba标准库测试分词结果对比图](https://github.com/limccn/cacl2/blob/master/docs/images/jieba.png)
#### 1.2 使用CaCl2和金融行业词库对比【招金词酷】进行分词

##### 【招金词酷】（版本1.1）的分词文本内容分词结果
```
A股  今日  迎来  4  月  开门红  三大  指数  集体  收涨  其中  沪指  上涨  0.71  %  收报  3466.33  点  深证  成指  上涨  1.46  %  收报  13979.69  点  
创业板  指  上涨  2.06  %  收报  2815.41  点  市场  成交量  持续  低迷  两  市  合计  成交  6577  亿元  行业板块  涨跌互现  钢铁板块  强势  领涨  
东吴证券  指出  目前  3  月  行情  已经  收官  进入  4  月份  后  一  季报  的  炒作  情绪  将  进一步  升温  因此  未来  市场  风格  将  以  估值  修复  和  业绩  成长  轮动  呈现  
投资者  可  重点关注  环比  业绩增长  的  品种  以及  顺  周期  板块  
中原证券  认为  核心  资产  持续  上涨的  动力  不足  场外  资金  入市  做  多  的  信心  不  强  沪指  继续  围绕  半年线  震荡  整固  的  格局  依然  未改  
建议投资者  继续关注  政策面  以及  资金面  的  变化  情况
```
##### 对比【招金词酷】（版本1.1）测试分词结果对比图

![CaCl2和金融行业词库对比【招金词酷】进行分词](https://github.com/limccn/cacl2/blob/master/docs/images/zhaojinciku.png)
#### 1.3 使用CaCl2和金融行业词库对比【招金词酷】进行分词提出摘要（@CaoWJ）
![使用CaCl2和金融行业词库对比【招金词酷】进行分词提出摘要]()

### 2.指标和得分
#### 2.1 行业数据集测试
##### 2.1.1 金融行业(银行行业)，分词测试
###### 代码示例（python）：使用CaCl2词库对某银行《银行贷款合同》进行分词测试
```python
import jieba
dict_name = '480100.txt'
jieba.load_userdict(dict_name)
seg_list = jieba.cut(text, cut_all=False)
print("cacl2: " + "/ ".join(seg_list))
```
![金融行业(银行行业)分词测试](https://github.com/limccn/cacl2/blob/master/docs/images/480100.png)

[详细分词测试结果地址](https://github.com/limccn/cacl2/raw/master/docs/480100_cacl2_seg.txt)
##### 2.1.2 金融行业(金融行业，不包含银行)，分词测试
###### 代码示例（python）：使用CaCl2词库对证券教材《移动平均线》章节进行分词测试
```python
import jieba
dict_name = '490000.txt'
jieba.load_userdict(dict_name)
seg_list = jieba.cut(text, cut_all=False)
print("cacl2: " + "/ ".join(seg_list))
```
![金融行业(金融行业，不包含银行)分词测试](https://github.com/limccn/cacl2/blob/master/docs/images/490000.png)

[详细分词测试结果地址](https://github.com/limccn/cacl2/raw/master/docs/490000_cacl2_seg.txt)
#### 2.2 标准数据集测试
##### 2.2.1 标准数据集Chinese Treebank（CTB5）上测试分词，[参考链接](https://www.cs.brandeis.edu/~clp/ctb/)
![标准数据集CTB5上测试分词]()
##### 2.2.2 标准数据集International Chinese Word Segmentation Bakeoff（ICWB2）上测试分词，[参考链接](http://sighan.cs.uchicago.edu/bakeoff2005/)
ICWB2标准数据集上测试分词的评分结果：
```
=== SUMMARY:
=== TOTAL INSERTIONS:	1796
=== TOTAL DELETIONS:	10090
=== TOTAL SUBSTITUTIONS:	12567
=== TOTAL NCHANGE:	24453
=== TOTAL TRUE WORD COUNT:	104372
=== TOTAL TEST WORD COUNT:	96078
=== TOTAL TRUE WORDS RECALL:	0.783
=== TOTAL TEST WORDS PRECISION:	0.851
=== F MEASURE:	0.815
=== OOV Rate:	0.058
=== OOV Recall Rate:	0.582
=== IV Recall Rate:	0.795
###	pku_cacl2_seg.txt	1796	10090	12567	24453	104372	96078	0.783	0.851	0.815	0.058	0.582	0.795
```

![标准数据集ICWB2上测试分词](https://github.com/limccn/cacl2/blob/master/docs/images/score.png)

[详细评分结果地址](https://github.com/limccn/cacl2/raw/master/docs/score.txt)

## 五、历史和变更日志
### 1.定期发布版本
| 版本 | 发布时间 | 变更日志 |
| :----: | :----: | :---- |
| 0.2 | 2021 | 发布中的版本 |
| 0.1.1 | 2020 | 使用申万行业分类对词库进行编目和分类，共28个一级行业和104个二级行业 |
| 0.1 | 2019 | 第一个发布版本，包含来自互联网的2100万中文词条，主要来自百度百科，维基中文百科等来源 |

### 2.自动发布版本
| 最新版本 | 发布周期 | 发布时间 | 变更日志 |
| :----: | :----: | :----: | :---- |
| v0.2.21.10 | monthly | 2021-10-01 | 新增二级行业分类。主要包括计算机和食品饮料。 |
| v0.2.21.09 | monthly | 2021-10-01 | 新增二级行业分类。不包括计算机和食品饮料。 |
| v0.2.21.08 | monthly | 2021-09-01 | 添加轻工制造、食品饮料、化工、公用事业等行数数据 |
| v0.2.21.07 | monthly | 2021-08-05 | 添加农林牧渔、交通运输、公用事业等行数数据 |
| v0.2.21.06 | monthly | 2021-07-05 | 添加化工、钢铁、有色金属等行数数据 |
| v0.2.21.05 | monthly | 2021-06-06 | 添加农林牧渔、商业贸易、房地产等行数数据 |
| v0.2.21.04 | monthly | 2021-05-07 | 添加ICWB2标准数据集测试结果 |
| v0.2.21.03 | monthly | 2021-04-06 | 公开金融行业测试数据结果 |
| v0.2.21.02 | monthly | 2021-03-01 | 增加28个行业候选词条约100万 |
| v0.2.21.01 | monthly | 2021-02-01 | 金融行业（银行和非银金融）行业词库发布 |
| v0.2.20.12 | monthly | 2021-01-01 | 版本0.2的初版，开源第一版，提供28个一级行业的各1万个词条预览 |

**历史自动发布版本，请参考链接: [版本历史](https://github.com/limccn/cacl2#2monthlyqurterly-releases)

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
感谢所有CaCl2贡献者的努力，我们欢迎所有愿意参与并贡献CaCl2项目的贡献者
### 1.如何贡献？
#### 1.1 Fork或Star我们的CaCl2
#### 1.2 在Github上参与CaCl2社区讨论
#### 1.3 加入讨论群组，QQ群：482671237

### 2.贡献者
@CaoWJ @ZhouXF

## 八、常见问题

## 九、其他说明
CaCl2的部分内容来自互联网公开的信息和数据资料，CaCl2不保证数据的完整性和正确性，不构成任何建议。

我们没有持有本文提及的相关证券，与本文提及的相关公司没有任何关联关系。

## 十、参考资料
1.[申银万国研究院行业分类标准.2014](https://github.com/limccn/cacl2/blob/master/references/申银万国研究院行业分类标准.pdf)
2.[中信证券行业分类标准.2020](https://github.com/limccn/cacl2/blob/master/references/中信证券行业分类标准.pdf)


## 捐助

如果您觉得这个项目对您有益，欢迎您给予捐助

### 1.ERC-20地址
```
0x9916688F2ff9678da19B0E510836dABf10606235
```
我们接受加密货币，您只需要将代币发送到上面的地址即可，谢谢。

### 2.捐助列表
| 日期   | 捐助地址 | 代币 | 数量 | 备注 |
| :----: | :----  | :----: | :----: | :---- |
| 2021-06-21 | 0x031c4D15b38A830BD55f7440DA062A48a1A8F18F | BNB | 0.02 | - | 

