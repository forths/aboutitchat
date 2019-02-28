# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
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

itchat.auto_login()

friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]

siglist = []

for i in friends:
    signature = i['Signature'].strip().replace('span','').replace('class','').replace('emoji','')
    rep = re.compile('1f\d+\w*|[<>/=]')
    signature = rep.sub(' ',signature)
    signature = getnum_alpha_china_words(signature)
    siglist.append(signature)

text = ' '.join(siglist)

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
coloring = plt.imread('./haha.jpg')

my_wordcloud = WordCloud(background_color='white',
                        max_words=200,
                        mask=coloring,
                        max_font_size=150,
                        random_state=42,
                        font_path='‪C:\Windows\Fonts\simkai.ttf').fit_words(cres)

image_colors = ImageColorGenerator(coloring)

d = path.dirname(__file__)
my_wordcloud.recolor(color_func=image_colors)
my_wordcloud.to_file(path.join(d, user+".png"))
itchat.send_image(user+".png",toUserName='filehelper')

plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()
print("over!")

