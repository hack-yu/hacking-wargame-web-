import requests

url = "http://webhacking.kr/challenge/javascript/js2.html"

headers = {
	"Cookie":"PHPSESSID=ce7d7b3317819f9f01951a6263279e37"		
}

request = requests.get(url, headers=headers)

print request.content