import requests

url = "http://webhacking.kr/challenge/bonus/bonus-12/?mode=del&time=1518070925"


headers = {
	"Cookie":"PHPSESSID=796c524a5dee9f2dd841854840012bb1",
	"Host":"webhacking.kr"
}


req = requests.get(url, headers=headers)
print repr(req.content)