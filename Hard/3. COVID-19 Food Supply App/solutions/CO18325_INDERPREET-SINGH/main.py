import sqlite3
import random
import sys


class App:

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        
        self.cateoryList = [
            ("Inf", "Infants"),
            ("Chd", "Childern"),
            ("old", "Old Age"),
            ("Adf", "Adult Female"),
            ("Adm", "Adult Male"),
            ("Ado", "Adult Other"),
        ]

        self.genderList = ["Male", "Female", "Other"]


    def add_slum_record(self,slum_name, slum_description):
        
        uniqueId = 'SLMP' + str(random.randint(433242324, 734324243))
        
        # Creation of Slum table
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS slum_data(
            s_id TEXT NOT NULL PRIMARY KEY, 
            s_name TEXT NOT NULL,
            s_desc TEXT NOT NULL
        )''')

        self.cursor.execute(''' INSERT INTO slum_data(s_id, s_name, s_desc) VALUES (?,?,?)''', 
        (uniqueId, slum_name.strip().capitalize(), slum_description.strip().capitalize()))

        self.conn.commit()


    def update_slum_record(self, slum_name, slum_description):



        entries = self.cursor.execute("SELECT s_name FROM slum_data").fetchall()

        for i in entries:

            if (i[0].strip().capitalize() ==  slum_name.strip().capitalize()):
                # Updating the Records
                self.cursor.execute('''UPDATE slum_data
                SET s_desc=? WHERE s_name=?
                ''', ( slum_description.strip().capitalize(), slum_name.strip().capitalize()))
                
                self.conn.commit()
                
  


    # Fetching the food product Details
    def fetch_food_product_results(self):
        result = self.cursor.execute("SELECT * FROM food_products").fetchall()

        print("     Food Product        Id      Item name       Item Quantity           Item Price")
        for item in result:
            print("           {}        {}      {}              {}         ".format(item[0], item[1],item[2],int(item[3])))




    # Fetching the Special Item Details
    def fetch_special_items(self):
        details = self.cursor.execute('SELECT * FROM special_items').fetchall()
        
        for item in details:
            print(item)

    # Registering the Survey
    def register_survey(self, aadhar_number, name, gender, age, slum_area, rice_quantity, dal_quantity, sp1, sp2):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS 
        survey_data(
        aadhar TEXT NOT NULL,
        name TEXT NOT NULL,
        gender TEXT NOT NULL,
        age TEXT NOT NULL,
        slum_area TEXT NOT NULL,
        rice_quantity INTEGER NOT NULL,
        dal_quantity INTEGER NOT NULL,
        sp_item1 TEXT NOT NULL,
        special_item2 TEXT NOT NULL
        )''')

        # try:
        survey_results = self.cursor.execute('SELECT aadhar FROM survey_data').fetchall()
        for data in survey_results:
            if(data[0] == aadhar_number):
                print("SURVEY ALREADY TAKEN BY THE CUSTOMER!!")
                break
        
        self.cursor.execute('''INSERT INTO survey_data(
            aadhar,
            `name`,
            gender,
            age,
            slum_area,
            rice_quantity,
            dal_quantity,
            special_item1,
            special_item2
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (aadhar_number, name, gender, age, slum_area, rice_quantity, dal_quantity, sp1, sp2))
        self.conn.commit()
        print("THANKS TO PROVIDE US THE REQUIRED INFORMATION!!")
        # except Exception:
        #     print("ERROR : UNABLE TO REGISTER THE USER!!")
        #     sys.exit(0)

    # Calculating the final Survey Sheet
    def generate_final_survey_sheet(self, area_name):
        infantAgeCount = 0
        childernAgeCount = 0
        oldAgeCount = 0
        adultFemaleCount  = 0
        adultMaleCount = 0
        adultOtherCount = 0

        age_results = self.cursor.execute("SELECT age, gender FROM survey_data WHERE slum_area=?",(area_name,)).fetchall()

        for age in age_results:
            finalAge = int(age[0])
            if(finalAge <= 2):
                infantAgeCount += 1
            elif (finalAge >= 3 and finalAge < 18):
                childernAgeCount += 1
            elif (finalAge > 70):
                oldAgeCount += 1
            elif (finalAge >= 18 and finalAge < 69 and age[1] == "Male"):
                adultMaleCount += 1
            elif (finalAge >= 18 and finalAge < 69 and age[1] == "Female"):
                adultFemaleCount += 1
            elif (finalAge >= 18 and finalAge < 69 and age[1] == "Other"):
                adultOtherCount += 1
        
        print("############################################# OVERALL SURVEY REPORT #############################################")
        print("\t\t Personal Information")
        print("\t\t Age Group\t\t No.Of People")
        print("\t\t Infants: Below 2years: {}".format(infantAgeCount))
        print("\t\t Children: Between 3 to 18 years: {}".format(childernAgeCount))
        print("\t\t Old Age: Above 70 years: {}".format(oldAgeCount))
        print("\t\t Adult Female: Between 18 to 69 years: {}".format(adultFemaleCount))
        print("\t\t Adult Male: Between 18 to 69 years: {}".format(adultMaleCount))
        print("\t\t Adult Other: Between 18 to 69 years: {}".format(adultOtherCount))

        # Quntity Values
        riceInKgPerDay = 0.0
        dalInKgPerDay = 0.0
        cerelacCount = 0
        amulPowderCount = 0
        nandiniMilkItemCount = 0
        breadCount = 0
        tigerOrParle_G_Count = 0
        cannedVeggiesCount = 0
        cannedFruitsCount = 0
        medicinePackCount = 0
        calcimSandozTabletCount = 0

        # Items Cost Overall Result
        riceOverallResult = 0
        dalOverallResult = 0
        cerelacOverallResult = 0
        amulPowderOverallResult = 0
        nandiniOverallResult = 0
        breadOverallResult = 0
        tigerOverallResult = 0
        cannedVeggiesOverallResult = 0
        cannedFruitsOverallResult = 0
        medicinePacksOverallResult = 0
        calciumandozOverallResult = 0
        totalAmount = 0

        # Mobthly Quantity
        riceMonthlyQuantity = 0
        dalMonthlyQuantity = 0
        cerelacMonthlyQuantity = 0
        amulPowderMonthlyQuantity = 0
        nandhiniMilkMonthlyQuantity = 0
        breadMonthlyQuantity = 0
        tigerParleMonthlyQuantity = 0
        cannedVeggiesMonthlyQuantity = 0
        cannedFruitsMonthlyQuantity = 0
        medicinePackMonthlyQuantity = 0
        calciumSandozMonthlyQuantity = 0
        

        registered_items = self.cursor.execute('SELECT * FROM survey_data WHERE slum_area=?', (area_name, ))
        
        # Calculating the Rice and Dal Quantity for all the Slum
        for item in registered_items:
            riceInKgPerDay = riceInKgPerDay + (item[5]/1000)
            dalInKgPerDay = dalInKgPerDay + (item[6] / 1000)
        
        registered_items = self.cursor.execute('SELECT * FROM survey_data WHERE slum_area=?', (area_name, ))
        #registered_items = list(registered_items)
        # print(registered_items)
        for item in registered_items:
            if(item[7].casefold() == "Cerelac".casefold() or item[8].casefold() == "Cerelac".casefold()):
                cerelacCount += 1
            elif(item[7].casefold() == "Amul powder".casefold() or item[8].casefold() == "Amul powder".casefold()):
                amulPowderCount += 1
            elif (item[7].casefold() == "Nandini milk tetrapacks".casefold() or item[8].casefold() == "Nandini milk tetrapacks".casefold()):
                nandiniMilkItemCount += 1
            elif (item[7].casefold() == "Bread".casefold() or item[8].casefold() == "Bread".casefold()):
                breadCount += 1
            elif (item[7].casefold() == "Canned fruits".casefold() or item[8].casefold() == "Canned fruits".casefold()):
                cannedFruitsCount += 1
            elif (item[7].casefold() == "Canned veggies".casefold() or item[8].casefold() == "Canned veggies".casefold()):
                cannedVeggiesCount += 1
            elif (item[7].casefold() == "Calcium sandoz tablets".casefold() or item[8].casefold() == "Calcium sandoz tablets".casefold()):
                calcimSandozTabletCount += 1
            elif (item[7] == "Medicine Packs".casefold()):
                medicinePackCount += 1
            elif (item[7] == "Tiger/parle g".casefold() or item[8] == "Tiger/parle g".casefold()):
                tigerOrParle_G_Count  += 1


        product_details = self.cursor.execute('SELECT * FROM food_products').fetchall()

        for item in product_details:
            if (item[1].casefold() == "Rice 1Kg".casefold()):
                riceOverallResult = riceOverallResult + (riceInKgPerDay * item[2] * item[3])
                riceMonthlyQuantity = item[2]
            elif (item[1].casefold() == "Dal 1Kg".casefold()):
                dalOverallResult = dalOverallResult + (dalInKgPerDay * item[2] * item[3])
                dalMonthlyQuantity = item[2]
        product_details = self.cursor.execute('SELECT * FROM sp_item_det').fetchall()

        for item in product_details:
            if(item[0].casefold() == "Cerelac".casefold()):
                cerelacOverallResult = cerelacOverallResult + (cerelacCount * item[1] * item[2])
                cerelacMonthlyQuantity = item[1]
            elif(item[0].casefold() == "Amul".casefold()):
                amulPowderOverallResult = amulPowderOverallResult + (amulPowderCount * item[1] * item[2])
                amulPowderMonthlyQuantity = item[1]
            elif (item[0].casefold() == "Nandini milk tetrapacks".casefold()):
                nandiniOverallResult = nandiniOverallResult + (nandiniMilkItemCount * item[1] * item[2])
                nandhiniMilkMonthlyQuantity = item[1]
            elif (item[0].casefold() == "Bread".casefold()):
                breadOverallResult = breadOverallResult + (breadCount * item[1] * item[2])
                breadMonthlyQuantity = item[1]
            elif (item[0].casefold() == "Canned fruits".casefold()):
                cannedFruitsOverallResult = cannedFruitsOverallResult + (cannedFruitsCount * item[1] * item[2])
                cannedFruitsMonthlyQuantity = item[1]
            elif (item[0].casefold() == "Canned veggies".casefold()):
                cannedVeggiesOverallResult = cannedVeggiesOverallResult + (cannedVeggiesCount * item[1] * item[2])
                cannedVeggiesMonthlyQuantity = item[1]
            elif (item[0].casefold() == "Calcium sandoz tablets".casefold()):
                calciumandozOverallResult = calciumandozOverallResult + (calcimSandozTabletCount * item[1] * item[2])
                calciumSandozMonthlyQuantity = item[1]
            elif (item[0].casefold() == "Medicine Packs".casefold()):
                medicinePacksOverallResult = medicinePacksOverallResult + (medicinePackCount * item[1] * item[2])
                medicinePackMonthlyQuantity = item[1]
            elif (item[0].casefold() == "Tiger/parle g".casefold()):
                tigerOverallResult = tigerOverallResult + (tigerOrParle_G_Count * item[1] * item[2])
                tigerParleMonthlyQuantity = item[1]

        
        print("\n")
        # Calculating the Rice Price
        if (riceInKgPerDay > 0):
            totalAmount = totalAmount + riceOverallResult
            print("\t\t RICE IN KG PER DAY: {:.2F} KG : {:.2F} KG : {:.2F}".format(riceInKgPerDay, riceMonthlyQuantity, riceOverallResult))

        # Calculating the Dal Price
        if (dalInKgPerDay > 0):
            totalAmount += dalOverallResult
            print("\t\t DAL IN KG PER DAY: {:.2F} KG : {:.2F} KG : {:.2F}".format(dalInKgPerDay, dalMonthlyQuantity, dalOverallResult))

        # Calculating the Cerelac Items
        if (cerelacCount > 0):
            totalAmount += cerelacOverallResult
            print("\t\t Cerelac: {} : {} : {}".format(cerelacCount, cerelacMonthlyQuantity, cerelacOverallResult))

        # Amul Powder Calculation
        if (amulPowderCount > 0):
            totalAmount += amulPowderOverallResult
            print("\t\t Amul powder : {} : {} : {}".format(amulPowderCount, amulPowderMonthlyQuantity, amulPowderOverallResult))

        # Nandini Milk Tetrapacks Calculation
        if (nandiniMilkItemCount > 0):
            totalAmount += nandiniOverallResult
            print("\t\t Nandini Milk TetraPacks: {} : {} : {}".format(nandiniMilkItemCount, nandhiniMilkMonthlyQuantity, nandiniOverallResult))

        # Bread Calculation
        if (breadCount > 0):
            totalAmount += breadOverallResult
            print("\t\t Bread: {} : {} : {}".format(breadCount, breadMonthlyQuantity, breadOverallResult))

        # Tiger Parle G Biscuit calculation
        if (tigerOrParle_G_Count > 0):
            totalAmount += tigerOverallResult
            print("\t\t Tiger/Parle G Biscuits: {} : {} : {}".format(tigerOrParle_G_Count, tigerParleMonthlyQuantity, tigerOverallResult))

        # Canned Veggies Calculation
        if (cannedVeggiesCount > 0):
            totalAmount += cannedVeggiesOverallResult
            print("\t\t Canned Veggies: {} : {} : {}".format(cannedVeggiesCount, cannedVeggiesMonthlyQuantity, cannedVeggiesOverallResult))

        # Canned Fruits Calculation
        if (cannedFruitsCount > 0):
            totalAmount += cannedFruitsOverallResult
            print("\t\t Canned Fruits: {} : {} : {}".format(cannedFruitsCount, cannedFruitsMonthlyQuantity, cannedFruitsOverallResult))

        # Medicine Packs Calculation
        if (medicinePackCount > 0):
            totalAmount += medicinePacksOverallResult
            print("\t\t Medicine Packs: {} : {} : {}".format(medicinePackCount, medicinePackMonthlyQuantity, medicinePacksOverallResult))

        # Calcium Sandoz Calculation
        if (calcimSandozTabletCount > 0):
            totalAmount += calciumandozOverallResult
            print("\t\t Rice in Kg per day: {} : {} : {}".format(calcimSandozTabletCount, calciumSandozMonthlyQuantity, calciumandozOverallResult))

        print("Total Amount Required: {:.2f}".format(totalAmount)) 
    
    def get_slum_names(self):
        print("SLUM LIST: ")
        result = self.cursor.execute("SELECT s_name FROM slum_data").fetchall()
        for index, slum in enumerate(result):
            print(str(index) + "---" + slum[0])
        
        while True:
            ind = int(input("ENTER THE CORRESPONDING INDEX NUMBER TO THE SLUM SELECTED : "))
            if ind >= 0 and ind < len(result):
                break
            else:
                print("Enter a valid Number!!")
        return result[ind]

    # Destructor
    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":

    app = App()

    while True:
        try:
            # Admin Work
            while True:
                userChoice = int(input("Enter your option to work\n 1. Admin\n 2. Survey Taker\n 3. quit\n Your Option: "))
               
#######################################################################################################################################

                if(userChoice == 1):
                    while True:
                        try:
                            adminWork = int(input('''ENTER YOU OPTION\n 
                            0. ADD SLUM RECORD\n
                            1. UPDATE SLUM RECORD\n
                            2. FETCH FOOD INFORMATION\n 
                            3. FETCH THE FOOD PRODUCT DETAILS\n 
                            4. FETCH SPECIAL ITEMS DETAILS\n
                            5. QUIT \n 
                            YOUR CHOICE:
                            '''))

                            if adminWork == 0:
                                slum_name = input("ENTER THE NEW SLUM NAME: ")
                                # print(slum_name)
                                slum_description = input("ENTER THE SLUM DESCRIPTION: ")
                                app.add_slum_record(slum_name, slum_description)
                            if(adminWork == 1):
                                slum_name = app.get_slum_names()[0]
                                # print(slum_name)
                                slum_description = input("ENTER THE SLUM DESCRIPTION: ")
                                app.update_slum_record(slum_name, slum_description)
                                                    
                            elif (adminWork == 2):
                                slum_name =app.get_slum_names()[0]
                                app.generate_final_survey_sheet(slum_name)

                            elif (adminWork == 3):
                                app.fetch_food_product_results()

                            elif (adminWork == 4):
                                app.fetch_special_items()

                            elif(adminWork == 5):
                                print("THANKS FOR USING THE APPLICATION.!")
                                sys.exit(0)  

                        except ValueError:
                            print("ENTER A VALID OPTION.!")
                            continue



######################################################################################################################################

                elif(userChoice == 2):
                    while True:
                        try:
                            survey_choice = int(input('''SELECT YOUR CHOICE:\n 
                            1. REGISTER SURVEY\n 
                            2. FETCH FOOD INFORMATION BY AADHAR NUMBER\n 
                            3. QUIT\n 
                            SELECT YOUR OPTION:'''))


                            ################################# REGISTER A USER ##############################################
                            if(survey_choice ==  1):
                                # Aadhar Number
                                person_aadhar = None
                                while True:
                                    person_aadhar = input("ENTER THE PERSON AADHAR NUMBER: ")
                                    if(person_aadhar.isdigit()):
                                        break
                                    else:
                                        print("PLEASE ENTER A VALID AADHAR NUMBER.!")
                                        continue
                                
                                # print(person_aadhar)
                                # Person name
                                person_name = input("ENTER THE PERSON NAME AS PER THE AADHAR RECORDS:")

                                # print(person_name)
                                # Person Gender
                                gender_choice = None
                                while True:
                                    try:
                                        gender_choice = int(input('''ENTER YOUR GENDER CHOICE:\n 
                                        1. MALE\n
                                        2. FEMALE\n 
                                        3. OTHER\n 
                                        SELECT YOUR OPTION:'''))
                                        if(gender_choice <= 0 or gender_choice > 3):
                                            print("PLEASE ENTER A VALID GENDER CHOICE AVAILABLE IN THE LIST.!")
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        print("PLEASE ENTER A VALID CHOICE.!")
                                        continue
                                person_gender = app.genderList[gender_choice - 1]

                                # print(person_gender)
                                # Person Age
                                person_age = None
                                while True:
                                    person_age = input("ENTER THE PERSON AGE: ")

                                    if(person_age.isdecimal()):
                                        person_age = int(person_age)
                                        break
                                    else:
                                        print("PLEASE ENTER A VALID AGE.!")
                                        continue
                                
                               
                                person_slum_name = app.get_slum_names()[0]
                                print(person_slum_name)

                               
                                # print(person_slum_name)
                                # Rice Eat Value
                                person_rice_eat = int(input("ENTER HOW MUCH RICE IN GRAMS HE/SHE EATS PER DAY?: "))

                                # Dal Eat Value
                                person_dal_eat = int(input("ENTER HOW MUCH DAL IN GRAMS HE/SHE EATS PER DAY?: "))

                                print(person_rice_eat, person_dal_eat)

                                # Special Items Selection
                                sp_item1 = ""
                                special_item2 = ""
                            
                                if(person_age <= 2):
                                    sp_items = list(app.cursor.execute('SELECT c_item FROM special_items WHERE c_id=?',(app.cateoryList[0][0],)).fetchall())
                                    
                                    print("CHOOSE THE OPTIONS FROM THE BELOW LIST")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    
                                    while True:
                                        try:
                                            sp_c1 = int(input("ENTER YOUR FOOD ITEM OPTION NUMBER FROM THE ABOVE LIST:"))
                                            if(sp_c1 <= len(sp_items) and sp_c1 > 0):
                                                sp_item1 = sp_items[sp_c1 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_c2 = int(input("ENTER YOU FOOD ITEM OPTION NUMBER FROM THE ABOVE LIST:"))
                                            if(sp_c2 <= len(sp_items) and sp_c2 > 0):
                                                special_item2 = sp_items[sp_c2 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                elif(person_age >= 3 and person_age < 18):
                                    sp_items = list(app.cursor.execute('SELECT c_item FROM special_items WHERE c_id=?',(app.cateoryList[1][0],)).fetchall())
                                    print("CHOOSE THE OPTIONS FROM THE BELOW LIST")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    
                                    while True:
                                        try:
                                            sp_c1 = int(input("ENTER YOU FOOD ITEM OPTION NUMBER FROM THE ABOVE LIST:"))
                                            if(sp_c1 <= len(sp_items) and sp_c1 > 0):
                                                sp_item1 = sp_items[sp_c1 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_c2 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_c2 <= len(sp_items) and sp_c2 > 0):
                                                special_item2 = sp_items[sp_c2 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                elif(person_age > 70):
                                    sp_items = list(app.cursor.execute('SELECT c_item FROM special_items WHERE c_id=?',(app.cateoryList[2][0],)).fetchall())
                                    print("CHOOSE THE OPTIONS FROM THE BELOW LIST")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    
                                    while True:
                                        try:
                                            sp_c1 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_c1 <= len(sp_items) and sp_c1 > 0):
                                                sp_item1 = sp_items[sp_c1 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_c2 = int(input("ENTER YOU FOOD ITEM OPTION NUMBER FROM THE ABOVE LIST:"))
                                            if(sp_c2 <= len(sp_items) and sp_c2 > 0):
                                                special_item2 = sp_items[sp_c2 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                elif(person_age >= 18 and person_age < 69 and person_gender == "Female"):
                                    sp_items = list(app.cursor.execute('SELECT c_item FROM special_items WHERE c_id=?',(app.cateoryList[3][0],)).fetchall())
                                    print("CHOOSE THE OPTIONS FROM THE BELOW LIST")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    
                                    while True:
                                        try:
                                            sp_c1 = int(input("ENTER YOU FOOD ITEM OPTION NUMBER FROM THE ABOVE LIST:"))
                                            if(sp_c1 <= len(sp_items) and sp_c1 > 0):
                                                sp_item1 = sp_items[sp_c1 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_c2 = int(input("ENTER YOU FOOD ITEM OPTION NUMBER FROM THE ABOVE LIST:"))
                                            if(sp_c2 <= len(sp_items) and sp_c2 > 0):
                                                special_item2 = sp_items[sp_c2 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                elif(person_age >= 18 and person_age < 69 and person_gender == "Male"):
                                    sp_items = list(app.cursor.execute('SELECT c_item FROM special_items WHERE c_id=?',(app.cateoryList[4][0],)).fetchall())
                                    print("CHOOSE THE OPTIONS FROM THE BELOW LIST")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    

                                    while True:
                                        try:
                                            sp_c1 = int(input("ENTER YOU FOOD ITEM OPTION NUMBER FROM THE ABOVE LIST:"))
                                            if(sp_c1 <= len(sp_items)  and sp_c1 > 0):
                                                sp_item1 = sp_items[sp_c1 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_c2 = int(input("ENTER YOU FOOD ITEM OPTION NUMBER FROM THE ABOVE LIST:"))
                                            if(sp_c2 <= len(sp_items) and sp_c2 > 0):
                                                special_item2 = sp_items[sp_c2 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                elif(person_age >= 18 and person_age < 69 and person_gender == "Other"):
                                    sp_items = list(app.cursor.execute('SELECT c_item FROM special_items WHERE c_id=?',(app.cateoryList[5][0],)).fetchall())
                                    print("CHOOSE THE OPTIONS FROM THE BELOW LIST")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    
                                    while True:
                                        try:
                                            sp_c1 = int(input("ENTER YOU FOOD ITEM OPTION NUMBER FROM THE ABOVE LIST:"))
                                            if(sp_c1 <= len(sp_items) and sp_c1 > 0):
                                                sp_item1 = sp_items[sp_c1 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_c2 = int(input("ENTER YOU FOOD ITEM OPTION NUMBER FROM THE ABOVE LIST:"))
                                            if(sp_c2 <= len(sp_items) and sp_c2 > 0):
                                                special_item2 = sp_items[sp_c2 - 1][0]
                                                break
                                            else:
                                                print("PLEASE ENTER A VALID OPTION.!")
                                                continue
                                        except ValueError:
                                            print("PLEASE ENTER A VALID OPTION.!")
                                            continue
                                    
                                # print(sp_item1, special_item2)
                                app.register_survey(person_aadhar, person_name, person_gender, person_age, person_slum_name, person_rice_eat, person_dal_eat, sp_item1.strip().capitalize(), special_item2.strip().capitalize())
                            



                            ######################################## GET USER INFORMATION ###################################
                            
                            elif (survey_choice == 2):

                                aadhar_id = input("ENTER THE AADHAR ID: ")

                                if(aadhar_id.isdigit()):
                                    food_information_results = app.cursor.execute('SELECT * FROM survey_data WHERE aadhar=?', (aadhar_id, )).fetchone()
                                    
                                    if food_information_results is not None:
                                        food_information_results = list(food_information_results)
                                        print("Aadhar Number: {}".format(food_information_results[0]))
                                        print("Person Name: {}".format(food_information_results[1]))
                                        print("Gender: {}".format(food_information_results[2]))
                                        print("Age: {}".format(food_information_results[3]))
                                        print("Slum Name: {}".format(food_information_results[4]))
                                        print("\n*****************************************************************************************************************\n")
                                        print("Food Item                    :   Quantity As Per Survey           :           Monthly Quantity")
                                        print("Rice Quantity                :       {:.2f} KG :                   :               {:.2f} KG".format(food_information_results[5]/1000, ((food_information_results[5]/1000) * 30)))
                                        print("Dal Quantity                 :       {:.2f} KG :                   :               {:.2f} KG".format(food_information_results[6]/1000, ((food_information_results[6]/1000) * 30)))
                                        # print("{}".format(food_information_results[7]))
                                        # print("{}".format(food_information_results[8]))
                                        print("SPECIAL ITEMS : --")
                                             
                                        # print(c_id)
                                        special_item_results = app.cursor.execute('SELECT * FROM sp_item_det').fetchall()
                                        # print(special_item_results)
                                        # print(food_information_results[8].casefold())
                                        for item in special_item_results:
                                            # print(item[0])
                                            # print(food_information_results[8])
                                            if(item[0].casefold() == food_information_results[7].casefold()) or (item[0].casefold() == food_information_results[8].casefold()):
                                                print("{}  - {}(QUANTITY) -  {}(PER MONTH)".format(item[0], item[1], item[2]))
                                            
                                

                                    else:
                                        print("NO PERSON IS REGISTERED WITH THAT AADHAR CARD.!")
                                        
                                    
                            ################################# QUIT OPERATION ######################################################
                                 
                            elif(survey_choice == 3):
                                print("THANKS FOR USING OUR APPLICATION.!")
                                sys.exit(0)

                        except ValueError:
                            print("YOU HAVE ENTERED A WRONG OPTION CHOICE.!")
                            continue
                


###################################################################################################################################                        
                elif(userChoice == 3):
                    print("THANKS FOR USING OUR APPLICATION.!")
                    sys.exit(0)
        
                workOption = input("DO YOU WANT TO CONTINUE AGAIN: [Y/N]")
                if(workOption.lower() == 'y'):
                    continue
                elif(workOption.lower() == 'n'):
                    break
                else:
                    print("YOU HAVE ENTERED THE OUT OF OPTIONS.!")
                    sys.exit(0)
            else:
                print("PLEASE ENTER A VALID OPTION.!")
                continue
        except ValueError:
            print("PLEASE ENTER A VALID OPTION.!")
            continue