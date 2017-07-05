import csv
import json
from firebase import firebase
import datetime
#mi objeto de firebase
firebase = firebase.FirebaseApplication('https://haha-4cf04.firebaseio.com', None)
     
data = []

#LEYENDO INFO DEL CSV 
with open('/mnt/d/DMS/yourBigFile3.txt')as f:
	read = f.readlines()
	i=0
	for row in read:
		size =(row[0])
		type = (row[1])
		tlt = (row[2])	
		category =(row[3])
		sender = (row[4])
		reciver = (row[5])
		lat = (row[6])
		long1 = (row[7])
		datetime = (row[8])
		group =(row[9])
		name =1
		#dateTime = datetime.datetime.strptime(dateTime, "%Y/%m/%d %H:%M:%S")
		#print str(dateTime1) + '->' + str(dateTime)
		print name
		print size
		print type
		print tlt
		print category
		print sender
		print reciver
		print lat
		print long1
		print datetime
		print group
		i=i+1
		firebase.put('/onlineMCS',i,{"name": name,"type": type,"tlt": tlt,"category": category,"sender": sender,"reciver": reciver,"lat": lat,"long": long1,"datetime": datetime, "group": group,"size":size})
