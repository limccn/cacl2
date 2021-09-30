

def process_dict():
    words = []
    with open('mba_temp_dict.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            temp_arr = str(line).split(',')
            word = temp_arr[2]
            words.append(word)
    words = list(set(words))
    with open('mba_dict.txt', 'w', encoding='utf-8') as wf:
        for word in words:
            wf.write('%s\n' % word)
    pass


if __name__ == '__main__':
    process_dict()