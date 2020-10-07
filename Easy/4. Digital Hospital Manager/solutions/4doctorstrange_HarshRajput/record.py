import sqlite3
import datetime
from patients import patients

class record:
	def __init__(self):
		conn=sqlite3.connect("database.db")

		c=conn.cursor()
		c.execute(''' CREATE TABLE IF NOT EXISTS records(
			Id int,
			Name text,
			PhoneNumber int,EmergencyNumber int,
			Age int,Gender text, BloodType text,
			Weight int,Height int,
			Symptoms text, DateOfAdmission text)
			''')
		conn.commit()
		conn.close()

	def add_patient(self,pat):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute(''' INSERT INTO records VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(pat.reg,pat.name,pat.phnno,pat.emgno,pat.age,pat.gender,pat.bloodtype,pat.weight,pat.height,pat.symptoms,pat.date))
		conn.commit()
		conn.close()

	def show_all(self):
		print("Patient ID \t Patient Name \t   Phone Number   Emergency Contact.No \t Age  Gender  Blood Type  Weight  Height  Symptoms/Details \t  Date of Admission")
		print()
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute('''SELECT * FROM records ''')
		arr=c.fetchall()
		count=0
		for row in arr:
			count+=1
			print(row[0],"\t",row[1],row[2],"  ",row[3],"  \t",row[4],"  ",row[5],"    ",row[6],"\t  ",row[7],"\t  ",row[8],"    ",row[9],"\t  ",row[10])
		print()
		print("Total Number of patients in hospital are : ",count)
		conn.commit()
		conn.close()

	def showby_date(self,d):
		print("Patient ID \t Patient Name \t   Phone Number   Emergency Contact.No \t Age  Gender  Blood Type  Weight  Height  Symptoms/Details \t  Date of Admission")
		print()
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute(''' SELECT * FROM records WHERE DateOfAdmission=(?)''',(d,))
		arr=c.fetchall()
		for row in arr:
			print(row[0],"\t",row[1],row[2],"  ",row[3],"  \t",row[4],"  ",row[5],"    ",row[6],"\t  ",row[7],"\t  ",row[8],"    ",row[9],"\t  ",row[10])
		print()
		conn.commit()
		conn.close()

	def remove_patient(self,reg):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute(''' DELETE FROM records WHERE Id=(?)''',(reg,))
		conn.commit()
		conn.close()
	def get_bill(self):
		pass





'''
name="xyz sharma"
phnno=9810637282
emgno=862829292
age=20
gender="Male"
bloodtype="A+"
weight=89
height=179
symptoms="fever"
x=datetime.datetime.now()
date=x.strftime("%x")
reg=int(date.replace("/","")+str(phnno))
p=patients(reg,name,phnno,emgno,age,gender,bloodtype,weight,height,symptoms,date)
'''