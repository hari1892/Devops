#!/usr/bin/python3.5
import pexpect
import sys
import os
import argparse
import re

def usage():
    ipinputlist = ''
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ipaddr", help="Enter a single ip")
    parser.add_argument("-f","--file", help="File with list of ipv4 address delimited by newline")
    parser.add_argument("-u","--user", help="Remote user name to connect")
    parser.add_argument("-p","--password", help="Remote user password to connect")
    parser.add_argument("-C","--command", help="Enter Shell command to execute on remote system")
    args = parser.parse_args()
    b = {'file':'','ipaddr':'','user':'','password':'','command':''}
    b.update(file = str(args.file))
    b.update(ipaddr = str(args.ipaddr))
    b.update(user = str(args.user))
    b.update(password = str(args.password))
    b.update(command = str(args.command))
    filepath = b['file']
    ipa = b['ipaddr']
    user = b['user']
    password = b['password']
    command = b['command']
    if b['user'] == 'None' or b['command'] == 'None' or b['password'] == 'None':
        print("User,command and password are mandatory")
        exit()
    if b['ipaddr'] == 'None' and  b['file'] == 'None':
        print('Enter input as single ip or file with list of ips')
        exit()
    if b['ipaddr'] != 'None' and  b['file'] != 'None':
        print('Enter one 1ip or a file path')
        exit()
    if str(filepath) != 'None' and os.path.isfile(os.getcwd() + '/'+str(filepath)) == True:
        fpath = os.getcwd() + '/'+str(filepath)
        filec = open(os.getcwd() + '/'+filepath,"rt")
        contents = filec.read()
#        iprecontents = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', contents)
        iprecontents = re.findall(r'(.+)', contents)
        filec.close()
        if not iprecontents:
            print("No valid ip address found in the file, may be the file is empty")
    elif ipa != 'None' and bool(re.findall(r'(.+)', ipa)) == True:
        ipinputs = []
        delimited = re.split(',',ipa)
        for i in delimited:
            temp = re.findall(r'(.+)', i)
            ipinputs.append(temp)
        ipinput = []
        for j in ipinputs:
            for k in j:  
                ipinput.append(k)
    if b['ipaddr'] == 'None':
        ipinputlist = iprecontents
        print( "Ip address:" + str(ipinputlist) + '\n' + "Remote User:"+ user + '\n' + 'Remote_command:' + command + '\n' + 'Remote_password:' + password)
    else:
        ipinputlist = ipinput
        print("Ip address:" + str(ipinputlist) + '\n' + "Remote User:"+ user + '\n' + 'Remote_command:' + command + '\n' + 'Remote_password:' + password)
        print("================================================================================>")
    

    ssh_cmd(user,command,password,list(ipinputlist))


def ssh_cmd(user,cmd,password,ipinputlist):
    k = 0
    for j in ipinputlist:
        realip = ipinputlist[k]
        print("=========================================================>")
        print("Printing Result for" + ' ' +  str(realip))
        ssh = pexpect.spawn('ssh %s@%s "%s;echo $?"' % (user,realip,cmd))
#        ssh.delaybeforesend = 2
#        print(ssh)
        print("=================================================================================>")
        k = k + 1
        try:
            j = ssh.expect(['password:', 'continue connecting (yes/no)?'],timeout=5)
            if j == 0 :
                a = ssh.sendline(password)
#                o = ssh.expect (['Permission denied', '0'])
#                if str(o) == '1':
                r = ssh.read()
                print(r.decode("utf-8"))
                ssh.close()
#                else: raise Exception("User or Password Wrong")
            elif j == 1:
                ssh.sendline('yes')
                ssh.expect('password: ')
                o = ssh.expect (['Permission denied', '0'])
                a = ssh.sendline(password)
#                if str(o) == '1':
                r = ssh.read()
                print(r.decode("utf-8"))
#                else: raise Exception("User or Password Wrong")
        except pexpect.EOF:
            print("EOF--->" + ' ' + str(realip) + ' ' + "unable to connect to the machine, machine not reachable" )
        except pexpect.TIMEOUT:
            print("TIMEOUT,--->"+ ' ' + str(realip) + ' ' + "unable to connect with given password or machine not reachable")
        except Exception as e:
            print(e)
            print("INCORRECT USERNAME or PASSWORD---->" + str(realip) + ' ' + "Permission denied, incorrect username or password sent")
        else:
            ssh.close()


usage()

