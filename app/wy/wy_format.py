"""
{
    "pchbtjry_b"：[]
    "pchdjhry":[]
    "pchnfsry":[]
    "pcxncdry":[]
    "pchnry":[]
    "pchdjhry_c":[]
    "pchbtjry":[{
            "ip": "10.139.20.9",
            "event": [
                {
                    "msg": "code-version-error",
                    "operator": "lhq_script",
                    "time": "2022-03-14 18:57:46"
                },
                {
                    "msg": "code-version-error",
                    "operator": "lhq_script",
                    "time": "2022-03-17 14:48:07"
                }
            ]
        }]
}

code-version-error 客户手动关机 不记录到故障次数
ip 故障类型 故障次数 机柜	节点号	端口	IP地址	备注1

"""
import re
from toolz import compose
from openpyxl import workbook


def file_read():
    with open("info.txt", mode="rt", encoding='utf-8') as f:
        san_dic = ""
        for i in f:
            san_dic += i
        return eval(san_dic)




def fmt(dic):
    info_list = []
    for area in dic:  # area = pchnfsry
        for details in dic[area]:
            """
            details = {'ip': '10.131.84.26',
                'event': [{'msg': 'network-error', 'operator': 'lhq_script', 'time': '2022-03-13 16:35:48'},
                    {'msg': 'network-error', 'operator': 'lhq_script', 'time': '2022-03-14 04:37:24'}
                    ]}
            """
            ip = details["ip"]
            print(ip)
            event = details["event"]  # [{'msg': 'network-error', 'operator': 'lhq_script', 'time': '2022-03-13 16:35:48'},]
            event_num = len(event)
            if not event:
                msg = "空信息"
            else:
                msg = event[-1]["msg"]

            with open("placement_info.txt", mode="r", encoding='utf-8') as data:
                f = data.read()
                row = re.findall(".*{}\t.*".format(ip), f)
                print(row, ip)
                if not row:
                    info_list.append(
                        "{area}\t{ip}\t{msg}\t{event_num}\t{enclosure}\t{NodeNumber}\t{Port}\t{DeliveryTime}\t{peer_to_peer_ip}".format(
                            area=area, ip=ip, msg=msg, event_num=event_num, enclosure="无信息", NodeNumber="无信息",
                            Port="无信息", DeliveryTime="无信息", peer_to_peer_ip="无信息")
                    )
                    continue
                row_l = row[0].split("\t")
                if not int(len(row_l))  > 5:
                    row_l.append("null")

                # 获取对点机器的ip信息
                # i5机器的判断
                NodeNumber_tmp = []
                peer_to_peer_ip = ""
                if "机框" in row_l[1]:
                    pass
                elif re.findall(".*i5.*|.*i9.*" ,row_l[0], re.IGNORECASE):
                    # 生成对点节点信息
                    for i in range(1,6):
                        NodeNumber_tmp.append("{}.{}".format(row_l[1].split(".", -1)[0], i))

                    for node in NodeNumber_tmp:
                        row_l_escape = row_l[0].replace("(","\(")
                        row_l_escape = row_l_escape.replace(")", "\)")
                        # print(re.findall(".*{}\t{}.*".format(row_l_escape, node), f),ip)
                        if re.findall(".*{}\t{}\t.*".format(row_l_escape, node), f):
                            row_l_tmp = re.findall(".*{}\t{}\t.*".format(row_l_escape, node), f)[0].split("\t")
                        # print("row=={}".format(row_l_tmp),type(row_l_tmp))
                            peer_to_peer_ip += "{},".format(row_l_tmp[3])
                        else:
                            peer_to_peer_ip += "{}为空,".format(node)

                elif row_l[1].split(".", -1)[-1] == "1":
                    row_l_escape = row_l[0].replace("(", "\(")
                    row_l_escape = row_l_escape.replace(")", "\)")
                    if re.findall(".*{}\t{}\.2\t.*".format(row_l_escape, row_l[1].split(".", -1)[0] ), f):
                        row_l_tmp = re.findall(".*{}\t{}\.2\t.*".format(row_l_escape, row_l[1].split(".", -1)[0] ), f)[0].split("\t")
                        peer_to_peer_ip += "{},".format(row_l_tmp[3])
                    else:
                        peer_to_peer_ip += "{}.2为空,".format(row_l[1].split(".", -1)[0])
                else:
                    row_l_escape = row_l[0].replace("(", "\(")
                    row_l_escape = row_l_escape.replace(")", "\)")
                    if re.findall(".*{}\t{}\.1\t.*".format(row_l_escape, row_l[1].split(".", -1)[0] ), f):
                        row_l_tmp = re.findall(".*{}\t{}\.1\t.*".format(row_l_escape, row_l[1].split(".", -1)[0] ), f)[0].split("\t")
                        peer_to_peer_ip += "{},".format(row_l_tmp[3])
                    else:
                        peer_to_peer_ip += "{}.1为空,".format(row_l[1].split(".", -1)[0])

                # print(peer_to_peer_ip)


            #区域 ip 故障信息 故障次数 机柜(row_l[0]) 节点号(row_l[1]) 端口 交付时间 对点ip
            info_list.append("{area}\t{ip}\t{msg}\t{event_num}\t{enclosure}\t{NodeNumber}\t{Port}\t{DeliveryTime}\t{peer_to_peer_ip}".format(area=area,ip=ip,msg=msg,event_num=event_num,enclosure=row_l[0],NodeNumber=row_l[1],Port=row_l[2],DeliveryTime=row_l[4],peer_to_peer_ip=peer_to_peer_ip))
    return info_list





if __name__ == '__main__':
    dic = file_read()
    print(dic)
    info_list = fmt(dic)
    res = sorted(info_list, key=compose(lambda x: (x[0],x[4]), lambda x: x.split("\t")))
    # info_list.sort(key = lambda  i:(re.match("^.*\t", ".*\t.*\t.*\t.*\t(\()")))
    wb = workbook.Workbook()
    sheet = wb.worksheets[0]
    row_x = 1
    res.insert(0, "区域\tip\t故障信息\t故障次数\t机柜\t节点号\t端口\t交付时间\t对点ip")
    for item in res:
        row_y = 1
        for i in item.split("\t"):
            cell = sheet.cell(row_x, row_y)
            cell.value = i
            row_y += 1
        row_x += 1
    wb.save("data.xlsx")
    print("完成")



