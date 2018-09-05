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
from collections import Counter

def getnum_alpha_china_words(oprwords):
    _re_digist = re.compile('\d')
    _re_alpha = re.compile('[a-zA-Z]')
    _re_chinese = re.compile(u'[\u4e00-\u9fa5]')
    oprwords = oprwords.split()
    res = []
    for j in oprwords:
        tmp = ''
        for i in j:
            if _re_digist.search(i) or _re_alpha.search(i) or _re_chinese.search(i):
                tmp += i
            else:
                tmp += ''
        res.append(tmp)
    return ' '.join(res)
#登录方法，会弹出登录二维码，用微信扫描登录
itchat.auto_login()

#关于所有微信还有的资料信息都封装在这个方法里
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]
#获取好友签名信息
siglist = []

#遍历好友信息
for i in friends:
    #过滤信息
    signature = i['Signature'].strip().replace('span','').replace('class','').replace('emoji','')
    rep = re.compile('1f\d+\w*|[<>/=]')
    signature = rep.sub(' ',signature)
    signature = getnum_alpha_china_words(signature)
    siglist.append(signature)
#所有签名信息封装在text中
text = ' '.join(siglist)

#写入本地文件
textfile = open(user+'.txt','w',encoding="utf-8")
textfile.write(text)
textfile.close()

wordlist = jieba.cut(text,cut_all=True)
word_space_split = " ".join(wordlist).split(" ")
res = []
for i in word_space_split:
    if not i:
        continue
    else:
        if len(i) > 1:
            res.append(i.strip())
cres = Counter(res)
print(len(cres))
print(cres)
#画图
coloring = plt.imread('./haha.jpg')
#设置词云相关属性
my_wordcloud = WordCloud(background_color='white',
                        max_words=200,
                        mask=coloring,
                        max_font_size=150,
                        random_state=42,
                        font_path='‪C:\Windows\Fonts\simkai.ttf').fit_words(cres)
                        # font_path='‪C:\Windows\Fonts\simkai.ttf').generate_from_text(word_space_split)


image_colors = ImageColorGenerator(coloring)
# 保存图片
d = path.dirname(__file__)
my_wordcloud.recolor(color_func=image_colors)
my_wordcloud.to_file(path.join(d, user+".png"))
itchat.send_image(user+".png",toUserName='filehelper')
#显示词云
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()
print("over!")

