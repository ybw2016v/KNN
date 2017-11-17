#python3
import requests
import json
def knnpost(text):
	pass
	url="https://oapi.dingtalk.com/robot/send?access_token=e0bde372efc3ec08d2a535922568073ab942eacbc715baa6980b5b2ee0865288"
	data={ "msgtype": "text", "text": {"content": text}}
	HEADERS = {"Content-Type": "application/json ;charset=utf-8 "}
	p=requests.post(url,data=json.dumps(data),headers=HEADERS)
	print(p.text)
# dog=input("text")
# knnpost(dog)
