#!/usr/bin/python3
print("content-type:text/html")
print()


import cgi
import subprocess
import os

y=cgi.FieldStorage()

verify=y.getvalue("pass")

if verify=="redhat":
    cmd=y.getvalue("cmd")
    lst=[]
    lst=cmd.split(',')
    for i in lst: 
        wds=[]
        wds=i.split()
        if("docker" in wds and ("status" in wds or "service" in wds)):
            print("command=sudo systemctl status docker")
            output=subprocess.getoutput("sudo systemctl status docker")
            print(output)
            print("\n \n \n")
        elif("cal" in wds or "calendar" in wds):
            print("command=cal")
            output=subprocess.getoutput("cal")
            print(output)
            print("\n \n \n")

        elif("date" in wds):
            print("command=date")
            output=subprocess.getoutput("date")
            print(output)
            print("\n \n \n")

        elif(("list" in wds and ("files"in wds or"file" in wds))or "ls" in wds):
            print("command=ls")
            output=subprocess.getoutput("ls")
            print(output)
            print("\n \n \n")


        elif(("ram" in wds or "memory" in wds)and("usage" in wds or "status"in wds)):
            print("command=free -m")
            output=subprocess.getoutput("free -m")
            print(output)
            print("\n \n \n")

        elif("docker" in wds and "container" in wds and ("launch" in wds or "start" in wds)):
            print("command=sudo docker run -dit --name=myos1111 wordpress")
            output=subprocess.getoutput("sudo docker run -dit --name=myos1111 wordpress")
            print(output)
            print("\n \n \n")

        elif("docker" in wds and "container" in wds and "stop" in wds):
            print("command=sudo docker stop myos1111")
            output=subprocess.getoutput("sudo docker stop myos1111")
            print(output)
            print("\n \n \n")

        elif("create" in wds and "folder" in wds):
            print("command=mkdir fold1")
            output=subprocess.getoutput(" sudo mkdir fold1")
            print(output)
            print("\n \n \n")

                                                 
    elif("docker" in wds and ("container" in wds or "containers" in wds)):
            print("command=sudo docker ps")
            output=subprocess.getoutput("sudo docker ps")
            print(output)
            print("\n \n \n")

        elif("docker" in wds and ("image" in wds or "images" in wds)):
            print("command=sudo docker images")
            output=subprocess.getoutput("sudo docker images")
            print(output)
            print("\n \n \n")

        elif("create" in wds and ("file" in wds)):
            print("command=touch a.txt")
            output=subprocess.getoutput("sudo touch a.txt")
            print(output)
            print("\n \n \n")


        else:
            print("Commands not supported!!")
else:
    print("Please enter valid credentials!!")
