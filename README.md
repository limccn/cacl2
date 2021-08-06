# CaCl2


Read this in other languages: [简体中文](https://github.com/limccn/cacl2/blob/master/README-zh_CN.md),[English](https://github.com/limccn/cacl2/blob/master/README.md)

CaCl2词库和NLP自然语言处理相关技术交流QQ群现已开通，欢迎加入。群号：482671237

## Introduction

### What is CaCl2?
CaCl2（CaCl2: Chinese Lexicon V2, Simple Chinese：CA中文语言词库） CaCl2 is originates from a Chinese natural language processing(NLP) researching project sponsored by a Chinese company.

CaCl2 project is an important part of CaOCl (CaOCl: Open Chinese Lexical Analyzer) Project.

### How does CaCl2 work?
CaCl2 analyses the existing large volumes of textual data obtain from Internet and reformats data into massive entries
, Catalogues and classifies the entries according to the financial industry classification standard [see reference.1],

### What can CaCl2 Lexicon do?
In the natural language processing (NLP) tasks, the CaCl2 lexicon helps break down language into shorter, elemental pieces.(Aka. tokenization)

the CaCl2 lexicon can be used for higher-level NLP tasks such as word segmentation, document summarization, contextual extraction, content categorization, etc.

### What is CaCl2 aim at?
CaCl2 project aims to build a consistent, complete and accurate industrial lexicon or dictionary collections for Internet. we make our best effort to achieve higher data integrity, provide a firm foundation for Chinese NLP works, Users would devote more attention to their business and research.


## Statistics
#### Entries
|  Date |  All  | Candidate  | Released  | Preview  |
| :----: | :----: |  :----: | :----: | :----: | 
| 2021-02-01 | 21,000,000 | 3,000,000 | 5,480,494 | 280,000 |

#### Dictionaries
|  Date | Class | Industries | Released  | Preview |  Closing  | 
| :----: | :----: | :----: | :----: | :----: | :----: |
| 2021-02-01 | Class-1 |  28  |  2 | 26 | 0 |
| 2021-02-01 | Class-2 |  104 |  5 | 99 | 0 |

**Detail Statistics data please refer to [Statistics](https://github.com/limccn/cacl2/blob/master/STATUES.md)

## Get Start

### 1.Clone cacl2 or download dictionaries from GitHub
Clone cacl2
```shell
git clone https://github.com/limccn/cacl2.git
```
or Download a dictionary
```shell
wget https://github.com/limccn/cacl2/blob/master/archive/v0.2/[put dictionary code here].zip
```
### 2.Import dictionaries to your project & research environment

CaCl2 dictionary has a well formatted, can be use in many lexiconic tools.
#### 2.1 Example for using [jieba](https://github.com/fxsjy/jieba/)

```python
import jieba
dict_name = '480000.txt'
jieba.load_userdict(os.path.join(BASE_PATH_TO_DICT), dict_name))
```
#### 2.2 Example for using [IK Analyzer](https://code.google.com/archive/p/ik-analyzer/)

```xml
<properties>   
  <entry key="ext_dict">480000.txt;480100.txt;</entry>  
</properties> 
```

### 3.Run，Test and Enjoy CaCl2！


## Open-Source Schedule
### Released
|  Code | Name | Entries | Date | Version | Format | Download |
| :----: | :---- | :----:  | :----: | :----: | :----: | :----: |
| 480000 | Banking-Common | 52,105 | 2021-02 | v0.2 | txt  | [480000.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480000.zip) |
| 480100 | Banking-Bank | 232,434 | 2021-02 | v0.2 | txt | [480100.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480100.zip) |
| 490000 | Financials-Common | 365,87 | 2021-02 | v0.2 | txt | [490000.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/490000.zip) |
| 490100 | Financials-Securities | 338,428 | 2021-02 | v0.2 | txt | [490100.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/490100.zip) |
| 490200 | Financials-Insurance | 45,388 | 2021-02 | v0.2 | txt | [480200.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480200.zip) |

### Scheduled Release
|  Code  |  Name | Entries | Schedule | Version  | Format | Download |
| :----:  | :----  |  :----:  | :----: | :----: | :----: | :----: |
| 490300 | Financials-Others | 10,000 | 2Q 2021 | v0.2 | txt | [490300.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/490300.zip) |

### Technical Preview
Before dictionary finally publish/release, we published a technical preview dictionary contains 10,000 entries for every class-1 industry.
If you need further information about all entries, Please refer to [Statistics](https://github.com/limccn/cacl2/blob/master/STATUES.md)

|  Code  |  Name | Entries | Format | Download |
| :----:  | :----  |  :----:  | :----: | :----: |
| 110000 | Agriculture-Common | 10,000 |  txt | [110000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/110000.zip) |
| 210000 | Mining-Common | 10,000 |  txt | [210000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/210000.zip) |
| 220000 | Chemical-Common | 10,000 |  txt | [220000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/220000.zip) |
| 230000 | Ferrous Metal-Common | 10,000 |  txt | [230000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/230000.zip) |
| 240000 | Nonferrous Metal-Common | 10,000 |  txt | [240000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/240000.zip) |
| 270000 | Electronics-Common | 10,000 |  txt | [270000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/270000.zip) |
| 280000 | Automobile-Common | 10,000 |  txt | [280000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/280000.zip) |
| 330000 | Household Appliances-Common | 10,000 |  txt | [330000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/330000.zip) |
| 340000 | Food & Beverage-Common | 10,000 |  txt | [340000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/340000.zip) |
| 350000 | Textile & Apparel-Common | 10,000 |  txt | [350000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/350000.zip) |
| 360000 | Light-industry Manufacture-Common | 10,000 |  txt | [360000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/360000.zip) |
| 370000 | Health Care-Common | 10,000 |  txt | [370000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/370000.zip) |
| 410000 | Utility-Common | 10,000 |  txt | [410000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/410000.zip) |
| 420000 | Transportation-Common | 10,000 |  txt | [420000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/420000.zip) |
| 430000 | Real Estate-Common | 10,000 |  txt | [430000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/430000.zip) |
| 450000 | Commerce-Common | 10,000 |  txt | [450000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/450000.zip) |
| 460000 | Leisure Services-Common | 10,000 |  txt | [460000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/460000.zip) |
| 480000 | Banking-Common | 10,000 |  txt | [480000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/480000.zip) |
| 490000 | Financials-Common | 10,000 |  txt | [490000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/490000.zip) |
| 510000 | Conglomerate-Common | 10,000 |  txt | [510000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/510000.zip) |
| 610000 | Construction Material-Common | 10,000 |  txt | [610000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/610000.zip) |
| 620000 | Architectural Decoration-Common | 10,000 |  txt | [620000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/620000.zip) |
| 630000 | Electrical Equipment-Common | 10,000 |  txt | [630000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/630000.zip) |
| 640000 | Machinery Equipment-Common | 10,000 |  txt | [640000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/640000.zip) |
| 650000 | National Defense-Common | 10,000 |  txt | [650000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/650000.zip) |
| 710000 | Information Services-Common | 10,000 |  txt | [710000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/710000.zip) |
| 720000 | Media-Common | 10,000 |  txt | [720000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/720000.zip) |
| 730000 | Telecom-Common | 10,000 |  txt | [730000.zip](https://github.com/limccn/cacl2/blob/master/archive/preview/730000.zip) |


**Original raw data,  please refer to [/dicts](https://github.com/limccn/cacl2/tree/master/dicts)

**Detail Class-1 and 2 industries dictionaries, Please refer to [Statistics](https://github.com/limccn/cacl2/blob/master/STATUES.md)

## Comparison and Test
### 1.Comparsion 
#### 1.1 Compare CaCl2 Dictionary and [jieba](https://github.com/fxsjy/jieba/)（@CaoWJ）Dictionary

##### Text for test
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
##### Implement jieba with standard dictionary (demo)
```python
import jieba
seg_list = jieba.cut(text, cut_all=False)
print("jieba: " + "/ ".join(seg_list))
```
##### Jieba Output:
```
/ A股/ 今日/ 迎来/ 4/ 月/ 开门红/ ，/ 三大/ 指数/ 集体/ 收涨/ ，/ 其中/ 沪/ 指/ 上涨/ 0.71%/ ，/ 收报/ 3466.33/ 点/ ；/ 深证/ 成指/ 上涨/ 1.46%/ ，/ 收报/ 13979.69/ 点/ ；/ 
/ 创业板/ 指/ 上涨/ 2.06%/ ，/ 收报/ 2815.41/ 点/ 。/ 市场/ 成交量/ 持续/ 低迷/ ，/ 两市/ 合计/ 成交/ 6577/ 亿元/ ，/ 行业/ 板块/ 涨跌互现/ ，/ 钢铁/ 板块/ 强势/ 领涨/ 。/ 
/ 东吴/ 证券/ 指出/ ，/ 目前/ 3/ 月/ 行情/ 已经/ 收官/ ，/ 进入/ 4/ 月份/ 后/ ，/ 一/ 季报/ 的/ 炒作/ 情绪/ 将/ 进一步/ 升温/ ，/ 因此/ 未来/ 市场/ 风格/ 将/ 以/ 估值/ 修复/ 和/ 业绩/ 成长/ 轮动/ 呈现/ ，/ 
/ 投资者/ 可/ 重点/ 关注/ 环比/ 业绩/ 增长/ 的/ 品种/ 以及/ 顺/ 周期/ 板块/ 。/ 
/ 中原/ 证券/ 认为/ ，/ 核心/ 资产/ 持续/ 上涨/ 的/ 动力/ 不足/ ，/ 场外/ 资金/ 入市/ 做/ 多/ 的/ 信心/ 不/ 强/ ，/ 沪/ 指/ 继续/ 围绕/ 半年线/ 震荡/ 整固/ 的/ 格局/ 依然/ 未改/ 。/ 
/ 建议/ 投资者/ 继续/ 关注/ 政策/ 面/ 以及/ 资金面/ 的/ 变化/ 情况/ 。/ 
```
##### Implement jieba with CaCl2 dictionary
```python
import jieba
dict_name = '490000.txt'
jieba.load_userdict(dict_name)
seg_list = jieba.cut(text, cut_all=False)
print("cacl2: " + "/ ".join(seg_list))
```
##### CaCl2 Output:
```
/ A股/ 今日/ 迎来/ 4/ 月/ 开门红/ ，/ 三大指数/ 集体/ 收涨/ ，/ 其中/ 沪指/ 上涨/ 0.71%/ ，/ 收报/ 3466.33/ 点/ ；/ 深证成指/ 上涨/ 1.46%/ ，/ 收报/ 13979.69/ 点/ ；/ 
/ 创业板指/ 上涨/ 2.06%/ ，/ 收报/ 2815.41/ 点/ 。/ 市场/ 成交量/ 持续/ 低迷/ ，/ 两市/ 合计/ 成交/ 6577/ 亿元/ ，/ 行业板块/ 涨跌互现/ ，/ 钢铁板块/ 强势/ 领涨/ 。/ 
/ 东吴证券/ 指出/ ，/ 目前/ 3/ 月/ 行情/ 已经/ 收官/ ，/ 进入/ 4/ 月份/ 后/ ，/ 一/ 季报/ 的/ 炒作/ 情绪/ 将/ 进一步/ 升温/ ，/ 因此/ 未来/ 市场/ 风格/ 将/ 以/ 估值/ 修复/ 和/ 业绩/ 成长/ 轮动/ 呈现/ ，/ 
/ 投资者/ 可/ 重点/ 关注/ 环比/ 业绩/ 增长/ 的/ 品种/ 以及/ 顺/ 周期/ 板块/ 。/ 
/ 中原证券/ 认为/ ，/ 核心资产/ 持续/ 上涨/ 的/ 动力/ 不足/ ，/ 场外资金/ 入市/ 做多/ 的/ 信心/ 不/ 强/ ，/ 沪指/ 继续/ 围绕/ 半年线/ 震荡/ 整固/ 的/ 格局/ 依然/ 未改/ 。/ 
/ 建议/ 投资者/ 继续/ 关注/ 政策面/ 以及/ 资金面/ 的/ 变化/ 情况/ 。/ 
```
* **Comparsion**

![Compare CaCl2 and Jieba dictionary](https://github.com/limccn/cacl2/blob/master/docs/images/jieba.png)

#### 1.2 Word segmentation compare with [招金词酷](https://mp.weixin.qq.com/s/CuSZQ-BVZTzVS1ljYLcaKw?)（@CaoWJ）

##### 招金词酷(version 1.1) Output
```
A股  今日  迎来  4  月  开门红  三大  指数  集体  收涨  其中  沪指  上涨  0.71  %  收报  3466.33  点  深证  成指  上涨  1.46  %  收报  13979.69  点  
创业板  指  上涨  2.06  %  收报  2815.41  点  市场  成交量  持续  低迷  两  市  合计  成交  6577  亿元  行业板块  涨跌互现  钢铁板块  强势  领涨  
东吴证券  指出  目前  3  月  行情  已经  收官  进入  4  月份  后  一  季报  的  炒作  情绪  将  进一步  升温  因此  未来  市场  风格  将  以  估值  修复  和  业绩  成长  轮动  呈现  
投资者  可  重点关注  环比  业绩增长  的  品种  以及  顺  周期  板块  
中原证券  认为  核心  资产  持续  上涨的  动力  不足  场外  资金  入市  做  多  的  信心  不  强  沪指  继续  围绕  半年线  震荡  整固  的  格局  依然  未改  
建议投资者  继续关注  政策面  以及  资金面  的  变化  情况
```

* **Comparsion**

![Compare CaCl2 and 招金词酷](https://github.com/limccn/cacl2/blob/master/docs/images/zhaojinciku.png)
#### 1.3 Document summarization compare with [招金词酷](https://mp.weixin.qq.com/s/CuSZQ-BVZTzVS1ljYLcaKw?)（@CaoWJ）
![Document summarization]()

### 2. Test and Score
#### 2.1 industrial test dataset
Word segmentation test use for different industrial textual data
##### 2.1.1 Word segmentation use financial industry（banking industry Only）dictionary
###### Sample: Word segmentation using CaCl2（source code written in python）
```python
import jieba
dict_name = '480100.txt'
jieba.load_userdict(dict_name)
seg_list = jieba.cut(text, cut_all=False)
print("cacl2: " + "/ ".join(seg_list))
```
![Financial industry（banking industry Only） Word segmentation](https://github.com/limccn/cacl2/blob/master/docs/images/480100.png)

[Word segmentation output](https://github.com/limccn/cacl2/raw/master/docs/480100_cacl2_seg.txt)
##### 2.1.2 Word segmentation use Financial industry（Except banking industry）dictionary
###### Sample: Word segmentation using CaCl2（source code written in python）
```python
import jieba
dict_name = '490000.txt'
jieba.load_userdict(dict_name)
seg_list = jieba.cut(text, cut_all=False)
print("cacl2: " + "/ ".join(seg_list))
```
![Financial industry（Except banking industry） Word segmentation](https://github.com/limccn/cacl2/blob/master/docs/images/490000.png)

[Word segmentation output](https://github.com/limccn/cacl2/raw/master/docs/490000_cacl2_seg.txt)

#### 2.2 Standard test dataset
Word segmentation test use Standard Chinese test dataset
##### 2.2.1 Score for [Chinese Treebank（CTB5）](https://www.cs.brandeis.edu/~clp/ctb/)
![Score for CTB5]()
##### 2.2.2 Score for [International Chinese Word Segmentation Bakeoff（ICWB2）](http://sighan.cs.uchicago.edu/bakeoff2005/)
Score for ICWB：
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
![Test word segmentation with ICWB2](https://github.com/limccn/cacl2/blob/master/docs/images/score.png)

[Score for ICWB](https://github.com/limccn/cacl2/raw/master/docs/score.txt)

## History and changelogs
### 1.Regular releases
| Version |  Date | Changelogs |
| :----: | :----: | :---- |
| 0.2 | 2021 | latest |
| 0.1.1 | 2020 | Catalogues and classifies all entries into 28 class-1 industries and 240 class-2 industries|
| 0.1 | 2019 | First released version，contains overs 20 million entries，data mainly obtain from Baidu baike，Wikipedia |

### 2.Monthly/Quarterly releases
| Version |  Circle |  Date | Changelogs |
| :----: | :----: | :----: | :---- |
| v0.2.21.07 | monthly | 2021-08-05 | Dictionaries for agriculture,transportation and utility added |
| v0.2.21.06 | monthly | 2021-07-05 | Dictionaries for chemical, ferrous and nonferrous metal added |
| v0.2.21.05 | monthly | 2021-06-06 | Dictionaries for agriculture, commerce & trade and real estate added |
| v0.2.21.04 | monthly | 2021-05-07 | ICWB2 test and code added |
| v0.2.21.03 | monthly | 2021-04-06 | Comparsion test and code added |
| v0.2.21.02 | monthly | 2021-03-01 | Candidate entries added |
| v0.2.21.01 | monthly | 2021-02-01 | Release: banking and financials dictionary  |
| v0.2.20.12 | monthly | 2021-01-01 | v0.2 Initial version |

**Detail monthly/quarterly releases history, please refer to [Auto-Release history](https://github.com/limccn/cacl2#2monthlyqurterly-releases)

## License
### Open-Source license
CaCl2 is released Under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)。
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

### Creative Commons license
Text, Lexicon/Dictionaries, Models are under 
[Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)。

![CC BY-NC-SA](https://github.com/limccn/cacl2/blob/master/docs/images/cc_by_nc_sa.png)


## Contribute
CaCl2 Thanks for contributions from all contributors. 
We welcome all the contributions to CaCl2 and appreciate for your feedback very much.
### 1.Become A Contributor
#### 1.1 Fork or Star CaCl2

#### 1.2 Join CaCl2 community

#### 1.3 Join online discussion group, Tencent QQ Group:482671237


### 2.Contributor
@CaoWJ @ZhouXF

## FAQ

## Disclosure
CaCl2 and its data comes from the information published on the Internet. CaCl2 does not guarantee the integrity and correctness of the data. CaCl2 does not constitute any investment suggestion.

As Contributor, we have no positions in any stocks mentioned. We have no business relationship with any company whose stock is mentioned in this article. 

## Reference
1.[Industry Classification Standard of SWSI.2014](https://github.com/limccn/cacl2/blob/master/references/申银万国研究院行业分类标准.pdf)
