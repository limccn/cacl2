import os
import codecs
import elasticsearch

"""
根据智库爬下的各行业词汇去elasticsearch上检索长词
金融词汇用
输出路径：output/financial/
取xx_finally.txt文件

"""

# 


def get_categories(csv_path, path, name, categories, write=True):
    file = codecs.open(csv_path, "r", "utf-8")
    temp_categories = []
    for line in file:
        words = str(line).strip().split(',')
        if words[0] in categories and words[1] == 'categories':
            temp_categories.append(words[2])
    # print(temp_categories)
    write_words = []
    if write:
        write_words.extend(categories)
        write_words.extend(temp_categories)
    else:
        write_words.extend(temp_categories)
    out_file = codecs.open(path + name + '_categories.txt', "ab", "utf-8")
    for word in write_words:
        out_file.write('%s\n' % word)
    out_file.close()
    if len(temp_categories) > 0:
        get_categories(csv_path, path, name, temp_categories, write=False)


def get_words(path, out_path, name):
    file = codecs.open(path + name + '_categories.txt', "r", "utf-8")
    key_words = []
    for line in file:
        line = line.strip()
        if str(line).startswith('#'):
            continue
        if line in key_words:
            continue
        word = line
        key_words.append(word)
    file.close()

    output_words = []
    mba_file = codecs.open('input/finance_dict_mba.txt', "r", "utf-8")
    for mba_line in mba_file:
        words = mba_line.split(',')
        tem_key = words[0]
        use_word = words[1]
        for temp_word in key_words:
            if temp_word == tem_key:
                output_words.append(use_word)
    mba_file.close()
    # 添加分类词
    output_words.extend(key_words)
    # print(len(output_words))
    # 添加扩展词汇
    extend_path = path + name + '_words_extend.txt'
    if os.path.exists(extend_path):
        extend_file = codecs.open(extend_path, "r", "utf-8")
        for line in extend_file:
            line = line.strip()
            if str(line).startswith('#'):
                continue
            if line in key_words:
                continue
            word = line
            output_words.append(word)
        extend_file.close()

    output_words = list(set(output_words))
    print(len(output_words))
    write_file = codecs.open(path + name + '_words.txt', "w", "utf-8")
    for word in output_words:
        write_file.write(word + '\n')
    write_file.close()

    search_es(out_path, name, output_words)

    pass


def search_es(out_path, name, output_words):
    vr = Vector2ES()
    for index, key_word in enumerate(output_words):
        print(key_word + '===>' + str(index))
        vr.search(key_word, out_path, name)
    remove_duplicate_words(out_path, name)


def write_file(words_list, key_word, out_path, file_name):
    count_file = codecs.open(out_path + file_name + '_count.txt', "ab", "utf-8")
    count_file.write(key_word + ',' + str(len(words_list)) + '\n')
    count_file.close()
    words_list.append(key_word)

    file = codecs.open(out_path + file_name + '.txt', "ab", "utf-8")
    for word in words_list:
        file.write(word + ' 99 n\n')
    file.close()
    pass


def remove_duplicate_words(out_path, file_name):
    file = codecs.open('%s%s.txt' % (out_path, file_name), "r", "utf-8")
    words = []
    for line in file:
        words.append(line.strip())
    file.close()
    new_words = list(set(words))
    # new_words.sort()
    new_file = codecs.open('%s%s_finally.txt' % (out_path, file_name), "w", "utf-8")
    for word in new_words:
        if str(word).strip() == '':
            continue
        new_file.write('%s\n' % word)
    new_file.close()
    pass


# 获取追加的词
def get_more_words(path, out_path, name):
    file = codecs.open(path + name + '_words_more.txt', "r", "utf-8")
    key_words = []
    for line in file:
        line = line.strip()
        if str(line).startswith('#'):
            continue
        if line in key_words:
            continue
        word = line
        key_words.append(word)
    file.close()

    search_es(out_path, name, key_words)


def search_bank_words():
    input_path = 'input/financial/bank/'
    out_path = 'output/financial/bank/'
    name = 'bank'
    categories = ['银行', '银行法规', '外汇', '货币', '抵押', '质押', '拍卖', '理财', '金融危机']
    csv_path = 'input/financial/bank/mba_word_银行_印刷.csv'
    get_categories(csv_path, input_path, name, categories)
    get_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)


def search_bank_more_words():
    input_path = 'input/financial/bank/'
    out_path = 'output/financial/bank/'
    name = 'bank'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_bank_universal_words():
    input_path = 'input/financial/bank_universal/'
    out_path = 'output/financial/bank_universal/'
    name = '480000'
    categories = ['银行', '银行监管', '银行法规', '外汇', '货币', '理财', '抵押', '质押', '货币', '金融危机']
    csv_path = 'input/financial/bank/mba_word_银行_印刷.csv'
    get_categories(csv_path, input_path, name, categories)
    get_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)


