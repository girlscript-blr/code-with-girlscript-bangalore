import datetime
from patients import patients
from record import record
while True:
	print("----------------------------------------------------------------------")
	print("Hello, select a number from given description to perform operation : ")
	print(''' 1 -> enter details of patient/patients \n 2-> show current status of database\n 3-> show details of patients added on certain date \n 4-> Delete a patient's record \n 5-> exit ''' )
	q=int(input())

	if q==1:
		n=int(input("Enter number of patients to be added in databases: "))
		for i in range(n):
			print("Enter details of patient: ",i+1)
			name=input("Enter name of patient: ")
			phnno=int(input("Enter Contact number: "))
			emgno=int(input("Enter Emergency contact number: "))
			age=int(input("Enter age of patient: "))
			gender=input("Enter Gender: ")
			bloodtype=input("Enter bloood type of patient: ")
			weight=int(input("Enter weight of patient: "))
			height=int(input("Enter height of patient: "))
			symptoms=input("Enter symptoms of patient: ")

			x=datetime.datetime.now()
			date=x.strftime("%x")
			t=datetime.datetime.now()
			time=t.strftime("%X")
			reg=int(date.replace("/","")+ time.replace(":",""))
			name=name.ljust(20," ")
			symptoms=symptoms.ljust(15," ")

			pat=patients(reg,name,phnno,emgno,age,gender,bloodtype,weight,height,symptoms,date)
			rec=record()
			rec.add_patient(pat)
			print()

	elif q==2:
		obj=record()
		obj.show_all()
		print()

	elif q==3:
		d=input("enter date in given format MM/DD/YY : \n")
		obj=record()
		obj.showby_date(d)
		print()

	elif q==4:
		num=int(input("enter id of the patient: "))
		obj=record()
		obj.remove_patient(num)
		print("record of the patient deleted!\n")

	elif q==5:
		print("Thanks!")
		break
	else:
		print("enter valid code")
		print()


