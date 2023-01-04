import requests, json, datetime

# 跟据id删除munu的数据
def del_munu(munu_ip, id_list):
    vm_list = []
    # 分页取值
    for munu_id in id_list:
        # print(pageindex)
        url = "http://{ip}:9915/sys/node_remove?id={id}&operator=yanrk"
        try:
            url = url.format(ip=munu_ip, id=munu_id)
        except Exception as e:
            return "{}连接失败".format()
        ret = requests.get(url).text
        data = json.loads(ret)
        print("删除{}".format(munu_id))

if __name__ == '__main__':
    ip_list = []
    id_list = []
    munu_ip = "10.116.116.9"
    with open("ip.txt", mode="r", encoding='utf-8') as f:
        for ip in f:
            print(ip)
            if not ip.strip():
                continue
            i_list = ip.strip().split(".")
            id = (int(i_list[0]) * 256 * 256 * 256 + int(i_list[1]) * 256 * 256 + int(i_list[2]) * 256 + int(i_list[3])) * 256 * 256
            id_list.append(id)
    print(id_list,munu_ip)
    del_munu(munu_ip, id_list)

