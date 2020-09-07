import sqlite3
import random
import sys

class Application:

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cateoryList = [
            ("Inf223232", "Infants"),
            ("Chd656765", "Childern"),
            ("Old765557", "Old Age"),
            ("Adf765465", "Adult Female"),
            ("Adm867654", "Adult Male"),
            ("Ado897543", "Adult Other"),
        ]
        self.genderList = ["Male", "Female", "Other"]

    # Adding/Updating the Slum Records
    def add_or_update_slum_record(self, slum_name, slum_description):
        uniqueId = 'SLMP' + str(random.randint(433242324, 734324243))
        
        # Creation of Slum table
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS slum_data(
            slum_id TEXT NOT NULL PRIMARY KEY, 
            slum_name TEXT NOT NULL,
            slum_desc TEXT NOT NULL
        )''')
        records = self.cursor.execute("SELECT slum_name FROM slum_data").fetchall()
        # print(records)
        for i in records:
            if i[0].strip().capitalize() ==  slum_name.strip().capitalize():
                # Updating the Records
                self.cursor.execute('''UPDATE slum_data
                SET slum_name=?, slum_desc=?
                ''', (slum_name.strip().capitalize(), slum_description.strip().capitalize()))
                return
        
        # Insertion of Data.
        self.cursor.execute(''' INSERT INTO 
        slum_data(slum_id, slum_name, slum_desc) 
        VALUES
        (?,?,?)        
        ''', (uniqueId, slum_name.strip().capitalize(), slum_description.strip().capitalize()))
                

        self.conn.commit()

    # Adding/Updating the Food Products
    def add_or_update_food_product(self, product_name, product_monthly_quantity, product_price):
        
        food_product_id = 'FPDS' + str(random.randint(2323432434, 7786588657))
        # self.cursor.execute('DROP TABLE food_products')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS food_products(
            prod_id TEXT NOT NULL PRIMARY KEY,
            prod_name TEXT NOT NULL,
            prod_monthly_quan INTEGER NOT NULL,
            prod_price REAL NOT NULL
            )''')
        
        results = self.cursor.execute('SELECT prod_name FROM food_products WHERE prod_name=?',(product_name, )).fetchall()

        for item in results:
            if(item[0].strip().capitalize() == product_name.strip().capitalize()):
                self.cursor.execute('''UPDATE food_products
                SET prod_monthly_quan=?, prod_price=?
                ''', (product_monthly_quantity, product_price))
        

        self.cursor.execute('''INSERT INTO food_products
        (prod_id, prod_name, prod_monthly_quan, prod_price)
        VALUES
        (?, ?, ?, ?)
        ''', (food_product_id, product_name, product_monthly_quantity, product_price))
            
        self.conn.commit()

    # Fetching the food product Details
    def fetch_food_product_results(self):
        result = self.cursor.execute("SELECT * FROM food_products").fetchall()

        print("Food Product Id   Item name  Item Quantity  Item Price")
        for item in result:
            print(item[0], item[1], ":", item[2], ":", int(item[3]))

    # Creating the Category Table
    def special_item_category(self):
        # self.cursor.execute('DROP TABLE special_items')
        # self.cursor.execute('DROP TABLE category')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS category
        (category_id TEXT NOT NULL PRIMARY KEY,
        category_name TEXT NOT NULL)
        ''')
        
        self.cursor.executemany('''INSERT INTO 
        category(category_id, category_name)
        VALUES
        (?, ?)
        ''', self.cateoryList)
        self.conn.commit()

    # Adding the Special Category Items
    def add_special_category_items(self, category_id, category_item):
        
        
        # Creating the table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS special_items
                                (category_id TEXT NOT NULL, 
                                category_item TEXT NOT NULL)
                            ''')
        results = self.cursor.execute("SELECT * FROM special_items").fetchall()

        for item in results:
            if(item[0] == category_id and item[1] == category_item):
                print('Item is already added for that category.!')
                return
        
        self.cursor.execute('''INSERT INTO special_items
                                   (category_id, category_item)
                                   VALUES (?, ?)  
                                ''', (category_id, category_item))

        self.conn.commit()

    # Fetching the Special Item Details
    def fetch_special_items(self):
        details = self.cursor.execute('SELECT * FROM special_items').fetchall()
        
        for item in details:
            print(item)

    # Registering the Survey
    def register_survey(self, person_aadhar_number, person_name, person_gender, person_age, person_slum_area, rice_quantity, dal_quantity, sp1, sp2):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS 
        survey_data(
        person_aadhar TEXT NOT NULL,
        person_name TEXT NOT NULL,
        person_gender TEXT NOT NULL,
        person_age TEXT NOT NULL,
        person_slum_area TEXT NOT NULL,
        person_rice_quantity INTEGER NOT NULL,
        person_dal_quantity INTEGER NOT NULL,
        person_special_item1 TEXT NOT NULL,
        person_special_item2 TEXT NOT NULL
        )''')

        try:
            survey_results = self.cursor.execute('SELECT person_aadhar FROM survey_data').fetchall()
            for data in survey_results:
                if(data[0] == person_aadhar_number):
                    print("User had already taken the Survey earlier!")
                    break
            
            self.cursor.execute('''INSERT INTO survey_data(
                person_aadhar,
                person_name,
                person_gender,
                person_age,
                person_slum_area,
                person_rice_quantity,
                person_dal_quantity,
                person_special_item1,
                person_special_item2
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (person_aadhar_number, person_name, person_gender, person_age, person_slum_area, rice_quantity, dal_quantity, sp1, sp2))
            self.conn.commit()
            print("Thank You for taking the Survey!")
        except Exception:
            print("Unable to register the user.!")
            sys.exit(0)

    # Calculating the final Survey Sheet
    def generate_final_survey_sheet(self, area_name):
        infantAgeCount = 0
        childernAgeCount = 0
        oldAgeCount = 0
        adultFemaleCount  = 0
        adultMaleCount = 0
        adultOtherCount = 0

        age_results = self.cursor.execute("SELECT person_age, person_gender FROM survey_data WHERE person_slum_area=?",(area_name,)).fetchall()

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

        registered_items = self.cursor.execute('SELECT * FROM survey_data WHERE person_slum_area=?', (area_name, ))
        
        # Calculating the Rice and Dal Quantity for all the Slum
        for item in registered_items:
            riceInKgPerDay = riceInKgPerDay + (item[5]/1000)
            dalInKgPerDay = dalInKgPerDay + (item[6] / 1000)
        
        registered_items = self.cursor.execute('SELECT * FROM survey_data WHERE person_slum_area=?', (area_name, ))
        #registered_items = list(registered_items)
        # print(registered_items)
        for item in registered_items:
            if(item[7].casefold() == "Cerelac 1 pack".casefold() or item[8].casefold() == "Cerelac 1 pack".casefold()):
                cerelacCount += 1
            elif(item[7].casefold() == "Amul powder 1kg".casefold() or item[8].casefold() == "Amul powder 1kg".casefold()):
                amulPowderCount += 1
            elif (item[7].casefold() == "Nandini milk tetrapacks 1lt".casefold() or item[8].casefold() == "Nandini milk tetrapacks 1lt".casefold()):
                nandiniMilkItemCount += 1
            elif (item[7].casefold() == "Bread loaf 1pack".casefold() or item[8].casefold() == "Bread loaf 1pack".casefold()):
                breadCount += 1
            elif (item[7].casefold() == "Canned fruits".casefold() or item[8].casefold() == "Canned fruits".casefold()):
                cannedFruitsCount += 1
            elif (item[7].casefold() == "Canned veggies".casefold() or item[8].casefold() == "Canned veggies".casefold()):
                cannedVeggiesCount += 1
            elif (item[7].casefold() == "Calcium sandoz tablets".casefold() or item[8].casefold() == "Calcium sandoz tablets".casefold()):
                calcimSandozTabletCount += 1
            elif (item[7] == "Medicine Packs".casefold() or item[8] == "Medicine Packs".casefold()):
                medicinePackCount += 1
            elif (item[7] == "Tiger/parle g biscuits 5pieces pack".casefold() or item[8] == "Tiger/parle g biscuits 5pieces pack".casefold()):
                tigerOrParle_G_Count  += 1

        product_details = self.cursor.execute('SELECT * FROM food_products').fetchall()

        for item in product_details:
            if(item[1].casefold() == "Cerelac 1 pack".casefold()):
                cerelacOverallResult = cerelacOverallResult + (cerelacCount * item[2] * item[3])
                cerelacMonthlyQuantity = item[2]
            elif(item[1].casefold() == "Amul powder 1kg".casefold()):
                amulPowderOverallResult = amulPowderOverallResult + (amulPowderCount * item[2] * item[3])
                amulPowderMonthlyQuantity = item[2]
            elif (item[1].casefold() == "Nandini milk tetrapacks 1lt".casefold()):
                nandiniOverallResult = nandiniOverallResult + (nandiniMilkItemCount * item[2] * item[3])
                nandhiniMilkMonthlyQuantity = item[2]
            elif (item[1].casefold() == "Bread loaf 1pack".casefold()):
                breadOverallResult = breadOverallResult + (breadCount * item[2] * item[3])
                breadMonthlyQuantity = item[2]
            elif (item[1].casefold() == "Canned fruits".casefold()):
                cannedFruitsOverallResult = cannedFruitsOverallResult + (cannedFruitsCount * item[2] * item[3])
                cannedFruitsMonthlyQuantity = item[2]
            elif (item[1].casefold() == "Canned veggies".casefold()):
                cannedVeggiesOverallResult = cannedVeggiesOverallResult + (cannedVeggiesCount * item[2] * item[3])
                cannedVeggiesMonthlyQuantity = item[2]
            elif (item[1].casefold() == "Calcium sandoz tablets".casefold()):
                calciumandozOverallResult = calciumandozOverallResult + (calcimSandozTabletCount * item[2] * item[3])
                calciumSandozMonthlyQuantity = item[2]
            elif (item[1].casefold() == "Medicine Packs".casefold()):
                medicinePacksOverallResult = medicinePacksOverallResult + (medicinePackCount * item[2] * item[3])
                medicinePackMonthlyQuantity = item[2]
            elif (item[1].casefold() == "Tiger/parle g biscuits 5pieces pack".casefold()):
                tigerOverallResult = tigerOverallResult + (tigerOrParle_G_Count * item[2] * item[3])
                tigerParleMonthlyQuantity = item[2]
            elif (item[1].casefold() == "Rice 1Kg".casefold()):
                riceOverallResult = riceOverallResult + (riceInKgPerDay * item[2] * item[3])
                riceMonthlyQuantity = item[2]
            elif (item[1].casefold() == "Dal 1Kg".casefold()):
                dalOverallResult = dalOverallResult + (dalInKgPerDay * item[2] * item[3])
                dalMonthlyQuantity = item[2]
        
        print("\n")
        # Calculating the Rice Price
        if (riceInKgPerDay > 0):
            totalAmount = totalAmount + riceOverallResult
            print("\t\t Rice in Kg per day: {:.2f} KG : {:.2f} KG : {:.2f}".format(riceInKgPerDay, riceMonthlyQuantity, riceOverallResult))

        # Calculating the Dal Price
        if (dalInKgPerDay > 0):
            totalAmount += dalOverallResult
            print("\t\t Dal in Kg per day: {:.2f} KG : {:.2f} KG : {:.2f}".format(dalInKgPerDay, dalMonthlyQuantity, dalOverallResult))

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

    # Destructor
    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    app = Application()
    # app.special_item_category()
    while True:
        try:
            # Admin Work
            while True:
                userChoice = int(input("Enter your option to work\n 1. Admin\n 2. Survey Taker\n 3. quit\n Your Option: "))
               
                if(userChoice == 1):
                    try:
                        adminWork = int(input("Enter you option\n 1. Add/Update Slum Record\n 2. Update Food Products\n 3. Fetch Food Information\n 4. Add/Update Special Items\n 5. Fetch the food product Details\n 6. Fetch Special Items Details\n Your Choice:"))
                        if(adminWork == 1):
                            slum_name = input("Enter the new slum name: ")
                            slum_description = input("Enter the slum description: ")
                            app.add_or_update_slum_record(slum_name, slum_description)
                        elif (adminWork == 2):

                            while True:
                                product_name = input("Enter the food product name: ")
                                product_price = None
                                product_quantity = None
                                
                                # Product Price
                                while True:
                                    try:
                                        product_price = int(input("Enter the product price: "))
                                        if(product_price > 0):
                                            break
                                    except ValueError:
                                        print("Please enter a valid price.!")
                                        continue
                                
                                # Product Qunatity
                                while True:
                                    try:
                                        product_quantity = int(input("Enter the product monthly Qunatity: "))
                                        if(product_quantity > 0):
                                            break
                                        elif (product_quantity <= 0):
                                            print("please enter a proper quantity.!")
                                            continue
                                    except ValueError:
                                        print("Please enter a valid price.!")
                                        continue
                                
                                app.add_or_update_food_product(product_name, product_quantity, product_price)
                                update_choice = input("Do you want to add/update an another food product [y/n]: ")
                                if(update_choice.lower() == 'y'):
                                    continue
                                elif(update_choice.lower() == 'n'):
                                    break
                                else:
                                    break
                        
                        elif (adminWork == 3):
                            slum_name = input("Enter the slum Name: ")
                            app.generate_final_survey_sheet(slum_name)

                        elif (adminWork == 4):
                            while True:
                                try:
                                    special_item_choice = int(input("Select the Option to Add the food Item Category\n 1. Infants\n 2. Childern\n 3. Old Age\n 4. Adult Female\n 5. Adult Male\n 6. Adult Other\n Select your Option:"))
                                    if(special_item_choice == 1):
                                        special_food_item_name = input("Enter your Item Name: ")
                                        app.add_special_category_items(app.cateoryList[0][0], special_food_item_name.strip().capitalize())
                                    elif (special_item_choice == 2):
                                        special_food_item_name = input("Enter your Item Name: ")
                                        app.add_special_category_items(app.cateoryList[1][0], special_food_item_name.strip().capitalize())
                                    elif (special_item_choice == 3):
                                        special_food_item_name = input("Enter your Item Name: ")
                                        app.add_special_category_items(app.cateoryList[2][0], special_food_item_name.strip().capitalize())
                                    elif (special_item_choice == 4):
                                        special_food_item_name = input("Enter your Item Name: ")
                                        app.add_special_category_items(app.cateoryList[3][0], special_food_item_name.strip().capitalize())
                                    elif (special_item_choice == 5):
                                        special_food_item_name = input("Enter your Item Name: ")
                                        app.add_special_category_items(app.cateoryList[4][0], special_food_item_name.strip().capitalize())
                                    elif (special_item_choice == 6):
                                        special_food_item_name = input("Enter your Item Name: ")
                                        app.add_special_category_items(app.cateoryList[5][0], special_food_item_name.strip().capitalize())
                                    else:
                                        print("Please Select a valid Option number.!")
                                        continue
                                    
                                    item_add_choice = input('Do you want to add another Item [y/n]:')
                                    if(item_add_choice.lower() == 'y'):
                                        continue
                                    elif (item_add_choice.lower() == 'n'):
                                        break
                                    else:
                                        print("You have entered the out of options.!")
                                        break

                                except ValueError:
                                    print("please enter a valid Option.!")
                                    continue
                        elif (adminWork == 5):
                            app.fetch_food_product_results()
                        elif (adminWork == 6):
                            app.fetch_special_items()
                    except ValueError:
                        print("Enter a valid Option.!")
                        continue
                elif(userChoice == 2):
                    while True:
                        try:
                            survey_choice = int(input("Select your Choice:\n 1. Register Survey\n 2. Fetch Food Information By Aadhar Number\n 3. Quit\n Select your Option:"))
                            if(survey_choice ==  1):
                                # Aadhar Number
                                person_aadhar = None
                                while True:
                                    person_aadhar = input("Enter the person aadhar number: ")
                                    if(person_aadhar.isdigit()):
                                        break
                                    else:
                                        print("Please enter a valid aadhar number.!")
                                        continue
                                
                                # print(person_aadhar)
                                # Person name
                                person_name = input("Enter the person name as per the aadhar records:")

                                # print(person_name)
                                # Person Gender
                                gender_choice = None
                                while True:
                                    try:
                                        gender_choice = int(input("Enter your gender choice:\n 1. Male\n 2. Female\n 3. Other\n Slect your Option:"))
                                        if(gender_choice <= 0 or gender_choice > 3):
                                            print("please enter a valid gender choice available in the list.!")
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        print("Please enter a valid choice.!")
                                        continue
                                person_gender = app.genderList[gender_choice - 1]

                                # print(person_gender)
                                # Person Age
                                person_age = None
                                while True:
                                    person_age = input("Enter the person Age: ")

                                    if(person_age.isdecimal()):
                                        person_age = int(person_age)
                                        break
                                    else:
                                        print("Please enter a valid age.!")
                                        continue
                                
                                # print(person_age)
                                # Slum Name
                                slum_name_results = app.cursor.execute("SELECT slum_name FROM slum_data").fetchall()
                                slum_list = list()

                                print("**********Slum names**********")
                    
                                for item in slum_name_results:
                                    print(item[0])
                                    slum_list.append(item[0])

                                person_slum_name = None
                                while True:
                                    person_slum_name = input("Enter the person slum name properly from the above list: ")

                                    person_slum_name = person_slum_name.capitalize()
                                    if(person_slum_name in slum_list):
                                        break
                                    else:
                                        print("Please enter a valid slum name that is available in the list")
                                        continue
                                
                                # print(person_slum_name)
                                # Rice Eat Value
                                person_rice_eat = int(input("Enter How much rice in grams he/she eats per day?: "))

                                # Dal Eat Value
                                person_dal_eat = int(input("Enter How much dal in grams he/she eats per day?: "))

                                print(person_rice_eat, person_dal_eat)

                                # Special Items Selection
                                special_item1 = ""
                                special_item2 = ""
                            
                                if(person_age <= 2):
                                    sp_items = list(app.cursor.execute('SELECT category_item FROM special_items WHERE category_id=?',(app.cateoryList[0][0],)).fetchall())
                                    
                                    print("Choose the Options from the below List")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    
                                    while True:
                                        try:
                                            sp_choice1 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice1 <= len(sp_items) and sp_choice1 > 0):
                                                special_item1 = sp_items[sp_choice1 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_choice2 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice2 <= len(sp_items) and sp_choice2 > 0):
                                                special_item2 = sp_items[sp_choice2 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                elif(person_age >= 3 and person_age < 18):
                                    sp_items = list(app.cursor.execute('SELECT category_item FROM special_items WHERE category_id=?',(app.cateoryList[1][0],)).fetchall())
                                    print("Choose the Options from the below List")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    
                                    while True:
                                        try:
                                            sp_choice1 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice1 <= len(sp_items) and sp_choice1 > 0):
                                                special_item1 = sp_items[sp_choice1 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_choice2 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice2 <= len(sp_items) and sp_choice2 > 0):
                                                special_item2 = sp_items[sp_choice2 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                elif(person_age > 70):
                                    sp_items = list(app.cursor.execute('SELECT category_item FROM special_items WHERE category_id=?',(app.cateoryList[2][0],)).fetchall())
                                    print("Choose the Options from the below List")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    
                                    while True:
                                        try:
                                            sp_choice1 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice1 <= len(sp_items) and sp_choice1 > 0):
                                                special_item1 = sp_items[sp_choice1 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_choice2 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice2 <= len(sp_items) and sp_choice2 > 0):
                                                special_item2 = sp_items[sp_choice2 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                elif(person_age >= 18 and person_age < 69 and person_gender == "Female"):
                                    sp_items = list(app.cursor.execute('SELECT category_item FROM special_items WHERE category_id=?',(app.cateoryList[3][0],)).fetchall())
                                    print("Choose the Options from the below List")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    
                                    while True:
                                        try:
                                            sp_choice1 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice1 <= len(sp_items) and sp_choice1 > 0):
                                                special_item1 = sp_items[sp_choice1 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_choice2 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice2 <= len(sp_items) and sp_choice2 > 0):
                                                special_item2 = sp_items[sp_choice2 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                elif(person_age >= 18 and person_age < 69 and person_gender == "Male"):
                                    sp_items = list(app.cursor.execute('SELECT category_item FROM special_items WHERE category_id=?',(app.cateoryList[4][0],)).fetchall())
                                    print("Choose the Options from the below List")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    

                                    while True:
                                        try:
                                            sp_choice1 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice1 <= len(sp_items)  and sp_choice1 > 0):
                                                special_item1 = sp_items[sp_choice1 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_choice2 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice2 <= len(sp_items) and sp_choice2 > 0):
                                                special_item2 = sp_items[sp_choice2 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                elif(person_age >= 18 and person_age < 69 and person_gender == "Other"):
                                    sp_items = list(app.cursor.execute('SELECT category_item FROM special_items WHERE category_id=?',(app.cateoryList[5][0],)).fetchall())
                                    print("Choose the Options from the below List")
                                    for item in range(0, len(sp_items)):
                                        print(item + 1, " ", sp_items[item][0])
                                    
                                    while True:
                                        try:
                                            sp_choice1 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice1 <= len(sp_items) and sp_choice1 > 0):
                                                special_item1 = sp_items[sp_choice1 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                    
                                    while True:
                                        try:
                                            sp_choice2 = int(input("Enter you Food Item Option number from the above list:"))
                                            if(sp_choice2 <= len(sp_items) and sp_choice2 > 0):
                                                special_item2 = sp_items[sp_choice2 - 1][0]
                                                break
                                            else:
                                                print("please enter a valid option.!")
                                                continue
                                        except ValueError:
                                            print("please enter a valid option.!")
                                            continue
                                    
                                # print(special_item1, special_item2)
                                app.register_survey(person_aadhar, person_name, person_gender, person_age, person_slum_name, person_rice_eat, person_dal_eat, special_item1.strip().capitalize(), special_item2.strip().capitalize())
                            
                            elif (survey_choice == 2):

                                aadhar_id = input("Enter the aadhar Id: ")

                                if(aadhar_id.isdigit()):
                                    food_information_results = app.cursor.execute('SELECT * FROM survey_data WHERE person_aadhar=?', (aadhar_id, )).fetchone()
                                    
                                    if food_information_results is not None:
                                        food_information_results = list(food_information_results)
                                        print("Aadhar Number: {}".format(food_information_results[0]))
                                        print("Person Name: {}".format(food_information_results[1]))
                                        print("Gender: {}".format(food_information_results[2]))
                                        print("Age: {}".format(food_information_results[3]))
                                        print("Slum Name: {}".format(food_information_results[4]))
                                        print("************************************************************************")
                                        print("Food Item \t Quantity As Per Survey \t Monthly Quantity")
                                        print("Rice Quantity: {:.2f} KG : {:.2f} KG".format(food_information_results[5]/1000, ((food_information_results[5]/1000) * 30)))
                                        print("Dal Quantity: {:.2f} KG : {:.2f} KG".format(food_information_results[6]/1000, ((food_information_results[6]/1000) * 30)))
                                        # print("{}".format(food_information_results[7]))
                                        # print("{}".format(food_information_results[8]))

                                        special_item_results = app.cursor.execute('SELECT * FROM food_products').fetchall()

                                        for item in special_item_results:
                                            if(item[1].casefold() == food_information_results[7].casefold()):
                                                print("{} : 1 : {}".format(item[1], item[2]))
                                            
                                            if(item[1].casefold() == food_information_results[8].casefold()):
                                                print("{} : 1 : {}".format(item[1], item[2]))

                                    else:
                                        print("No Person is registered with that Aadhar Card.!")
                                        
                                    
                                
                            elif(survey_choice == 3):
                                print("Thanks for using our Application.!")
                                sys.exit(0)

                        except ValueError:
                            print("You have entered a wrong Option choice.!")
                            continue
                
                        
                elif(userChoice == 3):
                    print("Thanks for using our Application.!")
                    sys.exit(0)
        
                workOption = input("Do you want to continue again: [y/n]")
                if(workOption.lower() == 'y'):
                    continue
                elif(workOption.lower() == 'n'):
                    break
                else:
                    print("You have entered the out of options.!")
                    sys.exit(0)
            else:
                print("Please enter a valid option.!")
                continue
        except ValueError:
            print("Please enter a valid option.!")
            continue