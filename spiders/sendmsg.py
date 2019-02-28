import itchat

itchat.auto_login(enableCmdQR=2,hotReload=True)

def send_onegroup(msg,gname):
    # rooms = itchat.get_chatrooms(update=True)
    rooms = itchat.search_chatrooms(gname)
    if rooms is not None:
        for i in range(1):
            username = rooms[0]['UserName']
            itchat.send(msg,toUserName=username)
            itchat.send_image("@e610ba4cf0b2902929e1c529b706c4f3b5936208972f98707442a88be01253d4.png",toUserName=username)
    else:
        print("None group found.")
if __name__ == "__main__":
    send_onegroup(u"Hello world,I am send by program sendmsg.py!","testmsg")
