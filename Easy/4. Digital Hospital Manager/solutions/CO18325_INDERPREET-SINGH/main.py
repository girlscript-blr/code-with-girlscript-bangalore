class Patient:

    def get_info(self):
        
        self.name = str(input("ENTER YOUR FULL NAME : "))
        self.ph_num = str(input("ENTER YOUR PHONE NUMBER : "))
        self.e_contact = str(input("ENTER YOUR EMERGENCY CONTACT NUMBER : "))
        self.age = int("ENTER YOUR AGE: ")


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
                



        
        



                
        