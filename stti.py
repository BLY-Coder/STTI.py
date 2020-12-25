import requests
from bs4 import BeautifulSoup as bs

file= open("stti.txt",'r')
read_file= file.readlines()


for i in b:
	req = requests.get(""+i.replace("\n","")).text
	aa = bs(req,"lxml")
	bb = aa.find("str")
	if bb != None and "<str>"+i.replace("\n","")+"<str>" != bb:
		print("[*] Payload: ",i.replace("\n",""))
		print(bb)
		print()

