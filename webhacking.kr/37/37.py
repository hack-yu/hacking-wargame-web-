#1517892391


import requests
for i in range(1,100):
	url = "http://webhacking.kr/challenge/web/web-18/"



	files = {

	'upfile' : ('tmp-1517893700',open('tmp-1517893700','rb'),'multipart/form-data')

	}


	headers = {
		"Cookie":"PHPSESSID=8aa8b01919b86d9a80f524a71c187ce9",
		"Host":"webhacking.kr"
	}

	req = requests.post(url,files = files, headers=headers)

	print req.content