from itertools import product
import hashlib
import requests


quest = "YzQwMzNiZmY5NGI1NjdhMTkwZTMzZmFhNTUxZjQxMWNhZWY0NDRmMg=="
chars = 'abcdefghijklmnopqrstuvwxyz'
count = 0

for _ in product(chars, repeat=4):
	answer = "".join(_)
	h1 = hashlib.sha1(answer).hexdigest()
	h2 = hashlib.sha1(h1).hexdigest()
	h3 = h2.encode("base64").rstrip('\n') # 인코딩하면 값 뒤에 개행이 붙어 지워준다.

	if h3 == quest:
		print h1
		print h2
		print h3
		print "answer!! =====> "+answer

url = "http://webhacking.kr/challenge/web/web-04/index.php"


headers = {
	"Cookie":"oldzombie=1;PHPSESSID=ce7d7b3317819f9f01951a6263279e37",
	"Host":"webhacking.kr",
	"Origin":"http://webhacking.kr",
	"Content-Type": "application/x-www-form-urlencoded",
	"Referer":"http://webhacking.kr/challenge/web/web-04/"
}

params = "key=" + answer

req = requests.post(url, headers=headers, data=params)
res = req.content
print res
