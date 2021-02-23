# Import libraries
import time
from datatime import datatime as dt

# Windows host file path
hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"

# Add the website you want to block, in this list
while True:
     
    # Duration during which, website blocker will work
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() <
    dt(dt.now().year,dt.now().month,dt.now().day,18):
        print ("Sorry Not Allowed...")
        with open(hostsPath, 'r+') as file:
            content=file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
    else:
        with open(hostsPath, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
            file.truncate()
        print ("Allowed Access !")
    time.sleep(5)
