from Personal_data import Personal_data
from Medical_data import Medical_data
from Record import Record
import datetime
class Input:
	def get_input(self):
		n=int(input("Enter number of patients to be added in databases: "))
		for i in range(n):
			print("Enter personal details of patient: ",i+1)
			name=input("Enter name of patient: ")
			phnno=int(input("Enter Contact number: "))
			emgno=int(input("Enter Emergency contact number: "))
			age=int(input("Enter age of patient: "))
			gender=input("Enter Gender: ")
			bloodtype=input("Enter blood type of patient: ")
			weight=int(input("Enter weight of patient: "))
			height=int(input("Enter height of patient: "))
			agee=age
			x=datetime.datetime.now()
			date=x.strftime("%x")
			
			t=datetime.datetime.now()
			time=t.strftime("%X")
			reg=int(date.replace("/","")+ time.replace(":",""))
			name=name.ljust(20," ")

			pd=Personal_data(reg,name,phnno,emgno,age,gender,bloodtype,weight,height,date)
			############################################################################################
			print("---MEDICAL DATA---")

			s=Input()                     #symptoms and severity
			
			#symm=symm.ljust(15," ")
			symptoms=s.get_symptoms()   
			medical_details="Null"
			v=Input()
			severity=v.get_severity(age,symptoms)
			symptoms=symptoms.ljust(15," ")
			date_of_discharge="Null"
			discharge_comment="Null"
			d_and_t_of_death="Null"

			med=Medical_data(reg,name,symptoms,medical_details,severity,date_of_discharge,discharge_comment,d_and_t_of_death)

			rec=Record()
			rec.add_patient(pd,med)


	def get_symptoms(self):
		print("select the symptoms from the following: ")
		print(''' 1->fever\n 2->headache\n 3->fatigue\n 4->runny_nose/styffy nose\n 5->Sore throat\n 6->cough\n 7->Shortness of Breath\n 8->Bluish lip\n 9->Constant pain/pressure in chest\n 10->Sneezing''')
		f=int(input())
		if f==1:
			symm="Fever"
		elif f==2:
			symm="Headache"

		elif f==3:
			symm="Fatigue"
		elif f==4:
			symm="Runny_nose"

		elif f==5:
			symm="SoreThroat"

		elif f==6:
			symm="Cough"

		elif f==7:
			symm="Shortness of Breath"

		elif f==8:
			symm="Bluish lip/face"
		elif f==9:
			symm="Constant pain"
		else:
			symm="Sneezing"
		return symm

	def get_severity(self,age,symm):
		com=["Fever","Headache","Fatigue","Runny_nose","SoreThroat","Cough","Sneezing"]
		if symm in com and age<=45:
			sev="Mild"

		else:
			sev="Emergency"
		return sev


'''
		if (sym=="Fever") or (sym=="Headache") or (sym=="Fatigue") or (sym=="Runny_nose") or (sym=="SoreThroat") or (sym=="Cough") or (sym=="Sneezing"):
			if age<=45:
				sev="Mild"
			else:
				sev="Emergency"
			print(sev)
			return sev
'''