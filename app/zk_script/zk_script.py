import os, time
from multiping import MultiPing


# 读取ip.txt，返回IP列表
def read_ip(ip_path):
    ip_list = []
    ipmi_ip = {}
    with open(ip_path, mode="r", encoding="utf-8") as f:
        for i in f:
            if i.strip():
                ip_ipmi_list = i.split("-")
                ip_list.append(ip_ipmi_list[0].strip())
                ipmi_ip[ip_ipmi_list[0].strip()] = ip_ipmi_list[1].strip()
    return ip_list, ipmi_ip


# ping检测
def ping_check(ip_list):
    mp = MultiPing(ip_list)
    mp.send()
    responses, no_responses = mp.receive(1)
    # responses, no_responses = multi_ping(ip_list, timeout=3, retry=2)
    # print(no_responses)
    return no_responses


# 取交集
def intersection(list1, list2):
    ret = [val for val in list1 if val in list2]
    return ret


#cmd
def syscmd(CMD):
    result = os.popen(CMD).read().strip()
    return result


# 重启机器
def reboot(reb_ip_list, ip_dict):
    cmd_list = ["ipmitool -H {} -I lan -U admin -P admin sel clear",
                "ipmitool -H {} -U admin -P admin chassis bootdev pxe",
                "ipmitool -H {} -I lan -U admin -P admin power cycle",
                "ipmitool -H {} -I lan -U admin -P admin power on",
                ]
    for i in reb_ip_list:
        reb_ipmi_ip = ip_dict[i]
        with open(logs, mode="at", encoding="utf-8") as log_f:
            log_f.write(",".join(reb_ip_list))
        for cmd in cmd_list:
            with open(logs, mode="at", encoding="utf-8") as log_f:
                # 写日志到文件
                log_f.write("{}  {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), cmd.format(reb_ipmi_ip)))
                ret = syscmd(cmd.format(reb_ipmi_ip))
                # 返回结果写入日志
                log_f.write("{}  {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ret))
                print(cmd.format(reb_ipmi_ip))
                time.sleep(1)
            # syscmd("D:\ipmitool\ipmitool -H {} -U admin -P admin lan print".format("10.42.131.21"))


if __name__ == '__main__':
    count = 1
    while True:
        print("{} 第{}轮 开始检测".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), count))
        logs = os.path.join("logs", "{}.txt".format(time.strftime("%Y-%m", time.localtime())))
        ip_list, ipmi_ip = read_ip("ip.txt")
        no_ping1 = ping_check(ip_list)
        print("{} 第{}轮 已完成第一次检测，休眠120s，然后进行第二次检测".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  count))
        time.sleep(10)
        no_ping2 = ping_check(ip_list)
        # 取交集
        no_ping = intersection(no_ping1, no_ping2)
        if int(len(no_ping)) > 60:
            with open(logs, mode="at", encoding="utf-8") as log_f:
                log_f.write("{} 超过60路不通，不进行重启操作，ip为：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ",".join(no_ping)))
            print("{} 第{}轮 超过60路不通，不进行重启操作，ip为：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  count,",".join(no_ping)))
        elif not int(len(no_ping)):
            print("{} 第{}轮 机器均为在线状态，不进行重启".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  count))
        else:
            # 重启对应机器
            print("{} 第{}轮 正在重启机器，ip为{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  count, ",".join(no_ping)))
            reboot(no_ping, ipmi_ip)
        # 列表清空
        no_ping1.clear()
        no_ping2.clear()
        print("{} 睡眠3600s后进行下次检测".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        time.sleep(3600)
        count += 1
