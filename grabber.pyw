import requests
import smtplib
import getpass
import socket
import time
from datetime import date


isConnected = 0
while isConnected == 0:
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        continue
    else:
        isConnected = 1

username = getpass.getuser()
today = date.today()

t = time.localtime()
current_time = time.strftime("%H : %M : %S", t)

cdate = today.strftime("%B %d, %Y")

ip = requests.get('http://ip.42.pl/raw').text
ip = "User Name : " + username + "\n" + "IP Address : " + ip + "\n" + "Date : " + cdate + "\n" + "Time : " + current_time

Subject = username + "'s PC has been started!!!"

message = 'Subject: {}\n\n{}'.format(Subject, ip)

server = smtplib.SMTP("smtp.gmail.com", 587)

# For the working of the app you have to enable your account to work with
# less secure apps link: https://myaccount.google.com/lesssecureapps
server.starttls()
email = "<username>"   # Email address from which email is to be sent
epass = "<Password>"   # Email password from which email is to be sent
destemail = "<EMAIL>"  # Destination Email where you receive prompts (it could be any Email address)

server.login(email, epass)


server.sendmail(email, destemail, message)

server.quit()
