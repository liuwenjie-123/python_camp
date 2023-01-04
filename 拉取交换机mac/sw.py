#!/usr/bin/python3

#H3c交换机

import time
import re,os
from netmiko import ConnectHandler

BASE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

now = time.strftime("%Y%m%d",time.localtime(time.time()))
log_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# ip_list = [
#     ['sw-001','10.149.0.1'],
# ]

SW = {
    'device_type':'hp_comware',
    'username':'admin',
    'ip' : '',
    'password':'Rayvision@2017'
}

ip_ile_path = os.path.join(BASE_DIR_PATH,"深圳未导入ip.txt")

with open(ip_ile_path) as f:
    for ips in f.readlines():
        ip = ips.strip()
        print(ip)
        SW['ip'] = ip
        connect = ConnectHandler(**SW)
        print(log_time + 'Successfully connected to ' + ip)
        with ConnectHandler(**SW) as conn:
            sw_name = conn.send_command_timing("display sysname")
            print("交换机：{}-{}".format(sw_name,ip))
            #取消分屏
            conn.send_command_timing("screen-length 0 temporary")
            #out = conn.send_command_timing("dis mac-add  | in Gi")
            out = conn.send_command_timing("dis mac-add  | in GE")
            for i in range(1, 49):
                #mt = re.findall(".+GigabitEthernet1/0/{}\s".format(i), out)
                mt = re.findall(".+GE1/0/{}\s".format(i), out)
                if mt:
                    mt1 = mt[0].split()
                    print("{}\t{}".format(mt1[-1],mt1[0]) )
                else:
                    print("GE1/0/{}".format(i), "")


