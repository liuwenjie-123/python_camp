import os
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8001))

message = client.recv(1024)
print(message.decode("utf-8"))

while True:
    user = input("请输入用户名（退出请输入q/Q）")
    passwd = input("请输入密码（退出请输入q/Q）")
    if user.upper() == "Q" or passwd.upper() == "Q":
        client.sendall("{},{}".format(user, passwd).encode("utf-8"))
        break
    client.sendall("{},{}".format(user, passwd).encode("utf-8"))
    data = client.recv(1024)
    print(data.decode("utf-8"))

client.close()