def search_securities_words():
    input_path = 'input/financial/securities/'
    out_path = 'output/financial/securities/'
    name = '490100'
    categories = ['证券', '债券', '股票', '证券法规', '信用']
    csv_path = 'input/financial/securities/mba_word_证券.csv'
    get_categories(csv_path, input_path, name, categories)
    get_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)


def search_securities_more_words():
    input_path = 'input/financial/securities/'
    out_path = 'output/financial/securities/'
    name = '490100'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_insurance_words():
    input_path = 'input/financial/insurance/'
    out_path = 'output/financial/insurance/'
    name = '490200'
    categories = ['保险', '保险法规']
    csv_path = 'input/financial/insurance/mba_word_投资_银行_保险.csv'
    get_categories(csv_path, input_path, name, categories)
    get_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)


def search_insurance_more_words():
    input_path = 'input/financial/insurance/'
    out_path = 'output/financial/insurance/'
    name = '490200'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_universal_words():
    input_path = 'input/financial/universal/'
    out_path = 'output/financial/universal/'
    name = '490000'
    categories = ['证券', '基金', '债券', '期货', '信托', '保险', '期权', '融资', '信用', '典当', '抵押', '质押', '拍卖', '理财', '金融危机', '金融理论']
    csv_path = 'input/financial/universal/mba_word_非银金融.csv'
    get_categories(csv_path, input_path, name, categories)
    get_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)


def search_universal_more_words():
    input_path = 'input/financial/universal/'
    out_path = 'output/financial/universal/'
    name = '490000'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_490300_words():
    input_path = 'input/financial/490300/'
    out_path = 'output/financial/490300/'
    name = '490300'
    categories = ['期货', '信托', '期权', '融资', '典当', '抵押', '质押', '拍卖', '理财']
    csv_path = 'input/financial/universal/mba_word_非银金融.csv'
    get_categories(csv_path, input_path, name, categories)
    get_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)


def search_490300_more_words():
    input_path = 'input/financial/490300/'
    out_path = 'output/financial/490300/'
    name = '490300'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


# 具体的行业分词
def search_computer_more_words():
    input_path = 'input/preview/计算机/'
    out_path = 'output/preview/计算机/'
    name = '710000'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_mining_more_words():
    input_path = 'input/preview/采掘/'
    out_path = 'output/preview/采掘/'
    name = '210300'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_transportation_more_words():
    input_path = 'input/preview/交通运输/'
    out_path = 'output/preview/交通运输/'
    name = '420800'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_leisure_services_more_words():
    input_path = 'input/preview/休闲服务/'
    out_path = 'output/preview/休闲服务/'
    name = '460500'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_medical_biology_more_words():
    input_path = 'input/preview/医药生物/'
    out_path = 'output/preview/医药生物/'
    name = '370600'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_media_more_words():
    input_path = 'input/preview/传媒/'
    out_path = 'output/preview/传媒/'
    name = '720300'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_public_utility_more_words():
    input_path = 'input/preview/公用事业/'
    out_path = 'output/preview/公用事业/'
    name = '410400'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_griculture_forestry_animal_husbandry_fishery():
    input_path = 'input/preview/农林牧渔/'
    out_path = 'output/preview/农林牧渔/'
    name = '110800'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_chemical_industry_more_words():
    input_path = 'input/preview/化工/'
    out_path = 'output/preview/化工/'
    name = '220600'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_commercial_trade_more_words():
    input_path = 'input/preview/商业贸易/'
    out_path = 'output/preview/商业贸易/'
    name = '450500'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_national_defense_industry_more_words():
    input_path = 'input/preview/国防军工/'
    out_path = 'output/preview/国防军工/'
    name = '650400'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_household_electric_appliances_more_words():
    input_path = 'input/preview/家用电器/'
    out_path = 'output/preview/家用电器/'
    name = '330200'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_building_material_more_words():
    input_path = 'input/preview/建筑材料/'
    out_path = 'output/preview/建筑材料/'
    name = '610300'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_architectural_decoration_more_words():
    input_path = 'input/preview/建筑装饰/'
    out_path = 'output/preview/建筑装饰/'
    name = '620500'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_real_estate_more_words():
    input_path = 'input/preview/房地产/'
    out_path = 'output/preview/房地产/'
    name = '430200'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_nonferrous_metals_more_words():
    input_path = 'input/preview/有色金属/'
    out_path = 'output/preview/有色金属/'
    name = '240500'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_mechanical_equipment_more_words():
    input_path = 'input/preview/机械设备/'
    out_path = 'output/preview/机械设备/'
    name = '640500'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_automobile_more_words():
    input_path = 'input/preview/汽车/'
    out_path = 'output/preview/汽车/'
    name = '280400'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_electronics_more_words():
    input_path = 'input/preview/电子/'
    out_path = 'output/preview/电子/'
    name = '270400'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_electrical_equipment_more_words():
    input_path = 'input/preview/电气设备/'
    out_path = 'output/preview/电气设备/'
    name = '630400'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_textile_clothing_more_words():
    input_path = 'input/preview/纺织服装/'
    out_path = 'output/preview/纺织服装/'
    name = '350200'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_comprehensive_more_words():
    input_path = 'input/preview/综合/'
    out_path = 'output/preview/综合/'
    name = '510100'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_computer_more_words():
    input_path = 'input/preview/计算机/'
    out_path = 'output/preview/计算机/'
    name = '720200'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_light_industry_manufacturing_more_words():
    input_path = 'input/preview/轻工制造/'
    out_path = 'output/preview/轻工制造/'
    name = '360400'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_signal_communication_more_words():
    input_path = 'input/preview/通信/'
    out_path = 'output/preview/通信/'
    name = '730200'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_steel_more_words():
    input_path = 'input/preview/钢铁/'
    out_path = 'output/preview/钢铁/'
    name = '230100'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_bank_more_words():
    input_path = 'input/preview/银行/'
    out_path = 'output/preview/银行/'
    name = '480100'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_non_bank_finance_more_words():
    input_path = 'input/preview/非银金融/'
    out_path = 'output/preview/非银金融/'
    name = '490100'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


