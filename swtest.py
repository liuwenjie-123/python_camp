
import re

mse = """
2009-2468-0248 131      Learned        GigabitEthernet1/0/11    AGING
2012-3768-0c10 131      Learned        GigabitEthernet1/0/7     AGING
2012-3768-0c24 131      Learned        GigabitEthernet1/0/2     AGING
2a02-4c37-0d64 131      Learned        GigabitEthernet1/0/12    AGING
2a03-a020-07ca 131      Learned        GigabitEthernet1/0/5     AGING
2a03-a043-07a7 131      Learned        GigabitEthernet1/0/1     AGING
2a04-4c15-0232 131      Learned        GigabitEthernet1/0/3     AGING
2a04-a015-01f6 131      Learned        GigabitEthernet1/0/8     AGING
2a05-a045-009a 131      Learned        GigabitEthernet1/0/10    AGING
2a05-a045-009b 131      Learned        GigabitEthernet1/0/9     AGING
2a15-6f04-0df2 131      Learned        GigabitEthernet1/0/14    AGING
2a20-6f03-0f7e 131      Learned        GigabitEthernet1/0/13    AGING
2a20-6f03-0fc6 131      Learned        GigabitEthernet1/0/4     AGING
2a24-6f02-1474 131      Learned        GigabitEthernet1/0/6     AGING
"""


for i in range(1,41):
    mt = re.findall(".+GigabitEthernet1/0/{}\s".format(i), mse)
    if mt:
        mt1 = mt[0].split()
        print(mt1[-1],mt1[0])
    else:
        print("GigabitEthernet1/0/{}".format(i),"")

