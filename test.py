import os
import configparser
from multiping import MultiPing
import re

import requests
import json
import prettytable as pt


config = configparser.ConfigParser()
config.read('my.ini', encoding='utf-8')

result = config.sections()
print(result)

ip_dict = {}
items = result
for key in items:
    ip_dict[key]= []
    result = config.items(key)
    for i,x in result:
        if re.match("10", i ):
            ip_dict[key].append(i)

print(ip_dict)


info_dick = {}
#{'tj': [1, 32, 0.031], 'jh': [1, 32, 0.031], 'gy': [0, 26, 0.0], 'xy': [1, 34, 0.029]}
#检测离线机器，形成数据，保存到info_dict
for i in ip_dict:
    mp = MultiPing(ip_dict[i])
    mp.send()
    responses, no_responses = mp.receive(1)
    # print("{}区域离线机器".format(i,))
    info_dick[i] = [len(no_responses),len(ip_dict[i]),round(len(no_responses)/len(ip_dict[i]), 3)]

    #机器列表，用于查找机柜信息

    with open("data.txt", mode="r",encoding='utf-8') as data:
        f = data.read()
        for i in no_responses:
            mc = re.findall(".*{}.*".format(i), f)
            print( mc[0].split()[0],"\t", mc[0].split()[1], "\t",mc[0].split()[2])

# print(info_dick)
#输出离线信息
info = []
# info.append(["区域", "离线数","总数", "离线率"])
# info.append("{}{}{}{}".format("区域".ljust(10), "离线数".ljust(10), "总数".ljust(10), "离线率".ljust(10)))
for key,val in info_dick.items():

    info.append([key, str(val[0]), str(val[1]), str(val[2]) ])
    # info.append("{}{}{}{}".format(str(key).ljust(10),str(val[0]).ljust(10),str(val[1]).ljust(10),str(val[2]).ljust(10)))
    # print(str(key).ljust(10),str(val[0]).ljust(10),str(val[1]).ljust(10),str(val[2]).ljust(10))
print(info)

#字符串格式化
tb = pt.PrettyTable()
tb.field_names = ["区域", "离线数", "总数", "离线率"]
for i in info: tb.add_row(i)

print(tb)


"""# 获取一维列表中字符串法的最大长度
def maxlen(tableData):
    num = 0
    for i in range(len(tableData)):
        if num < len(tableData[i]):
            num = len(tableData[i])

    # 返回列表中最长的字符串的长度
    return num

# 二位列表将列表以行格式化打印
#       apples     oranges    cherries      banana
#        Alice         Bob       Carol       David
#         dogs        cats       moose       goose
def printRowTable(tableData,flag):

    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidths[i] = maxlen(tableData[i])
    num = max(colWidths)

    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if flag == 'left' :
                print(tableData[i][j].ljust(num + 4), end="")
            elif flag == 'right':
                print(tableData[i][j].rjust(num + 4), end="")
            else:
                print(tableData[i][j].center(num + 4), end="")
        print()

# 二位列表将列表以列格式化打印
#     apples    Alice      dog
#    oranges      Bob     cats
#   cherries    Carol    moose
#     banana    David    goose
def printColumnTable(tableData,flag):

    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidths[i] = maxlen(tableData[i])
    num = max(colWidths)

    for j in range(len(tableData[0])):
        for i in range(len(tableData)):
            if flag == 'left' :
                print(tableData[i][j].ljust(num + 4), end="")
            elif flag == 'right':
                print(tableData[i][j].rjust(num + 4), end="")
            else:
                print(tableData[i][j].center(num + 4), end="")
        print()"""
#printRowTable(info,'right')
# print("\n".join(info))

#发送钉钉信息
class DingTalk_Base:
    def __init__(self):
        self.__headers = {'Content-Type': 'application/json;charset=utf-8'}
        self.url = ''
    def send_msg(self,text):
        json_text = {
            "msgtype": "text",
            "text": {
                "content": text
            },
            "at": {
                "atMobiles": [
                    ""
                ],
                "isAtAll": False
            }
        }
        return requests.post(self.url, json.dumps(json_text), headers=self.__headers).content
class DingTalk_Disaster(DingTalk_Base):
    def __init__(self):
        super().__init__()
        # 填写机器人的url
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=8240c507ed559969a035ff87bd9ca7c0e6f9cee3857a5e8e5be9a305f09dfe65'
if __name__ == '__main__':
    ding = DingTalk_Disaster()
    # print("{}{}".format("瑞云\n","\n".join(info)))
    # ding.send_msg("{}{}".format("瑞云\n", tb))