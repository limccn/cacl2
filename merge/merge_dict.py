import os

"""
检索完成的词汇合并统计
最终输出合并完的txt文件及词汇数量
输出路径：merge/output/financial/
取xx_finally.txt文件

"""


def merge_word():
    mba_words = []
    count = 0
    with open('input/financial/mba_dict.txt', 'r', encoding='utf-8') as mba:
        for line in mba.readlines():
            mba_words.append(line.strip())

    for root, dirs, files in os.walk('input'):
        if root == r'input\close':
            continue
        print(root)
        print(dirs)
        print(files)

        merge_files = []
        for file in files:
            if file.endswith('finally.txt'):
                merge_files.append(file)

        for path in merge_files:
            words = []
            full_path = '%s/%s' % (root, path)
            with open(full_path, 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    line = line.strip()
                    if '3,n' in line:
                        temp_arr = line.split(',3,n')
                    else:
                        temp_arr = line.split(' 99 n')
                    temp_word = temp_arr[0]
                    if temp_word.strip() != '':
                        words.append(temp_word)
            # print(words)
            #读取扩充词汇
            extend_path = '%s/%s' % (root, path.replace('_finally', '_extend'))
            if os.path.exists(extend_path):
                extend_words = []
                with open(extend_path, 'r', encoding='utf-8') as file:
                    for line in file.readlines():
                        extend_words.append(line.strip())
                # 合并扩充词汇
                words.extend(extend_words)
            # 金融词汇合并mba词
            if root == r'input\financial':
                # 合并mba词汇
                words.extend(mba_words)
            words = list(set(words))
            write_path = 'output/%s' % path.replace('_finally', '')
            dict_count = len(words)
            count = count + dict_count
            print('%s: %s' % (write_path, "{:,}".format(dict_count)))
            with open(write_path, 'w', encoding='utf-8') as w:
                for word in words:
                    w.write('%s 99 n\n' % word)

    print("{:,}".format(count))
    pass


if __name__ == '__main__':
    merge_word()