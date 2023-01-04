import requests, json, datetime

# 拉取munu数据
def get_munu(munu_ip):
    vm_list = []
    # 分页取值
    for pageindex in range(200):
        # print(pageindex)
        url = "http://{ip}:9915/sys/node_list&percentpagesize=100&pageindex={pageindex}&operator=yanrk"
        try:
            url = url.format(ip=munu_ip, pageindex=pageindex)
        except Exception as e:
            return "{}连接失败".format()
        print(url)
        ret = requests.get(url).text
        data = json.loads(ret)
        if not data["node"]:
            break
        for node in data["node"]:
            vm_ip = node["ip"]
            vm_status = node["status"]
            # if vm_status == "Offline":
            #     vm_list.append(vm_ip)
            vm_list.append(vm_ip)
    return vm_list


if __name__ == '__main__':
    ret = get_munu("10.116.116.9")
    with open("ip.txt", mode="a", encoding='utf-8') as f:
        for i in ret:
            f.write("{}\n".format(i))


