import jieba
import itchat
import re
import jieba
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
import PIL.Image as Image
import time
from os import path
import os
from scipy.misc import imread
a = """
Do one thing today and tomorrow.smile.....你好有事
没事常联系阴晴圆缺在窗外，心中自有一片艳阳天我相信我，瘦不下来
了！20岁那年买到了10岁时买不起的玩具，可却没了意义！。。。。。，
小影，加油！赵佳慧妈妈In the promise of another tomorrow这个人很懒稳稳的走每一步。。。。选择我你是对的瘦！瘦！瘦！人不开心的原因就是把自己关在一个跑不掉的地方Gemfield, A CivilNet Maintainer。这是个性签名不个性不签名平静不等于平凡，努力只为更好人生！仅此一生，当竭尽全力…万物并作  吾以观复
镜公众号-序员已经发生的，就是唯一会发生的。
我的世界我做主让信念坚持下去，梦想就会实现梦想还是要有的，万一要实现了呢土豆丝炒饼加蛋…寻觅心灵的富足Do something非洲政府官方认证究极难民13230604770It is not real but it is really there.你所
经历的，都是小事有孩童，有瓜果，
有小犬，有蝴蝶，足以撑起一个盛夏。淡泊人生爸妈的健康快乐是我最大的幸福！留余保持单纯
而又睿智的内心生活不仅仅是苟且。认准后就去做因为有双下巴，所以不太好低头～成长，听说是将哭声调成静音的过程对信任得人
永远别撒谎，对撒谎得人永远别信任！不卑不亢自律即自由。有想做的事兒，有值得愛的人，有美麗的夢。悲情城市当你足够优秀时
，生活自然会赋予你嘴角上扬的自信。想拥有一座属于自己的图书馆，做一个简简单单的书呆子。每一天我都会热泪盈眶，仰望星空,脚踏实地。向光生长一个人的温柔我就是我，谁都替代不了。生活节奏做一个乐观的人！努力奋斗人生不是一场物质的盛宴，而是一
次灵魂的修炼！无需言，做自己时刻怀有感恩之心讲文明，树新风，公益广告我的新号15101040761，看见的亲们都更新一下！谢谢大家。有你才幸福！！！电闪雷鸣，处变不惊振兴中国严肃文学！你需要尽你所能，最大限度地去努力。只要你这么做，只要你能保持
好的东西要一起分享不忘初心 方得始终觅一种力量来支撑未来终与始总归平淡，可喜一路的余欢无欲无求这个世界很小，我们就这样遇见，这个世界很大，分开就很难再见!不念过去，不畏将来！生而为人 请务必善良◢ ◤人生在勤，不索何获。嗯～追风的少年哈喽
～您好～朋友不断学习，无所畏惧向日葵 " "无所谓为什么要让稍纵即逝的快感败坏你的荣耀，你的天赋和你的生命？你一直是一个
人走路，昨天，今天，明天
没有期待就没有伤害。……都是虚假的，只是不在乎后的谎言罢了记录每一天。。。心想，事成ʚتɞ风华人之所以能，是相信能。那
些年的时光毫端蕴秀临霜写，口齿噙香对月吟如果快乐太难，那我祝你平安。N+O！一个不善解人意，随意爆炸的姑娘。2
"""
_re_digist = re.compile('\d')
_re_alpha = re.compile('[a-zA-Z]')
_re_chinese = re.compile(u'[\u4e00-\u9fa5]')
oprwords = a.split()
res = []
print("22222222222222222222222222222222")
for j in oprwords:
    tmp = ''
    for i in j:
        if _re_digist.search(i) or _re_alpha.search(i) or _re_chinese.search(i):
            tmp += i
        else:
            tmp += ''
    res.append(tmp)
a = ' '.join(res)
wordlist = jieba.cut(a,cut_all=True)
word_space_split = " ".join(wordlist).split(" ")
res = []
for i in word_space_split:
    if not i:
        continue
    else:
        if _re_digist.search(i) or _re_alpha.search(i) or _re_chinese.search(i):
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

# def getutf8str(oprwords):
