import requests

url = "http://webhacking.kr/challenge/web/web-05/mem/login.php"


headers = {
"Cookie":"oldzombie=1; PHPSESSID=ce7d7b3317819f9f01951a6263279e37",
"Host":"webhacking.kr"	
}

params = {
"id":"admin",
"pw":"qwer12"
}


req = requests.post(url,headers=headers,data=params)

res = req.content
print res