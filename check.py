import os
import configparser
from multiping import MultiPing
import re
import time

import requests
import json
import prettytable as pt


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IP_LIST_PATH = os.path.join(BASE_PATH, "ip_list")
DATA_PATH = os.path.join(BASE_PATH, "data")


def get_ip_list(ip_list_path):
    # {"电讯云"=[{"jh"=["xxx","xx1"]}, ],  }
    ip_dict = {}

    for i in os.listdir(ip_list_path):
        """
        遍历目录下的文件
        """
        project_name = str(re.findall("(.*)\.", i)[0])
        # print(project_name)
        ip_dict[project_name] = []
        ip_file_path = os.path.join(IP_LIST_PATH, i)
        #把文件里的区域写入到字典
        config = configparser.ConfigParser()
        config.read(ip_file_path, encoding='utf-8')
        count = 0
        for items in config.sections():
            #把项目名和区域写到字典
            ip_dict[project_name].append({items:[]})
            # print(ip_dict)
            # print(count)
            for key in config.items(items):
                #遍历IP，写入到字典
                # print(key)
                ip_dict[project_name][count][items].append(key[0])
            count += 1
    return ip_dict


def get_down_ip(ip_list_dict):
    for project_name, pronject_area_list in ip_list_dict.items():
        # print(project_name, pronject_area_list)
    # key是项目名称
        count = 0
        for area_dict in pronject_area_list:
            for area_dict_key, area_dict_value in area_dict.items():
                ip_list = area_dict_value
                mp = MultiPing(ip_list)
                mp.send()
                responses, no_responses = mp.receive(1)
                # print(no_responses)
                no_responses.append(len(area_dict_value))
                #把不通的IP替换原来的列表里的IP
                ip_list_dict[project_name][count][area_dict_key] = no_responses
            count += 1
    return ip_list_dict


def sed_info_tab(ip_list_dict):
    for project_name, pronject_area_list in ip_list_dict.items():
        # print(project_name, pronject_area_list)
        pronject_info = []
        for area_dict in pronject_area_list:
            for area_dict_key, area_dict_value in area_dict.items():
                pronject_info.append([area_dict_key, str(len(area_dict_value) - 1), str(area_dict_value[-1]), round((len(area_dict_value) - 1)/area_dict_value[-1], 3) ])
        #把数据转换成表格
        tb = pt.PrettyTable()
        tb.field_names = ["区域", "离线数", "总数", "离线率"]
        for i in pronject_info: tb.add_row(i)
        ding = DingTalk_Disaster()
        # ding.send_msg("瑞云-{}\n{}".format(project_name, tb))


def intersection(ip_list_dict_1, ip_list_dict_2):
    #1为最新的故障IP， 2为上次筛选出来的故障IP
    for project_name, pronject_area_list in ip_list_dict_1.items():
        # print(project_name, pronject_area_list)
        count = 0
        for area_dict in pronject_area_list:
            for area_dict_key, area_dict_value in area_dict.items():
                #使用sorted排序，防止取交集后顺序混乱
                j_set = sorted(list(set(area_dict_value).intersection(set(ip_list_dict_2[project_name][count][area_dict_key]))), key=lambda x:area_dict_value.index(x))
                ip_list_dict_2[project_name][count][area_dict_key] = j_set
            count += 1
    return ip_list_dict_2


def output_offline_info(ip_list_dict):
    for project_name, pronject_area_list in ip_list_dict.items():
        # print(project_name, pronject_area_list)
        print(project_name.center(40, "#"))
        for area_dict in pronject_area_list:
            for area_dict_key, area_dict_value in area_dict.items():
                prondect_data_path = os.path.join(DATA_PATH, "{}{}".format(project_name, ".txt"))
                with open(prondect_data_path, mode="r", encoding='utf-8') as data:
                    f = data.read()
                    print(str(area_dict_key).center(20, "="))
                    if len(area_dict_value) <= 1:
                        continue
                    for i in range(0, len(area_dict_value)-1):
                        mc = re.findall(".*{}\s".format(area_dict_value[i]), f)
                        print("{}\t{}\t{}".format(mc[0].split()[0], mc[0].split()[1], mc[0].split()[2]))
                        # print(mc[0].split()[0], "\t", mc[0].split()[1], "\t", mc[0].split()[2])
        print("".center(40, "#"))
        print()



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
    ip_down_dict = {}
    ip_down_dict_2 = {}
    for i in range(1, 6):
        ip_dict = get_ip_list(IP_LIST_PATH)
        ip_down_dict_1 = get_down_ip(ip_dict)
        if i == 1:
            print(i)
            ip_down_dict_2 = ip_down_dict_1
            continue
        ip_down_dict = intersection(ip_down_dict_1, ip_down_dict_2)
        time.sleep(50)
    # sed_info_tab(ip_down_dict)
    print(ip_down_dict)
    output_offline_info(ip_down_dict)