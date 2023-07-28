#-*- encoding:utf-8 -*-
from __future__ import print_function

# import sys
# from imp import reload
#
# try:
#     reload(sys)
#     sys.setdefaultencoding('utf-8')
# except:
#     pass

import codecs
from textrank4zh_test import TextRank4Keyword, TextRank4Sentence

text = str(input("请输入您想要总结的话：（中文）"))
# 你这个事啊，我们讲不是说，不是说不办，那么但是呢，没有说啊，没有任何一件事我们谈说，说一定怎么怎么样，说不‌‌‌‌‌‌‌‌‌行吗?也不是，我们讲事在人为啊，我们可以想办法啊，可以想办法，这样，你这个晚一点，咱们到时候呢，对吧，我们这个，对吧，包括哎我这个到时候你看一看对吧，完了呢我给你把这个事对吧，好吧就先这样。
tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
print(text)
print()
print( '前五个关键词：' )
for item in tr4w.get_keywords(5, word_min_len=1):
    print(item.word, item.weight)

print()
print( '这句话的关键短语：' )
for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
    print(phrase)

tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')

print()
print( '全句摘要：' )
for item in tr4s.get_key_sentences(num=1):
    print(item.index, item.weight, item.sentence)

#
# for words in tr4w.words_all_filters:
#     print('/'.join(words))   # py2中是unicode类型。py3中是str类型。