#-*- coding:utf8 -*-

import random
import smtplib

##########
# Config #
##########
host = "smtp.gmail.com:587" 
login = "YOUR_EMAIL_HERE@gmail.com"
password = "YOUR_PASSWORD_HERE"

people = [
    ["Person1", "person1@gmail.com"],
    ["Person2", "person2@hotmail.com"]
    ]


msg = """MIME-Version: 1.0
Content-type: text/html
Subject: Your secret pal is....
<br/><br/>
Hey {0}. <br/>
<br/>
You secret pal is <strong> {1} </strong>.<br/>
<br/>
<br/>
<br/>
Kind regards.
"""


########
# Code #
########
drawn = list(people)
raffle = True
while raffle:
    random.shuffle(drawn)
    raffle = False
    for i in range(len(people)):
        if people[i] == drawn[i]:
            raffle = True
            break


server = smtplib.SMTP(host)
server.starttls()
server.login(login,password)
print "List drawn"

for i in range(len(people)):
    print "Sending to " + people[i][0] + "...."
    server.sendmail(login,people[i][1],msg.format(people[i][0],drawn[i][0]))


server.quit()
