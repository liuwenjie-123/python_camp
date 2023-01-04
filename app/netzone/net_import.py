
template = """[{MAC}]
Name={Name}
MAC={MAC}
IP={IP}
Mask={Mask}
Gateway={Gateway}
BootServer={BootServer}
IOServer={IOServer}
Port=18003
Disk={Disk}
DeleUndo=1
EnableBAW=1
DataDisk=0
DataDiskSize=
DefPrinter=
OtherPrinter=
Desc=
DifVer=5
ResIndex=0
xres=0
yres=0
RefIndex=0
WksGrpId={WksGrpId}
WksGrpName={WksGrpName}

"""

with open("nodeList.txt", mode='rt', encoding="utf-8") as f:
    for i in range(68, 73):
        data = f.readline().split("\t")
        Name = "ZX" + ("%05d" % i)
        MAC = data[1].strip()
        IP = data[0].strip()
        Mask = "255.255.255.0"
        Gateway = "10.117.120.254"
        BootServer = "10.117.120.249"
        IOServer = "10.117.120.249"
        Disk = "1909-ry-02"
        WksGrpId = "0003"
        WksGrpName = "ZX"
        with open("import_data.ini", mode="a", encoding='utf-8') as fd:
            fd.write(template.format(Name=Name, MAC=MAC, IP=IP, Mask=Mask, Gateway=Gateway, BootServer=BootServer, IOServer=IOServer, Disk=Disk, WksGrpId=WksGrpId, WksGrpName=WksGrpName))