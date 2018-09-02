from wxpy import *
import PIL.Image as Image
#初始化机器人，扫码登录
bot = Bot()

#获取好友
my_fridends = bot.friends()
print(my_fridends)
#获取聊天对象
my_chats = bot.chats()
print(my_chats)
#群聊
my_groups = bot.groups()
print(my_groups)
#公众号
my_mps = bot.mps()
print(my_mps)
#friends(),具有sex(性别)，province(省份),city(城市),signature(个性签名)
sex_dict = {'male': 0, 'female': 0}
for friend in my_fridends:
    #统计性别
    if friend.sex == 1:
        sex_dict['male'] += 1
    else:
        sex_dict['female'] += 1
print("性别统计为：")
print(sex_dict)
img = Image.open("用户访问数据.png", mode="rw")
#显示图像内容
img.show()