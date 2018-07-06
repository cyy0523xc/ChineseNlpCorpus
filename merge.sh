#!/bin/bash
# 
# 合并成大的语料库
# Author: alex
# Created Time: 2018年07月04日 星期三 16时33分04秒
    #./format_datasets/weibo_senti_100k/weibo_senti_100k_neg.txt \
    #./format_datasets/weibo_senti_100k/weibo_senti_100k_pos.txt \

cat ./format_datasets/base/neg.txt \
    ./format_datasets/online_shopping_10_cats/online_shopping_10_cats_neg.txt \
    ./format_datasets/waimai_10k/waimai_10_neg.txt \
> tmp.txt
cat tmp.txt|sort|uniq > ./format_datasets/total_neg.txt

cat ./format_datasets/base/pos.txt \
    ./format_datasets/online_shopping_10_cats/online_shopping_10_cats_pos.txt \
    ./format_datasets/waimai_10k/waimai_10_pos.txt \
> tmp.txt
cat tmp.txt|sort|uniq > ./format_datasets/total_pos.txt

rm tmp.txt
