'''
Some notes:
1. It's good practice to use the with keyword when dealing with file objects as I do below.  This has the advantage
that the file is properly closed, even if an exception is raised.  It's also must shorter than equivalent try-finally blocks of code.

2. The any function is a generator expression.  Since you can't delete lines from a stream when reading files, we have to basically
rewrite the lines and then truncate the file from a point so that it's not duplicated.


'''

import time
import datetime

hosts_path=r"/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.yahoo.com", "yahoo.com"]

START_WORK_HOUR = 7
STOP_WORK_HOUR = 18

while True:
    now = datetime.datetime.now()
    if now.hour >= START_WORK_HOUR and now.hour <= STOP_WORK_HOUR:
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
               if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(10)