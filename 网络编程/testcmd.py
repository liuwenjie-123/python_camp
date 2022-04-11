import os

cmd1 = "C:\\sa\\scripts\\raid\\perccli64.exe /c0/eall/sall show |findstr \"SSD HDD\""
d = os.popen(cmd1)
f = d.read()
print(f)
