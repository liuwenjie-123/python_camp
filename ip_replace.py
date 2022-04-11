import os
import re

BASEPATH = os.path.dirname(os.path.abspath(__file__))
IP_DICT = {}  # [{'10-117-89-33': '10.117.111.33'}]

class IpReplace():

    def __index__(self):
        pass

    def ip1(self, ip_file):
        with open(ip_file) as f:
            for line in f:
                ip_t_list = line.split()
                IP_DICT[ip_t_list[0]] = ip_t_list[1]
                # IP_DICT[str(ip_t_list[0]).replace(".", "-")] = ip_t_list[1]

    def log_fiel_replace(self, log_fiel, log_fiel_new):
        with open(log_fiel) as f_log:
            with open(log_fiel_new, mode="wt", encoding="utf-8") as f_new:
                for line in f_log:
                    if "CHANGED" in line:
                        line_list = str.split(line)
                        if not IP_DICT.get(line_list[0]):
                            continue
                        # f_new.write(line.replace(line_list[0], IP_DICT[line_list[0]]))
                        f_new.write("\n{}\n".format(IP_DICT[line_list[0]]))
                    else:
                        f_new.write(line)



ip1_file = os.path.join(BASEPATH, "ip_file.txt")
log_file = os.path.join(BASEPATH, "log_file.txt")
log_file_new = os.path.join(BASEPATH, "log_file_new.txt")

v1 = IpReplace()
v1.ip1(ip1_file)
v1.log_fiel_replace(log_file, log_file_new)
