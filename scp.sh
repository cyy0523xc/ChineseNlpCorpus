#!/bin/bash
# 
# 
# Author: alex
# Created Time: 2018年07月03日 星期二 21时59分49秒

scp ./format_datasets/waimai_10k/waimai_10_neg.txt root@es5:/var/www/eyenlp/files/users/public/corpus/
scp ./format_datasets/waimai_10k/waimai_10_pos.txt root@es5:/var/www/eyenlp/files/users/public/corpus/

scp ./format_datasets/online_shopping_10_cats/online_shopping_10_cats_neg.txt root@es5:/var/www/eyenlp/files/users/public/corpus/
scp ./format_datasets/online_shopping_10_cats/online_shopping_10_cats_pos.txt root@es5:/var/www/eyenlp/files/users/public/corpus/

scp ./format_datasets/weibo_senti_100k/weibo_senti_100k_neg.txt root@es5:/var/www/eyenlp/files/users/public/corpus/
scp ./format_datasets/weibo_senti_100k/weibo_senti_100k_pos.txt root@es5:/var/www/eyenlp/files/users/public/corpus/


