# -*- coding: utf-8 -*-
#
# 将语料库拆分为训练集和测试集
# Author: alex
# Created Time: 2018年07月04日 星期三 16时43分11秒


def parse(source, train, test):
    with open(source, encoding='utf8') as r, \
        open(train, 'w', encoding='utf8') as tr, \
        open(test, 'w', encoding='utf8') as te:
        i = 0
        for line in r.readlines():
            line = line.strip()
            if len(line) < 1:
                continue
            i += 1
            if i % 5 == 0:
                te.write(line+"\n")
            else:
                tr.write(line+"\n")


source = './format_datasets/total_neg.txt'
train = './format_datasets/total_train_neg.txt'
test = './format_datasets/total_test_neg.txt'
parse(source, train, test)

source = './format_datasets/total_pos.txt'
train = './format_datasets/total_train_pos.txt'
test = './format_datasets/total_test_pos.txt'
parse(source, train, test)

print('ok')
