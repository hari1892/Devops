#Author        :  Hari Rajendiran
#email         :  hari1892@gmail.com
#Script Title  :  Dhcp Parser
#####################################

#!/usr/bin/python
import re
import os
import sys

scriptname = sys.argv[0]
if len(sys.argv) < 2:
    print("Pass the Dhcp lease file as Argument")
    exit()
elif len(sys.argv) != 2:
    print("Multiple Arguments not allowed")
    exit()
    
dhcplease = sys.argv[1]



if os.path.isfile(dhcplease) == True:
    fopen = open(dhcplease,'r')
    leasecontentcheck = fopen.read()
    check = re.findall(r'lease\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',leasecontentcheck)
    fopen.close()
    if not check:
        print(dhcplease + "is not a valid dhcp lease file")
        exit()
else:
    print("Invalid Input, pass valid dhcp lease file as argument")
    exit()


Linux_shell_command = 'cat ' + dhcplease + "| sed -n '/^lease.*/,/}/p' | sed 's/}/}\\n---/g' > /tmp/test;sed -i '$d' /tmp/test"
os.system(Linux_shell_command)


f = open('/tmp/test','r')
contents = f.read()
print('MAC ADDRESS'.ljust(18)+ '       ' + 'IP ADDRESS' + '         ' + 'Lease Start Time' + '             ' + 'Lease End Time')
print('=========================================================================================================================')
for i in contents.split('---'):
    line = i.split('\n')
    for i in line:
        if re.findall(r'lease',str(i)):
            ip = re.findall(r'lease\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',str(i))
        if re.findall(r'hardware ethernet',str(i)):
            mac_addr = re.findall(r'hardware ethernet (.*)',str(i))
        if re.findall(r'starts',str(i)):
            start = re.findall(r'starts (.*)',str(i))
        if re.findall(r'ends',str(i)):
            end = re.findall(r'ends (.*)',str(i))
    print(str(mac_addr).strip('[,],\'') + '       ' + str(ip).strip('[,],\'') + '       ' + str(start).strip('[,],\'') + '       ' + str(end).strip('[,],\''))

f.close()
os.unlink('/tmp/test')
