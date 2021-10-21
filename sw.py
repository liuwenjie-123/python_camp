#!/usr/bin/python3

#H3c交换机

import time
import re,os
from netmiko import ConnectHandler

BASE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

now = time.strftime("%Y%m%d",time.localtime(time.time()))
log_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# ip_list = [
#     ['sw-001','10.139.0.36'],
# ]

SW = {
    'device_type':'hp_comware',
    'username':'yunpt',
    'ip' : '',
    'password':'yunptai.com'
}

ip_ile_path = os.path.join(BASE_DIR_PATH,"ip.txt")

with open(ip_ile_path) as f:
    for ips in f.readlines():
        ip = ips.strip()
        print(ip)
        SW['ip'] = ip
        connect = ConnectHandler(**SW)
        print(log_time + 'Successfully connected to ' + ip)
        with ConnectHandler(**SW) as conn:
            print("交换机：{}".format(ip))
            out = conn.send_command_timing("dis mac-add  | in Gi")
            for i in range(1, 41):
                mt = re.findall(".+GigabitEthernet1/0/{}\s".format(i), out)
                if mt:
                    mt1 = mt[0].split()
                    print("{}\t{}".format(mt1[-1],mt1[0]) )
                else:
                    print("GigabitEthernet1/0/{}".format(i), "")


