from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests
from bs4 import BeautifulSoup
import random

def meigen():
	collect=[]
	collect2=[]
	d={}
	r=requests.get("https://meigen-ijin.com/genki/")
	soup = BeautifulSoup(r.content, "html.parser")
	kotoba=soup.select("p.meigen")
	detail=soup.select("p.ijin")
	for item in kotoba:
		collect.append(item.text)
	for item in detail:
		collect2.append(item.text)

	num=2
	while num<=5:
		r=requests.get("https://meigen-ijin.com/genki/"+str(num))
		soup = BeautifulSoup(r.content, "html.parser")
		kotoba=soup.select("p.meigen")
		for item in kotoba:
			collect.append(item.text)
		for item in detail:
			collect2.append(item.text)
		num += 1

	number=0
	while number<len(collect):
		d[collect[number]]=collect2[number]
		number += 1

	ran=random.choice(list(d.items()))
	message=ran[0]+"\n\n\n"+ran[1]

	return message

line_bot_api = LineBotApi(ENV['CHANNEL_ACCESS_TOKEN'])

line_bot_api.push_message(ENV['USER_ID'], TextSendMessage(text=meigen()))




