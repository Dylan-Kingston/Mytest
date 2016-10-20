#!/usr/bin/python

import sys
import subprocess

ans=True

def help_menu():

    print("\nWelcome To The Basic Networking Shell.")
    print("Select an option from the list below.\n")

    print("1. Display The Current User Of The Shell.")
    print("2. Display The Current Working Directory.")
    print("3. Display Settings For Interface eth0.")
    print("4. ")
    print("exit. Exit The Networking Shell.")

while ans:

    ans = raw_input(">:" )

    if ans=="whoami":
      subprocess.call("whoami",shell=True)
 
    elif ans=="who":
      subprocess.call("who",shell=True)

    elif ans=="pw":
      subprocess.call("pwd",shell=True)

    elif ans=="pwd":
      subprocess.call("pwd",shell=True)

    elif ans=="ifc":
      subprocess.call("ifconfig",shell=True)

    elif ans=="ifconfig":
      subprocess.call("ifconfig",shell=True)

    elif ans=="help":
      help_menu()      

    elif ans=="exit":
      print("Exiting The Shell.\n") 
      ans = None

    elif ans=="":
      ans = True

    else:
      print("Incorrect choice. Try again\n")
      ans = True
