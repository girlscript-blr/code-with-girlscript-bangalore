import sqlite3
from sqlite3.dbapi2 import connect



class Patient:

    def __init__(self):

        self.connection = sqlite3.connect('patientDB.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS patients
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         phone TEXT NOT NULL,
         e_cont TEXT NOT NULL,
         age INTEGER NOT NULL,
         gender TEXT NOT NULL,
         blood_group TEXT NOT NULL,
         weight REAL NOT NULL,
         height REAL NOT NULL,
         symptoms TEXT NOT NULL,
         reg_date REAL NOT NULL
        )''')

    def get_info(self):
        
        self.name = str(input("ENTER YOUR FULL NAME : "))
        self.ph_num = str(input("ENTER YOUR PHONE NUMBER : "))
        self.e_contact = str(input("ENTER YOUR EMERGENCY CONTACT NUMBER : "))
        self.age = int(input("ENTER YOUR AGE: "))


        print(" GENDER : \n 1 MALE \n 2 FEMALE \n 3 OTHER")

        while True:
            self.gender = int(input("ENTER THE CORRESPONDING NUMBER : "))

            if self.gender in [1,2,3]:
                break
            else:
                print("INVALID NUMBER!")

        while True:
            self.blood_gp = str(input("ENTER YOUR BLODD TYPE OUT OF : [A, A+, A-, B, B+, B-, O+, O-, AB+, AB-] : "))

            if self.blood_gp in ['A', 'A+', 'A-', 'B', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']:
                break
            else:
                print("INVALID BLOOD GROUP. \n TRY AGAIN.")

        
        while True:
            try:
                self.weight = int(input("ENTER THE PATIENT WEIGHT IN KILOGRAMS: "))
                break
            except ValueError:
                print("ENTER VALID WEIGHT")
    

        while True:
            try:
                self.height = int(input("ENTER THE PATIENT HEIGHT IN CENTIMETERS: "))
                break
            except ValueError:
                print("INVALID HEIGHT. \n TRY AGAIN.")
              

        self.symptoms = input("ENTER THE PATIENT DETAILS OR MEDICAL DETAILS: ")

    def print_info(self):
        print("NAME - " + self.name)
        print("CONTACT - " + str(self.ph_num))
        print("EMERGENCY CONTACT - " + self.e_contact)

        if self.gender == 1 :
            print("GENDER - MALE")
        elif self.gender == 2 :
            print("GENDER - FEMALE")
        if self.gender == 3 :
            print("GENDER - OTHER")

        print("HEIGHT - " + str(self.height))
        print("WEIGHT - " + str(self.weight))
        print("SYMPTOMS - " + str(self.symptoms))


    def save_data(self):

        self.cursor.execute('''INSERT INTO patients
        (id, name, phone, e_cont, age, gender, blood_group, weight, height, symptoms, reg_date)
        VALUES
        (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, date('now'))
        ''', 
        (self.name, self.ph_num, self.e_contact, self.age, self.gender, self.blood_gp, self.weight, self.height, self.symptoms))
        self.connection.commit()

        self.connection.close()


            




        
if __name__ == "__main__":
    print("-----------GIRLSCRIPT OCTOBER EASY PROBLEM-----------")

    while True:
        choice = int(input('''
            1. ENTER PATIENT DETAILS
            2. FETCH PATIENT DETAILS
            3. QUIT
        '''))   

        if choice == 1:
            p = Patient()
            p.get_info()
            p.print_info()
            p.save_data()
        elif choice == 2:
            connection = sqlite3.connect('patientDB.db')
            cursor = connection.cursor()
            

            results = cursor.execute('SELECT * FROM patients').fetchall()
            if(len(results) > 0):
                print("TOTAL NUMBER OF PATIENTS ADMITTED IN HOSPITAL ARE: {}".format(len(results)))

                print("-------------------------- ADMITTED PATIENT DETAILS --------------------------")
               
                for data in results:
                    print('{}   {}      {}      {}      {}      {}      {}      {}      {}      {}      {}'.format(data[0], data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10]))


            connection.close()


        elif choice == 3:
            break
        else:
            print("INVALID OUTPUT")

            





                
        