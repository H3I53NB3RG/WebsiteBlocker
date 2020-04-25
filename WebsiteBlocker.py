
import time
from datetime import datetime as dt

import subprocess

subprocess.call(["clear"])

f = open("banner.txt","r")
print(f.read())
f.close()

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"

websitesFile = open("websiteList.txt")
websiteList = []

try:
    start = input("Enter The Hour [0-24] At Which u Wanna Start Blocking This Sites : ")
    end = input("Enter The Hour [0-24]  At Which u Wanna Stop Blocking This Sites : ")

    x = int(start)
    z = int(end)

    while True:
        if start and end:
            if (x in range(0,25)) and (z in range(0,25)):
                for website in websitesFile:
                    if website[0] != "#":
                        websiteList.append(website)
                    else:
                        pass

                if x < (dt.now().hour) < z:
                    with open(hosts_path,"r+") as file:
                        content = file.read()
                        for website in websiteList:
                            if website in content:
                                pass
                            else:
                                file.write(redirect + " " + website + "\n")
                    
                else:
                    with open(hosts_path,'r+') as file:
                        content=file.readlines()
                        file.seek(0)
                        for line in content:
                            if not any(website in line for website in websiteList):
                                file.write(line)
                        file.truncate()
		
                print("[+] Running ...")
                time.sleep(5)
            else:
                print("[-] The Hours Are Not Between 0 and 24")
                break;
	    
	    
        else:
            print("[-] Please, Enter The Hours And Make Sure They're Between 0 and 24")
            break

except:
	print("[-] Please, Enter The Hours And Make Sure They're Between 0 and 24")
