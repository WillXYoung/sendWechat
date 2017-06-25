import time
import pickle
import sys
import httplib
#case [ticketnumber , caseown , Customer ,(time)]
case1=[5,'wyn','token',19]
case2=[3,'xgga','token',15]
def CheckIfSend(case):
	with open('data.pkl','rb') as oldre:
		dir=pickle.load(oldre)
	nowtme=int(time.strftime("%H"))
	ticket=case[0]
	if dir.has_key(ticket):
		flagtme=dir.get(case[0])[-1]
		if flagtme == nowtme:
			pass
		elif flagtme <= nowtme or (flagtme == 23 and nowtme == 00):
			print "notify : ALL "
			FindToken(case,'allmember')
			dir[case[0]][-1]=24
		elif flagtme >= 24:
			dir[case[0]][-1]+=1
			if dir[case[0]][-1] == 36:
				del(dir[ticket])
	else :
		flagtme=nowtme
		case.append(flagtme)
		dir[ticket]=case[:]
		if 15 < flagtme < 22 :
			print "notify : owner & duty"
			FindToken(case,'duty')
		else:
			print "notify : owner & OC"
			FindToken(case,'oc')
		print dir
	with open('data.pkl','wb') as newre:
		pickle.dump(dir,newre)
	print dir
	

def FindToken(case,other):
	contact={
		'wyn':'7ef10aab88b346f8e4a221ffe0fdd934'
	}
	if other == 'allmember':
#		token=contact.get(case[1])
		for key in contact.keys():
			token=contact.get(key)
			headerdata = {"Servicetoken":token}
#    headerdata.update({"Servicetoken":token})
			alart_msg = '{{"content":"{}"}}'.format(case[:-1])
			conn = httplib.HTTPConnection("www.linkedsee.com")
			conn.request("POST","/alarm/custom/",alart_msg,headerdata) 
			response = conn.getresponse()
			res = response.read()
			return res
	elif other =='oc' or other =='duty':
		for key in contact.keys():
			token=contact.get(key)
			headerdata = {"Servicetoken":token}
#    headerdata.update({"Servicetoken":token})
			alart_msg = '{{"content":"{}"}}'.format(case[:-1])
			conn = httplib.HTTPConnection("www.linkedsee.com")
			conn.request("POST","/alarm/custom/",alart_msg,headerdata) 
			response = conn.getresponse()
			res = response.read()
			return res

CheckIfSend(case1)
