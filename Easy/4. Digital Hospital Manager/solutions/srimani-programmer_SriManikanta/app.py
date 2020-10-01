import sqlite3
from random import randint
from datetime import datetime

class Application:

    def __init__(self):
        self.connection = sqlite3.connect('patientDB.db')
        self.cursor = self.connection.cursor()

    def createPatientRecord(self, patient_name, patient_phone_number, patient_emergency_number, patient_age, patient_gender, patient_blood_type, patient_weight, patient_hieght, patient_symptoms):
        # Creating Table
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS patients
        (patient_id TEXT PRIMARY KEY,
         patient_name TEXT NOT NULL,
         patient_phone TEXT NOT NULL,
         patient_emergency TEXT NOT NULL,
         patient_age INTEGER NOT NULL,
         patient_gender TEXT NOT NULL,
         patient_blood_group TEXT NOT NULL,
         patient_weight REAL NOT NULL,
         patient_height REAL NOT NULL,
         patient_symptoms TEXT NOT NULL,
         date_of_register REAL NOT NULL
        )''')
        patient_id = 'PTCOVID' + str(randint(2134324324, 9968867768))
        

        self.cursor.execute('''INSERT INTO patients
        (patient_id, patient_name, patient_phone, patient_emergency, patient_age, patient_gender, patient_blood_group, patient_weight, patient_height, patient_symptoms, date_of_register)
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, date('now'))
        ''', 
        (patient_id, patient_name, patient_phone_number, patient_emergency_number, patient_age, patient_gender, patient_blood_type, patient_weight, patient_hieght, patient_symptoms))
        self.connection.commit()

    def fetchPatientDetails(self):
        results = self.cursor.execute('SELECT * FROM patients').fetchall()
        if(len(results) > 0):
            print("Total Number of Patients Admitted in Hospital are: {}".format(len(results)))
            print("******************************** Admitted Patient Details ********************************")
            print("Patient_Id  Patient_Name  Patient_Phone_Number  Patient_Emergency_Contact  Patient_Age  Patient_Gender  Patient_Blood_Group  Patient_Weight  Patient_Height  Patient_Symptoms  DateOFAdmit")

            for data in results:
                print('{}    {}    {}    {}    {}    {}    {}    {}    {}    {}    {}'.format(data[0], data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10]))

        else:
            print("No Patients are Admitted in the Hospital")
    
    def __del__(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    app = Application()
    while True:
        app_choice = None
        try:
            app_choice = int(input("Select the Option to Work with the App:\n 1. Patient Record Register\n 2. Fetch Patient Statistics\n 3. Quit\n Enter your Choice: "))
        except ValueError:
            print("Please enter a valid Option.!")
            continue

        if(app_choice == 1):
            while True:
                print("Enter the Patient Admit Details")
                name = input("Enter the patient full name: ")
                phone = input("Enter patient phone number: ")
                emergency = input("Enter Patient Emergency Contact: ")
                # Taking the Age Input
                age = None
                while True:
                    try:
                        age = int(input("Enter the patient Age: "))
                        break
                    except ValueError:
                        print("please enter a valid age.!")
                        continue
                
                genderList = ["Male", "Female", "Others"]
                gender = None
                while True:
                    try:
                        genderOption = int(input("Enter the patient gender:\n 1. Male\n 2. Female\n 3. Others\n Choose a Valid Gender Option: "))
                        if(genderOption >= 1 and genderOption <= 3):
                            gender = genderList[genderOption -  1]
                            break
                        else:
                            print("Please enter a valid gender Option from the list")
                            continue
                    except ValueError:
                        print("Please select the valod gender Option")
                        continue
                blood_list = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
                blood_group = None
                while True:
                    try:
                        blood_option = int(input("Select the patient Blood Group from the list:\n 1. A+ \n 2. A- \n 3. B+\n 4. B-\n 5. AB+\n 6. AB-\n 7.O+\n 8. O-\n Select Option:"))
                        if(blood_option >= 1 and blood_option <= 8):
                            blood_group = blood_list[blood_option - 1]
                            break
                        else:
                            print("Please enter a valid given blood group Option")
                            continue
                    except ValueError:
                        print('Please enter a valid Option')
                        continue
                
                weight = None
                while True:
                    try:
                        weight = int(input("Enter the patient Weight in Kilograms: "))
                        break
                    except ValueError:
                        print("please enter a valid Weight Value.!")
                        continue
            
                height = None
                while True:
                    try:
                        height = int(input("Enter the patient height in centimeters: "))
                        break
                    except ValueError:
                        print("please enter a valid height Value.!")
                        continue
                symptoms = input("Enter the patient details or Medical Details: ")

                app.createPatientRecord(name, phone, emergency, age, gender, blood_group, weight, height, symptoms)
                intimation = None
                while True:
                    intimation = input("Do yo want to register a new patient Record [y/n]")
                    if(intimation.lower() == 'y' or intimation.lower() == 'n'):
                        break
                    else:
                        print("Please enter a valid option i.e either y/n")
                        continue
                if(intimation.lower() == 'y'):
                    continue
                elif(intimation.lower() == 'n'):
                    break
        elif (app_choice == 2):
            app.fetchPatientDetails()
        elif (app_choice == 3):
            print("Thanks for Using our Application")
            break






