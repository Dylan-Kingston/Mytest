#!/usr/bin/python

import sys
import subprocess

ans=True

while ans:
    print("\nWelcome To The Basic Networking Shell.")
    print("Select an option from the list below.\n")

    print("1. Display The Current User Of The Shell.")
    print("2. Display The Current Working Directory.")
    print("3. Display Settings For Interface eth0.")
    print("4. ")
    print("exit. Exit The Networking Shell.")

    ans = raw_input("\n>:" )

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

    elif ans=="exit":
      print("Exiting The Shell.\n") 
      ans = None

    else:
      print("Incorrect choice. Try again\n")
      ans = True
