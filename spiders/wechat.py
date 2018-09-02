#-*- coding：utf-8 -*-
#导入需要使用的相关模块
import itchat
# import re
# import jieba
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud,ImageColorGenerator
# import numpy as np
# import PIL.Image as Image
# from os import path
# from scipy.misc import imread

# 登录方法，会弹出登录二维码，用微信扫描登录
itchat.auto_login()

#关于所有微信还有的资料信息都封装在这个方法里
friends = itchat.get_friends(update=True)[0:]

#获取好友性别信息
# male = female = other = 0

#遍历好友信息
# for i in friends[1:]:
#     #按照微信资料上的信息规则，男1，女2，其他3
#     sex = i['Sex']
#     if sex == 1:
#         male += 1
#     elif sex == 2:
#         female +=1
#     else:
#         other +=1

total = len(friends[1:])
print(total)
# print('男生好友：%.2f%%' % (float(male)/total*100) + '\n' +
# '女生好友：%.2f%%' % (float(female)/total*100) + '\n' +
# '不明性别好友：%.2f%%' % (float(other)/total*100) + '\n' )