def search_food_and_beverage_more_words():
    input_path = 'input/preview/食品饮料/'
    out_path = 'output/preview/食品饮料/'
    name = '340300'
    get_more_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)
    pass


class Vector2ES(object):
    def __init__(self):
        self.es_client = elasticsearch.Elasticsearch(['111.229.148.99:9200'])
        self.indexes = ['2021064']

    def encoding(self, index_name, word, field='word', rtn_field='word'):
        result = self.es_client.search(index=index_name, size=10000, request_timeout=60 * 2, body={
            "_source": rtn_field,
            "query": {
                "match_phrase": {
                    field: word
                }
            }
        })
        total = result.get("hits").get("total").get("value")
        if int(total) >= 10000:
            return self.encoding_scroll(index_name, word=word, field='word', rtn_field='word')
        else:
            hits = result.get("hits")
            data = []
            if hits.get("hits"):
                for hit in hits.get("hits"):
                    temp_word = hit.get("_source").get(rtn_field)
                    if temp_word:
                        data.append(temp_word)
            return data

    def encoding_scroll(self, index_name, word, field='word', rtn_field='word'):
        result = self.es_client.search(index=index_name, scroll='3m', size=10000, request_timeout=60 * 2, body={
            "_source": rtn_field,
            "query": {
                "match_phrase": {
                    field: word
                }
            }
        })
        mdata = result.get("hits").get("hits")
        data = []
        if not mdata:
            return data
        total = result.get("hits").get("total").get("value")
        scroll_id = result.get("_scroll_id")
        print(total)
        for i in range(int(total / 10000)):
            print(i)
            res = self.es_client.scroll(scroll_id=scroll_id, scroll='3m')
            small_data = res.get("hits").get("hits")
            mdata = mdata + small_data
        self.es_client.clear_scroll(scroll_id=scroll_id)

        for hit in mdata:
            temp_word = hit.get("_source").get(rtn_field)
            if temp_word:
                data.append(temp_word)
        return data

    def search(self, key_word, out_path, file_name):
        # search_again_words = []
        words_list = self.encoding(self.indexes, word=key_word, field='word', rtn_field='word')
        write_file(words_list, key_word, out_path, file_name)
        # print(search_again_words)
        pass


if __name__ == '__main__':
    # search_bank_words()
    # search_bank_more_words()
    # search_securities_words()
    # search_insurance_more_words()
    # search_securities_more_words()
    # search_universal_words()
    # search_490300_words()
    # search_securities_more_words()
    # search_universal_more_words()
    # search_computer_more_words()
    # search_mining_more_words()
    # search_transportation_more_words()
    # search_leisure_services_more_words()
    # search_medical_biology_more_words()
    # search_media_more_words()
    # search_public_utility_more_words()
    # search_griculture_forestry_animal_husbandry_fishery()
    # search_chemical_industry_more_words()
    # search_commercial_trade_more_words()
    # search_national_defense_industry_more_words()
    # search_household_electric_appliances_more_words()
    # search_building_material_more_words()
    # search_architectural_decoration_more_words()
    # search_real_estate_more_words()
    # search_nonferrous_metals_more_words()
    # search_mechanical_equipment_more_words()
    # search_automobile_more_words()
    # search_electronics_more_words()
    # search_electrical_equipment_more_words()
    # search_textile_clothing_more_words()
    # search_comprehensive_more_words()
    # search_computer_more_words()
    # search_light_industry_manufacturing_more_words()
    # search_signal_communication_more_words()
    # search_steel_more_words()
    # search_bank_more_words()
    # search_non_bank_finance_more_words()
    search_food_and_beverage_more_words()