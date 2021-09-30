import os
import codecs
import elasticsearch

"""
根据智库爬下的各行业词汇去elasticsearch上检索长词
其他行业用
输出路径：output/preview
取xx_finally.txt文件

"""


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
    out_file = codecs.open(path+name+'_categories.txt', "ab", "utf-8")
    for word in write_words:
        out_file.write('%s\n' % word)
    out_file.close()
    if len(temp_categories) > 0:
        get_categories(csv_path, path, name, temp_categories, write=False)


def get_words(path, out_path, name):
    file = codecs.open(path+name+'_categories.txt', "r", "utf-8")
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
    write_file = codecs.open(path+name+'_words.txt', "w", "utf-8")
    for word in output_words:
        write_file.write(word+'\n')
    write_file.close()

    search_es(out_path, name, output_words)

    pass


def search_es(out_path, name, output_words):
    vr = Vector2ES()
    for index, key_word in enumerate(output_words):
        print(key_word + '===>' + str(index))
        vr.search(key_word, out_path, name)


def write_file(words_list, key_word, out_path, file_name):
    count_file = codecs.open(out_path + file_name + '_count.txt', "ab", "utf-8")
    count_file.write(key_word + ',' + str(len(words_list)) + '\n')
    count_file.close()
    words_list.append(key_word)

    file = codecs.open(out_path+file_name+'.txt', "ab", "utf-8")
    for word in words_list:
        file.write(word + ',3,n\n')
    file.close()
    pass


def remove_duplicate_words(out_path, file_name):
    file = codecs.open('%s%s.txt' % (out_path, file_name), "r", "utf-8")
    words = []
    for line in file:
        words.append(line.strip())
    file.close()
    new_words = list(set(words))
    new_file = codecs.open('%s%s_finally.txt' % (out_path, file_name), "w", "utf-8")
    for word in new_words:
        new_file.write('%s\n' % word)
    new_file.close()
    pass


def search_company_words():
    input_path = 'input/preview/计算机/'
    out_path = 'output/preview/计算机/'
    name = '710000'
    categories = ['计算机']
    csv_path = 'input/preview/计算机/mba_word_计算机.csv'
    get_categories(csv_path, input_path, name, categories)
    get_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)


def search_chemical_industry_words():
    input_path = 'input/preview/化工/'
    out_path = 'output/preview/化工/'
    name = '220000'
    categories = ['化工']
    csv_path = 'input/preview/化工/mba_word_化工.csv'
    get_categories(csv_path, input_path, name, categories)
    get_words(input_path, out_path, name)
    remove_duplicate_words(out_path, name)

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
    search_chemical_industry_words()

