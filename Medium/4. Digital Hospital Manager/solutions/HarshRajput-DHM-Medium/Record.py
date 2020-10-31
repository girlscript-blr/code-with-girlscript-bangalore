import sqlite3
import datetime

class Record:
	def __init__(self):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute(''' CREATE TABLE IF NOT EXISTS Patients(
			Id int NOT NULL PRIMARY KEY,
			Name text,
			PhoneNumber int,EmergencyNumber int,
			Age int,Gender text, BloodType text,
			Weight int,Height int,
			DateOfAdmission text)
			''')

		c.execute(''' CREATE TABLE IF NOT EXISTS MedicalData(
			Pid int NOT NULL,
			Symptoms char(20),MedicalDetails char(25),
			Severity text,DateOfDischarge text, DischargeComment text,
			DateAndTimeOfDeath text,
			FOREIGN KEY(Pid) REFERENCES Patients(Id)
			)
			''')
		conn.commit()
		conn.close()

	def add_patient(self,pat,med):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute(''' INSERT INTO Patients VALUES(?,?,?,?,?,?,?,?,?,?)''',(pat.reg,pat.name,pat.phnno,pat.emgno,pat.age,pat.gender,pat.bloodtype,pat.weight,pat.height,pat.date))
		c.execute(''' INSERT INTO MedicalData VALUES(?,?,?,?,?,?,?)''',(med.reg,med.symptoms,med.medical_details,med.severity,med.date_of_discharge,med.discharge_comment,med.d_and_t_of_death))
		conn.commit()
		conn.close()

	def show_all(self):
		print("- - - - - - - - - - - - - - - - -- - - - - - --  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  -")
		print('''Patient ID \t Patient Name \t   Phone Number   Emergency Contact.No \t Age  Gender  Blood Type  Weight  Height      Date of Admission  ''')
		print()
		print('''Symptoms       Medical Details      Severity    DateOfDischarge    DischargeComment      Date and Time of Death ''')
		print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - -- -- -- - - - ")
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute('''SELECT Patients.Id,Patients.Name,Patients.PhoneNumber,Patients.EmergencyNumber,Patients.Age,
		                    Patients.Gender,Patients.BloodType,Patients.Weight,Patients.Height,Patients.DateOfAdmission,
		                    MedicalData.Symptoms,MedicalData.MedicalDetails,MedicalData.Severity,MedicalData.DateOfDischarge,
		                    MedicalData.DischargeComment,MedicalData.DateAndTimeOfdeath
		                     FROM Patients,MedicalData Where Patients.ID=MedicalData.Pid ''')
		arr=c.fetchall()
		c=0
		print()
		for row in arr:
			c+=1
			print(row[0],"\t",row[1],row[2],"  ",row[3],"  \t",row[4],"  ",row[5],"    ",row[6],"\t  ",row[7],"\t  ",row[8],"\t\t",row[9])
			print()
			print(row[10],row[11],"  ",row[12]," ",row[13],"  ",row[14],"  ",row[15])
			print()
			print()
			print()
		print("Total Patients in Hospital are: ",c)
		conn.commit()
		conn.close()

	def update_medicaldetails(self,ide,st):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute(''' UPDATE MedicalData set MedicalDetails=(?) where Pid=(?)''',(st,ide,))
		conn.commit()
		conn.close()

	def update_dischargedate(self,ide,st):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute(''' UPDATE MedicalData set DateOfDischarge=(?) where Pid=(?)''',(st,ide,))
		conn.commit()
		conn.close()

	def update_cure(self,ide,st):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute(''' UPDATE MedicalData set DischargeComment=(?) where Pid=(?)''',(st,ide,))
		conn.commit()
		conn.close()

	def update_deceased(self,ide,st,fin):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute(''' UPDATE MedicalData set DischargeComment=(?) where Pid=(?)''',(st,ide,))
		c.execute(''' UPDATE MedicalData set DateAndTimeOfdeath=(?) where Pid=(?)''',(fin,ide,))
		conn.commit()
		conn.close()

	def show_by_id(self,ide):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute('''SELECT * FROM Patients Where ID=(?) ''',(ide,))
		arr=c.fetchone()
		c.execute('''SELECT MedicalData.Symptoms,MedicalData.MedicalDetails,MedicalData.Severity,MedicalData.DateOfDischarge,
		                    MedicalData.DischargeComment,MedicalData.DateAndTimeOfdeath
		                     FROM MedicalData Where MedicalData.Pid=(?)''',(ide,))

		brr=c.fetchone()
		conn.commit()
		conn.close()
		print("--------------------------------------------------------------------------------------------------")
		print("            INPUT                                                             VALUES              ")
		print('--------------------------------------------------------------------------------------------------')
		print(f"       Patient ID                                                             {arr[0]}   ")
		print(f"       Patient Name                                                           {arr[1]}")
		print(f"       Phone Number                                                           {arr[2]}")
		print(f"       Emergency Contct Number                                                {arr[3]}")
		print(f"       Age                                                                    {arr[4]}")
		print(f"       Gender                                                                 {arr[5]}")
		print(f"       Blood-Type                                                             {arr[6]}")
		print(f"       Weight                                                                 {arr[7]}")
		print(f"       Height                                                                 {arr[8]}")
		print(f"       Symptoms                                                               {brr[0]}")
		print(f"      *Severity                                                               {brr[2]}")
		print(f"      Medical Details                                                         {brr[1]}")
		print(f"      Date of Admission                                                       {arr[9]}")
		print(f"      Date of Discharge                                                       {brr[3]}")
		print(f"      Discharge Comment                                                       {brr[4]}")
		print(f"      Date And Time of Death                                                  {brr[5]}")
		print(f"--------------------------------------------------------------------------------------------------")

	def count_admission_date(self,date):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute('''SELECT * FROM Patients Where DateOfAdmission=(?) ''',(date,))
		print("Patients admitted on current date are:",len(c.fetchall()))
		conn.commit()
		conn.close()

	def count_discharge_date(self,date):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute('''SELECT * FROM Patients Where DateOfDischarge=(?) ''',(date,))
		print("Patients dicharged on current date are:",len(c.fetchall()))
		conn.commit()
		conn.close()

	def count_all(self):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute('''SELECT * FROM Patients ''')
		print("Patients currently in database are :",len(c.fetchall()))
		conn.commit()
		conn.close()

	def delete(self,ide):
		conn=sqlite3.connect("database.db")
		c=conn.cursor()
		c.execute(''' DELETE FROM Patients WHERE Id=(?)''',(ide,))
		c.execute(''' DELETE FROM MedicalData WHERE Pid=(?)''',(ide,))
		conn.commit()
		conn.close()