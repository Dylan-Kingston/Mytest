#!/usr/bin/python

from Tkinter import *
import sys
import subprocess
import os
import time
import getpass
import pwd
import grp

ans=True

def help_menu():

    print("\n\nWelcome To The Basic Networking Shell.")
    print("Select an option from the list below.\n")

    print("whoami |  Display The Current User Of The Shell.")
    print("who    |  List All Logged In Users.")
    print("pw     |  Display The Current Working Directory.")
    print("ifc    |  Display Settings For Interface eth0.")
    print("cal    |  Display The Calendar.")
    print("ls -al |  View The Contents Of The Current Directory.")
    print("dt     |  Display The Date And Time On The System.")
    print("ud     |  Display Standard Details For The Currently Logged-In User.")
    print("exit   |  Exit The Networking Shell.\n\n")

while ans:

    ans = raw_input(">:" )

    if ans=="whoami":
      subprocess.call("whoami",shell=True)
 
    elif ans=="who":
      subprocess.call("who",shell=True)

    elif ans=="pw":
      subprocess.call("pwd",shell=True)

    elif ans=="ifc":
      f = os.popen('/sbin/ifconfig eth0')
      result = f.read()
      print(result)

    elif ans=="cal":
      subprocess.call("cal",shell=True)

    elif ans=="ls -al":
      subprocess.call("ls -al",shell=True)

    elif ans=="dt":
      print(time.strftime("%Y%m%d%H%M%S"))

    elif ans=="ud":
      username=getpass.getuser()
      userId=pwd.getpwnam(username).pw_uid
      groupId = pwd.getpwnam(username).pw_gid
      groupName = grp.getgrgid(groupId).gr_name

      homeDirectory=os.getenv("HOME")
      info=os.stat(homeDirectory)
      iNode=info.st_ino

      print(str(userId)+","+str(groupId)+","+username+","+groupName+","+str(iNode))

    elif ans=="help":
      help_menu()      

    elif ans=="exit":
      print("Exiting The Shell.\n") 
      sys.exit()

    elif ans=="":
      ans = True

    else:
      print("Unknown Command.")
      ans = True
