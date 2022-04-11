import os
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(5)

conn, addr = sock.accept()
conn.sendall("欢迎使用xx系统信息".encode('utf-8'))

while True:
    data = conn.recv(1024).decode("utf-8")
    with open("key.txt", mode="r") as f:
        data1 = str(f.readline())
        if data == data1:
            print("验证成功-{}-{}".format(type(data),type(data1)))
        s_user, s_passwd = data1.split(",")
        d_user, d_passwd = data.split(",")
        if s_user == d_user and s_passwd == d_passwd:
            conn.sendall("登录成功".encode("utf-8"))
        elif str(d_user).upper()  == "Q" or str(d_passwd).upper() == "Q":
            break
        else:
            conn.sendall("登录失败，账密错误".encode("utf-8"))

conn.close()
sock.close()







