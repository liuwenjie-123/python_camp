import random

user_list = ["alex","武沛齐","李路飞"]
color_card = ["黑桃", "红桃", "梅花", "方块" ]
total_poke_list = []
for num in range(1, 16):
    if num == 14:
        print(("小王", 14))
        total_poke_list.append(("小王", 14))
        continue
    if num == 15:
        print(("大王", 15))
        total_poke_list.append(("大王", 15))
        continue
    for card in color_card:
        print((card, num))
        total_poke_list.append((card, num))
print(total_poke_list)