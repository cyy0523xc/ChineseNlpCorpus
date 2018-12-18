# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年07月03日 星期二 21时51分54秒
import csv


with open('./online_shopping_10_cats.csv', encoding='utf8') as r, \
    open('../../format_datasets/online_shopping_10_cats/test_online_shopping_10_cats.csv', 'w', encoding='utf8') as test, \
    open('../../format_datasets/online_shopping_10_cats/train_online_shopping_10_cats_pos.txt', 'w', encoding='utf8') as pos, \
    open('../../format_datasets/online_shopping_10_cats/train_online_shopping_10_cats_neg.txt', 'w', encoding='utf8') as neg:
    index = 0
    test_csv = csv.DictWriter(test, ['label', 'cat', 'content'])
    test_csv.writeheader()
    for row in csv.DictReader(r):
        index += 1
        if index % 5 == 0:
            test_csv.writerow({
                'label': row['label'],
                'cat': row['cat'],
                'content': row['review']
            })
            continue

        content = row['review'].replace("\n", ' ').strip() + "\n"
        if row['label'] == '1':
            pos.write(content)
        else:
            neg.write(content)

print('ok')
