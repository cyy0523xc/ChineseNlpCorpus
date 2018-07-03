# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年07月03日 星期二 21时51分54秒
import csv


with open('./weibo_senti_100k.csv', encoding='utf8') as r, \
    open('../../format_datasets/weibo_senti_100k/weibo_senti_100k_pos.txt', 'w', encoding='utf8') as pos, \
    open('../../format_datasets/weibo_senti_100k/weibo_senti_100k_neg.txt', 'w', encoding='utf8') as neg:
    for row in csv.DictReader(r):
        content = row['review'].replace("\n", ' ').strip() + "\n"
        if row['label'] == '1':
            pos.write(content)
        else:
            neg.write(content)

print('ok')
