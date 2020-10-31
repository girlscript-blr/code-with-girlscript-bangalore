from Record import Record
from Input import Input
import datetime

while True:
	print("----------------------------------------------------------------------")
	print("Hello, select a number from given description to perform operation : ")
	print(''' 1 -> Add Patients/Patients \n 2-> Display all \n 3-> Update Patient\n 4-> Get status of patient by ID\n 5-> View Statistics\n 6-> Delete a patient's record from database\n 7->Exit'''  )
	q=int(input())

	if q==1:
		ip=Input()
		ip.get_input()

	elif q==2:
		rec=Record()
		rec.show_all()

	elif q==3:
		ide=input(" Enter Id of the patient: ")
		n=int(input(" Select the Column that is to be updated:\n 1->Medical Details\n 2->Discharge Date\n 3->Discharge Comment "))
		r=Record()
		if n==1:
			st=input(" Enter updated Details: ")
			r.update_medicaldetails(ide,st)
		elif n==2:
			st=input(" Enter Discharge Date in format-> MM/DD/YY (including '/'): ")
			r.update_dischargedate(ide,st)

		else:
			no=int(input(" Select discharge comment 1->Cured or 2->Deceased: "))
			if no==1:
				r.update_cure(ide,"Cured")
			else:
				date_of_death=input("Enter Date of death in format-> MM/DD/YY (including '/'): ")
				time_of_death=input("Enter Time of death in format-> HH:MM:SS (including ':'): ")
				fin=date_of_death+" "+time_of_death
				r.update_deceased(ide,"Deceased",fin)

	elif q==4:
		ide=int(input("Enter ID of patient whose status needs to be checked: "))
		r=Record()
		r.show_by_id(ide)


	elif q==5:
		num=int(input("Select from the following:\n 1->Total patients admitted on the current date\n 2->Total patients discharged on the current date\n 3->Total number of patients in hospital at the current time\n"))
		x=datetime.datetime.now()
		date=x.strftime("%x")
		r=Record()
		if num==1:
			r.count_admission_date(date)
		elif num==2:
			r.count_discharge_date(date)
		elif num==3:
			r.count_all()
		else:
			print("ERROR , enter valid input ")
			break

	elif q==6:
		ide=int(input("Enter Id of patient whose record is to be deleted: "))
		r=Record()
		r.delete(ide)

	else:
		print("Thanks!")
		break
		
