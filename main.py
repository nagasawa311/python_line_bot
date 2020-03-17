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

line_bot_api = LineBotApi("aSIw31tl8kO9bYUdBK4JPO/jFJ9JBC5Sr2lJo8/68QZ9R+CYuh7nrIZ8Rgby6h2Jerz7wOQw0v1tJM4ao2zRNc9ZPVZ3TkTcVHXkpA4Smc1H3SZY1Ge5qvTPShO+0LnUfRkUH9ojBQdH7riyGK5C4AdB04t89/1O/w1cDnyilFU=")

line_bot_api.push_message("U4d27304dab2cef4f34c16cf0be35fba1", TextSendMessage(text=meigen()))




