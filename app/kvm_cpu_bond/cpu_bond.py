"""
cpu_bond =  <iothreads>2</iothreads>
	<cputune>
    <vcpupin vcpu='0' cpuset='1'/>
    <vcpupin vcpu='1' cpuset='2'/>
    <vcpupin vcpu='2' cpuset='3'/>
    <vcpupin vcpu='3' cpuset='4'/>
    <vcpupin vcpu='4' cpuset='37'/>
    <vcpupin vcpu='5' cpuset='38'/>
    <vcpupin vcpu='6' cpuset='39'/>
    <vcpupin vcpu='7' cpuset='40'/>
	<vcpupin vcpu='8' cpuset='37'/>
    <vcpupin vcpu='9' cpuset='38'/>
    <vcpupin vcpu='10' cpuset='39'/>
    <vcpupin vcpu='11' cpuset='40'/>
	<emulatorpin cpuset='9-12,45-48'/>
    <iothreadpin iothread='1' cpuset='9-10'/>
    <iothreadpin iothread='2' cpuset='11-12'/>
    </cputune>"
"""

"""
  <cpu mode='host-passthrough' check='none'>
    <topology sockets='1' cores='6' threads='2'/>
  </cpu>
"""


# vcpu的数量
vcpu_number = 14
# io线程数
iothreads = 2
# 物理cpu列表
cpu_list = []
# emulatorpin cpuset的值
cpuset_list = []
# numa node cpu列表
node = {
    "node01" : "1-27",
    "node02" : "57-83",
    # "node03" : "39-40",
    # "node04" : "75-77",
    # "node05" : "81-83",
    # "node06" : "87-88",
    # "node07" : "98-101",
    # "node08" : "105-107",

}
# cpu拓扑配置
sockets = 1
cores = 7
threads = 2
# 适配原神配置， 0 不适配，1适配
disable_hypervisor = 0


# 1、输出vcpu数量
vcpu_numbers = "  <vcpu placement='static'>{}</vcpu>".format(vcpu_number)


# 2、输出vpuc绑定信息
# 生成vcpu-物理cpu的列表
for i in node.items():
    cpuset_list.append(i[1])
    for cpu in range(int(i[1].split("-")[0]), int(i[1].split("-")[-1]) + 1):
        cpu_list.append(cpu)

# 生成cpuset数据
cpuset_number = int(len(node) / 2)

# 输出绑定信息
for i in range(vcpu_number):
    if i == 0:
        print("""<iothreads>2</iothreads>\n<cputune>\n    <vcpupin vcpu='{}' cpuset='{}'/>""".format(i, cpu_list[i]))
        continue

    if i == vcpu_number - 1:
        print("""    <vcpupin vcpu='{}' cpuset='{}'/>\n	<emulatorpin cpuset='{}'/>
    <iothreadpin iothread='1' cpuset='{}'/>
    <iothreadpin iothread='2' cpuset='{}'/>
    </cputune>""".format(i, cpu_list[i], ",".join(cpuset_list), ",".join(cpuset_list[0:cpuset_number]), ",".join(cpuset_list[cpuset_number:])))
        continue

    print("    <vcpupin vcpu='{}' cpuset='{}'/>".format(i, cpu_list[i]))


# 3、输出CPU拓扑
if disable_hypervisor:
    print("""  <cpu mode='host-passthrough' check='none'>
    <topology sockets='{}' cores='{}' threads='{}'/>
  </cpu>""".format(sockets, cores, threads) )
else:
    print("""    <cpu mode='host-passthrough' check='none'>
     <topology sockets='{}' cores='{}' threads='{}'/>
     <feature policy='disable' name='hypervisor'/>
    </cpu>""".format(sockets, cores, threads))