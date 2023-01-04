import re
from openpyxl import workbook

info_list = []

ip_list = []


with open("ip.txt", mode='r', encoding='utf-8') as fie:
    for i in fie:
        ip_list.append(i)

for ip in ip_list:
    ip = ip.strip()
    with open("placement_info.txt", mode="r", encoding='utf-8') as data:
        f = data.read()
        row = re.findall(".*{}\s.*".format(ip), f)
        # print(row, ip)
        if not row:
            info_list.append(
                "{ip}\t{enclosure}\t{NodeNumber}\t{Port}\t{DeliveryTime}\t{peer_to_peer_ip}".format(
                    ip=ip, enclosure="无信息", NodeNumber="无信息",
                    Port="无信息", DeliveryTime="无信息", peer_to_peer_ip="无信息")
            )
            continue
        row_l = row[0].split("\t")
        if not int(len(row_l)) > 5:
            row_l.append("null")

        # 获取对点机器的ip信息
        # i5机器的判断
        NodeNumber_tmp = []
        peer_to_peer_ip = ""
        if "机框" in row_l[1]:
            pass
        elif re.findall(".*i5.*|.*i9.*", row_l[0], re.IGNORECASE):
            # 生成对点节点信息
            for i in range(1, 6):
                NodeNumber_tmp.append("{}.{}".format(row_l[1].split(".", -1)[0], i))

            for node in NodeNumber_tmp:
                row_l_escape = row_l[0].replace("(", "\(")
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
            if re.findall(".*{}\t{}\.2\t.*".format(row_l_escape, row_l[1].split(".", -1)[0]), f):
                row_l_tmp = re.findall(".*{}\t{}\.2\t.*".format(row_l_escape, row_l[1].split(".", -1)[0]), f)[0].split(
                    "\t")
                peer_to_peer_ip += "{},".format(row_l_tmp[3])
            else:
                peer_to_peer_ip += "{}.2为空,".format(row_l[1].split(".", -1)[0])
        else:
            row_l_escape = row_l[0].replace("(", "\(")
            row_l_escape = row_l_escape.replace(")", "\)")
            if re.findall(".*{}\t{}\.1\t.*".format(row_l_escape, row_l[1].split(".", -1)[0]), f):
                row_l_tmp = re.findall(".*{}\t{}\.1\t.*".format(row_l_escape, row_l[1].split(".", -1)[0]), f)[0].split(
                    "\t")
                peer_to_peer_ip += "{},".format(row_l_tmp[3])
            else:
                peer_to_peer_ip += "{}.1为空,".format(row_l[1].split(".", -1)[0])

        # print(peer_to_peer_ip)

        # 区域 ip 故障信息 故障次数 机柜(row_l[0]) 节点号(row_l[1]) 端口 交付时间 对点ip
    info_list.append(
        "{ip}\t{enclosure}\t{NodeNumber}\t{Port}\t{DeliveryTime}\t{peer_to_peer_ip}".format(
            ip=ip, enclosure=row_l[0], NodeNumber=row_l[1], Port=row_l[2],
            DeliveryTime=row_l[4], peer_to_peer_ip=peer_to_peer_ip))

print(info_list)
wb = workbook.Workbook()
sheet = wb.worksheets[0]
info_list.insert(0, "ip\t故障次数\t机柜\t节点号\t端口\t交付时间\t对点ip")
row_x = 1
for item in info_list:
    row_y = 1
    for i in item.split("\t"):
        cell = sheet.cell(row_x, row_y)
        cell.value = i
        row_y += 1
    row_x += 1
wb.save("duidian.xlsx")
print("完成")