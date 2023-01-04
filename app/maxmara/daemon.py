# -*- coding: utf-8 -*-
import psutil
import os
# import logging
import time


BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# logger = logging.getLogger()
# fh = logging.FileHandler(r'{}\monitor.log'.format(BASE_PATH), encoding='utf-8', mode='a')
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# fh.setFormatter(formatter)
# logger.addHandler(fh)
# logger.setLevel(logging.DEBUG)


# 监控windows系统所有进程服务任务。定时任务执行，发现servername进程名在系统中不存在，执行启动程序


class MonitorServer:

    def __init__(self):
        self.pidNotHandle = []
        self.process_name = []
        self.servername = "php-cgi.exe"

    def now_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    def execute(self):
        self.pidNotHandle = list(psutil.process_iter())
        for each in self.pidNotHandle:
            self.process_name.append(each.name())

        # 是否存在进程名，存在就return
        if self.servername in self.process_name:
            print("{}  {} 进程存在".format(self.now_time(), self.servername))
            return 0

        # 进程不存在，重新启动程序
        cmd = r"C:\Nginx_HRD\Start.bat"
        os.popen(cmd)
        print("{}  重启程序.............".format(self.now_time()))
        return 0


if __name__ == '__main__':
    while True:
        MonitorServer().execute()
        time.sleep(10)