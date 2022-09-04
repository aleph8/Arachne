import os 
import sys
import re 

def install():
    print("[!] Working ...")
    ssh_command("sudo apt update && sudo apt -y upgrade")
    ssh_command("echo $(hostname -I)")
    ssh_command("sudo apt -y install python3 python3-pip")
    ssh_command("sudo pip3 install adafruit-circuitpython-servokit Adafruit-PCA9685")
    ssh_command("sudo apt -y autoremove")
    ssh_command("sudo raspi-config")
    ssh_command("mkdir ~/arachne")
    os.system("scp -i ~/.ssh/arachne movements/* 'prototype@%s:~/arachne/'" % local_ip_adress)


def ssh_command(com):
    os.system("ssh -i ~/.ssh/arachne prototype@%s '%s' " % (local_ip_adress,com))

def help():
    print(usage)

def discovery(ops):
    if ops == "Linux":
        print("[!] Waiting for ip ...")
        disc_ip = os.popen('ping -c 1 arachne.local | grep "PING arachne.local" | awk -F"(" \'{print $2}\' | awk -F")" \'{print $1}\' | tr -d \'\\n\'').read()
        print ("[!] The ip is %s" % disc_ip)
        change_ip(disc_ip)

        os.system("ssh-keygen -t rsa -f ~/.ssh/arachne -N \"\"")
        os.system("ssh-copy-id -i ~/.ssh/arachne.pub prototype@%s" % local_ip_adress)

    else:
        print("Work in progress (Windows) !")

def change_ip(ip):

    if not re.match(r"^[0-9]+.[0-9]+.[0-9]+.[0-9]+",ip,flags=re.MULTILINE):
        print("[x] An error has occurred with the wrong IP value (%s)\n" % ip )
        exit(255)

    print("[!] Changing the ip ... ")
    # BASH OPTION # 

    # os.system("sed -E -i 's/^local_ip_adress = .*/local_ip_adress = \"%s\"/' arachne.py" % ip)
    
    ############### 

    # PYTHON ALTERNATIVE #

    file_data = open("arachne.py","r").read()
    file_write = open("arachne.py","w")
    file_write.write(re.sub(r'^local_ip_adress = .*',r'local_ip_adress = "%s"' % ip,file_data,flags=re.MULTILINE))
    file_write.close()

    ######################
    print("[!] Done!")
    print("[!] Local IP = %s \n" % ip)


# VARIABLES #

local_ip_adress = "0.0.0.0"

start = """

                       _                   _                
                      / \   _ __ __ _  ___| |__  _ __   ___        | 
                     / _ \ | '__/ _` |/ __| '_ \| '_ \ / _ \\       |
                    / ___ \| | | (_| | (__| | | | | | |  __/      \\0/
                   /_/   \_\_|  \__,_|\___|_| |_|_| |_|\___|      /o\\
                                                            

[!] Local IP = %s
""" % (local_ip_adress)

usage = """
    [!] Usage = python3 arachne.py [OPTION]

    OPTIONS:

    -i <local_ip_adress> : change the local ip adress 

    -h : help panel 

    -d <Windows/Linux> : Search in the local network the IP of arachne with arachne.local and generate ssh key
    
    --install : Install what you need on the RasPi.
"""

#############

### MAIN ###
args = sys.argv
sentinel = 1

while (sentinel < len(args)):

    if args[sentinel] == "-i":
        print(start)
        change_ip(args[sentinel+1])
    elif args[sentinel] == "-d" and (args[sentinel+1] == "Linux" or args[sentinel+1] == "Windows") :
        print(start)
        discovery(args[sentinel+1])
    elif args[sentinel] == "--install":
        print(start)
        install()
    else:
        help()

    #print(args[sentinel])
    sentinel += 2

############