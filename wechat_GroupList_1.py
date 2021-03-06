import itchat, time, openpyxl
from openpyxl.utils import column_index_from_string, get_column_letter
from itchat.content import TEXT
#name = ' '
roomslist = []

itchat.auto_login(enableCmdQR = False)

def getroom_message(n):
    #获取群的username，对群成员进行分析需要用到
    itchat.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
    RoomList =  itchat.search_chatrooms(name=n)
    if RoomList is None:
        # print("%s group is not found!" % (name))
        pass
    else:
        return RoomList[0]['UserName']

def getchatrooms():
    #获取群聊列表
    roomslist = itchat.get_chatrooms()
    #print(roomslist)
    return roomslist



for i in getchatrooms():
    #print(i['NickName'])
    roomslist.append(i['NickName'])
print(roomslist)

wb = openpyxl.load_workbook('StudentList.xlsx')
sht = wb['wechat']
row = 1
ChatRoom = itchat.update_chatroom(getroom_message('庆典联络组'), detailedMember=True)
for i in ChatRoom['MemberList']:
    sht['A' + str(row)] = i['NickName']
    sht['B' + str(row)] = i['DisplayName']
    sht['C' + str(row)].value = "=RIGHT(B%d,11)" % row
    row += 1
wb.save(filename='StudentList.xlsx')



# with open('22.txt', 'a', encoding='utf-8')as f:
#     ChatRoom = itchat.update_chatroom(getroom_message('庆典联络组'), detailedMember=True)
#     for i in ChatRoom['MemberList']:
#         #print (i['Province']+":",i['NickName'])
#         f.write(i['NickName'] + ":" + i['DisplayName']+'\n')
#         # print('正在写入           '+i['Province']+":",i['NickName'])
# f.close()
