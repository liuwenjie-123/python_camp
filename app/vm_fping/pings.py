from scapy.all import *
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor


def packet_create(s):##构造ICMP报文
    pk = IP(
        dst=s
    )/ICMP(
        type=8
    )/data
    return pk

def packet_send(s,down_list):##发送ICMP报文
    ans = sr1(packet_create(s),timeout=6)
    if ans == None:
        down_list.append(s)


if __name__ == "__main__":
    file_path = "test.txt"##需要扫描的存放IP地址的文件路径
    data = "A"*32

    with open(file_path,"r") as f:
        server_IP = f.readlines()

    pool = ProcessPoolExecutor(max_workers=60)

    manager = Manager()
    down_list = manager.list()

    for s in server_IP:
        s = s.replace("\n","")
        pool.submit(packet_send,s,down_list)
    pool.shutdown()

    print(down_list)
    with open("NoresponseIP.txt",'w') as f:##保存没有回应的IP
        for i in down_list:
            f.write(i+'\n')