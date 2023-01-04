import json, urllib2
from urllib2 import Request, urlopen, URLError, HTTPError

# url and url header
# zabbix的api 地址，用户名，密码，这里修改为自己实际的参数
zabbix_url = "http://183.36.29.24:33080/api_jsonrpc.php"
zabbix_header = {"Content-Type": "application/json"}
zabbix_user = "lwj"
zabbix_pass = "liuwenjie"
auth_code = ""

# auth user and password
# 用户认证信息的部分，最终的目的是得到一个SESSIONID
# 这里是生成一个json格式的数据，用户名和密码
auth_data = json.dumps(
    {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params":
            {
                "user": zabbix_user,
                "password": zabbix_pass
            },
        "id": 0
    })

# create request object
request = urllib2.Request(zabbix_url, auth_data)

for key in zabbix_header:
    request.add_header(key, zabbix_header[key])

try:
    result = urllib2.urlopen(request)
# 对于出错新的处理
except HTTPError, e:
    print
    'The server couldn\'t fulfill the request, Error code: ', e.code
except URLError, e:
    print
    'We failed to reach a server.Reason: ', e.reason
else:
    response = json.loads(result.read())
    print
    response
    result.close()

# 判断SESSIONID是否在返回的数据中
if 'result' in response:
    auth_code = response['result']
else:
    print
    response['error']['data']

# request json
# 用得到的SESSIONID去通过验证，获取主机的信息（用http.get方法）
if len(auth_code) <> 0:
    host_list = []
    get_host_data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": "extend",
            },
            "auth": auth_code,
            "id": 1,
        })

    # create request object
    request = urllib2.Request(zabbix_url, get_host_data)
    for key in zabbix_header:
        request.add_header(key, zabbix_header[key])

    # get host list
    try:
        result = urllib2.urlopen(request)
    except URLError as e:
        if hasattr(e, 'reason'):
            print
            'We failed to reach a server.'
            print
            'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print
            'The server could not fulfill the request.'
            print
            'Error code: ', e.code
    else:
        response = json.loads(result.read())
        result.close()
        # 将所有的主机信息显示出来
        for r in response['result']:
            #    print r['hostid'],r['host']
            host_list.append(r['hostid'])
        # 显示主机的个数
        print
        "Number Of Hosts: ", len(host_list)



　　  # 返回所有hostid==10251的主机，并只查询name包含“CPU Usage”字段的item，并按照name排序
get_item_data = json.dumps({
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": "extend",
        "hostids": "10251"
                   "search": {
                                 # "key_": 'perf_counter[\Processor Information(_Total)\% Processor Time]'
                                 "name": "CPU Usage"
                             },
                             "sortfield": "name"
},
"auth": auth_code,
"id": 1
})

request = urllib2.Request(zabbix_url, get_item_data)
for key in zabbix_header:
    request.add_header(key, zabbix_header[key])
result = urllib2.urlopen(request)

try:
    result = urllib2.urlopen(request)
    response = json.loads(result.read())
    for r in response['result']:
        print
        r['itemid'], r['hostid']
    result.close()
except:
    pass

# 通过hostid获取相应的graphid
get_graph_data = json.dumps({
    "jsonrpc": "2.0",
    "method": "graphitem.get",
    "params": {
        "output": "extend",
        "expandData": 1,
        "itemids": "33712"
    },
    "auth": auth_code,
    "id": 1
})
request = urllib2.Request(zabbix_url, get_graph_data)
for key in zabbix_header:
    request.add_header(key, zabbix_header[key])
result = urllib2.urlopen(request)

try:
    result = urllib2.urlopen(request)
    response = json.loads(result.read())
    for r in response['result']:
        print
        r['itemid'], r['graphid']
    result.close()
except:
    pass
