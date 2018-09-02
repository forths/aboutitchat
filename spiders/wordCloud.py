#-*- coding：utf-8 -*-
#导入需要使用的相关模块
import itchat
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
import PIL.Image as Image
import time
from os import path
import os
from scipy.misc import imread

#登录方法，会弹出登录二维码，用微信扫描登录
itchat.auto_login()

#关于所有微信还有的资料信息都封装在这个方法里
friends = itchat.get_friends(update=True)[0:]

#获取好友签名信息
siglist = []

#遍历好友信息
for i in friends:
    #过滤信息
    signature = i['Signature'].strip().replace('span','').replace('class','').replace('emoji','')
    rep = re.compile('1f\d+\w*|[<>/=]')
    signature = rep.sub('',signature)
    siglist.append(signature)
#所有签名信息封装在text中
text = ''.join(siglist)
print(text)
#写入本地文件
textfile = open('info.txt','w',encoding="utf-8")
textfile.write(text)
text_from_file_with_apath = open('./info.txt').read()
print(text_from_file_with_apath)
wordlist = jieba.cut(text_from_file_with_apath)

word_space_split = " ".join(wordlist)
print(len(word_space_split))
print(word_space_split)


#画图
coloring = plt.imread('./haha.jpg')
#设置词云相关属性
my_wordcloud = WordCloud(background_color='white',
                        max_words=2000,
                        mask=coloring,
                        max_font_size=100,
                        random_state=42,
                        font_path='‪C:\Windows\Fonts\simkai.ttf').generate_from_text(word_space_split)

image_colors = ImageColorGenerator(coloring)

my_wordcloud.recolor(color_func=image_colors)
print(image_colors)
print(my_wordcloud)

#显示词云
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()
d = path.dirname(__file__)
# 保存图片
my_wordcloud.to_file(path.join(d, "签名.png"))