list1 = ["1", "3", "7"]
list2 = ["3", "1", "9"]
print(sorted(set(list1).intersection(set(list2)), key=lambda x:list1.index(x)))


print("{}\n".format("瑞云-{}".format("yyy").center(40, "#")))