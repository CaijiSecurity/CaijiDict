from pypinyin import lazy_pinyin

with open('姓氏.txt', 'r') as f:
    all_surname_str = f.read()

all_surname_list = ['{0}\n'.format(surname) for surname in all_surname_str.split(',')]
all_surname_pinyin_list = ['{0}\n'.format(lazy_pinyin(surname)[0]) for surname in all_surname_str.split(',')]

surnames_len = len(all_surname_list)

with open('surname-{0}.txt'.format(str(surnames_len)), 'w') as f:
    f.writelines(all_surname_list)

with open('surname-pinyin-{0}.txt'.format(str(surnames_len)), 'w') as f:
    f.writelines(all_surname_pinyin_list)