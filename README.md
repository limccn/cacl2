# CaCl2


Read this in other languages: [简体中文](https://github.com/limccn/cacl2/blob/master/README-zh_CN.md),[English](https://github.com/limccn/cacl2/blob/master/README.md)
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
| 2021-02-01 | 21,000,000 | 3,000,000 | 2,624,625 | 280,000 |

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
| 480000 | Banking-Common | 40,612 | 2021-02 | v0.2 | txt  | [480000.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480000.zip) |
| 480100 | Banking-Bank | 224,433 | 2021-02 | v0.2 | txt | [480100.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480100.zip) |
| 490000 | Financials-Common | 353,149 | 2021-02 | v0.2 | txt | [490000.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/490000.zip) |
| 490100 | Financials-Securities | 324,450 | 2021-02 | v0.2 | txt | [490100.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/490100.zip) |
| 490200 | Financials-Insurance | 31,020 | 2021-02 | v0.2 | txt | [480200.zip](https://github.com/limccn/cacl2/blob/master/archive/v0.2/480200.zip) |

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
![Compare Lexicon]()
#### 1.2 Word segmentation compare with [招金词酷](https://mp.weixin.qq.com/s/CuSZQ-BVZTzVS1ljYLcaKw?)（@CaoWJ）
![Word segmentation]()
#### 1.3 Document summarization compare with [招金词酷](https://mp.weixin.qq.com/s/CuSZQ-BVZTzVS1ljYLcaKw?)（@CaoWJ）
![Document summarization]()

### 2. Test and Score
#### 2.1 industrial test dataset
Word segmentation test use for different industrial textual data
##### 2.1.1 Word segmentation use financial industry（banking industry Only）dictionary
![Financial industry（banking industry Only） Word segmentation]()
##### 2.1.2 Word segmentation use Financial industry（Except banking industry）dictionary
![Financial industry（Except banking industry） Word segmentation]()

#### 2.2 Standard test dataset
Word segmentation test use Standard Chinese test dataset
##### 2.2.1 Score for [Chinese Treebank（CTB5）](https://www.cs.brandeis.edu/~clp/ctb/)
![Score for CTB5]()
##### 2.2.2 Score for [International Chinese Word Segmentation Bakeoff（ICWB2）](http://sighan.cs.uchicago.edu/bakeoff2005/)
![Score for ICWB]()

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
| v0.2.21.04 | monthly | 2021-02-01 | Release: banking and financials dictionary  |
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
### 2.Contributor
@CaoWJ

## FAQ

## Disclosure
CaCl2 and its data comes from the information published on the Internet. CaCl2 does not guarantee the integrity and correctness of the data. CaCl2 does not constitute any investment suggestion.

As Contributor, we have no positions in any stocks mentioned. We have no business relationship with any company whose stock is mentioned in this article. 

## Reference
1.[Industry Classification Standard of SWSI.2014](https://github.com/limccn/cacl2/blob/master/references/申银万国研究院行业分类标准.pdf)
