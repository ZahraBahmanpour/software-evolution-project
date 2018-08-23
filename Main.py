# import nltk
# from nltk.book import *
# def lexical_diversity(text):
#     return len(set(text)) / len(text)
#
# def percentage(count, total):
#     return 100 * count / total
# print("------------------------------------")
# #len(text3)
# print("-------------------")
# #len(set(text3))
# saying = ['After', 'all', 'is', 'said', 'and', 'done','more', 'is', 'said', 'than', 'done']
# tokens = set(saying)
# tokens = sorted(tokens)
# print("----------")
# print(tokens[-2:])
# print ("-------------")
# sent7= ['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the',
# 'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.']
# print([w for w in sent7 if len(w) < 4])
from mysqlConnector import *
s= MysqlDBConnector('localhost', 'User', 'jasper_7.2', 'gm_eclipse', '', '');
print('--------------------------------');