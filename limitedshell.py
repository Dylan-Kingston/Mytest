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

    if ans=="1":
      print("1. whoami / who\n")
      subprocess.call("whoami",shell=True)
      subprocess.call("who",shell=True)
    elif ans=="2":
      print("2. pwd\n")
      subprocess.call("pwd",shell=True)
    elif ans=="3":
      print("3.\n")
      subprocess.call("ifconfig",shell=True)
    elif ans=="4":
      print("\n")
    elif ans=="exit":
      print("Exiting The Shell.\n") 
      ans = None
    else:
      print("Incorrect choice. Try again\n")
      ans = True 
