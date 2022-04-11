"""
1、读取本地目录下的ip.txt文件
2、把ip装换成ip和主机名
 - 例10.132.80.49 (10 * 256 * 256 * 256 + 132 * 256 * 256 + 80 * 256 + 49) * 256 * 256
 -  SZ80-049
 num.zfill(2)

"""
import os


def import_munu():
    with open("ip.txt", mode="rt", encoding="utf-8") as f:
        for line in f:
            line_list = line.split(".")
            id = (int(line_list[0]) * 256 * 256 * 256 + int(line_list[1]) * 256 * 256 + int(line_list[2]) * 256 + int(
                line_list[3])) * 256 * 256
            host_name = "{}{}{}".format("{:03d}".format(int(line_list[1].strip())), "{:03d}".format(int(line_list[2].strip())), "{:03d}".format(int(line_list[3].strip())))
            print(line, id, host_name)

            xml_file = open(r"xml\{}.xml".format(id), mode="w", encoding="utf-8")
            xml_file.write("""<nodeitem>
<id>{}</id>
<listen>0</listen>
<ip>{}</ip>
<port>10000</port>
<aidport>10001</aidport>
<name>{}</name>
<description>{}</description>
<memory>32131</memory>
<numofcore>12</numofcore>
<pausetimes>0</pausetimes>
<abnormaltimes>0</abnormaltimes>
<successtimes>0</successtimes>
<failuretimes>0</failuretimes>
<abortedtimes>0</abortedtimes>
<successcosttime>0</successcosttime>
<failurecosttime>0</failurecosttime>
<abortedcosttime>0</abortedcosttime>
<offlinecosttime>9569</offlinecosttime>
<pausecosttime>0</pausecosttime>
<idlecosttime>674196</idlecosttime>
<connectingcosttime>0</connectingcosttime>
<abnormalcosttime>0</abnormalcosttime>
<interruptiblecosttime>0</interruptiblecosttime>
<sharingcosttime>0</sharingcosttime>
<exclusivecosttime>0</exclusivecosttime>
<status>2</status>
<clusterid>0</clusterid>
<clusterleader>false</clusterleader>
<needreboot>false</needreboot>
<category/>
<properties/>
<requirements/>
<constraints/>
</nodeitem>""".format(id,line.strip(), host_name, host_name))
            xml_file.flush()
            xml_file.close()

            xml_cfg = open('xml_cfg.xml', mode="a", encoding="utf-8")
            xml_cfg.write("<nodeitem>\n<id>{}</id>\n</nodeitem>\n".format(id))
            xml_cfg.flush()
            xml_cfg.close()

if __name__ == "__main__":
    import_munu()
