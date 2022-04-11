class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []

    def login(self, name, pwd):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        for i in self.user_list:
            if i.name == name and i.pwd == pwd:
                print("验证成功")
                break
            print("验证失败")

    def register(self, name, pwd):
        """
        用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        self.user_list.append(User(name, pwd))

    def run(self):
        """
        主程序
        :return:
        """
        while True:
            print("开始用户注册，跳过请输入（Q/q）")
            name = input("用户名：")
            pwd = input("密码：")
            if name.strip().upper() == "Q":
                break
            self.register(name, pwd)

        while True:
            print("开始登录验证。退出请输入(Q\q)")
            name = input("用户名：")
            pwd = input("密码：")
            if name.strip().upper() == "Q":
                break
            self.login(name, pwd)

if __name__ == '__main__':
    obj = Account()
    obj.run()