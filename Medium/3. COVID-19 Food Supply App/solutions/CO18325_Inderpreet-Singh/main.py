# SOLUTION BY : INDERPREET SINGH 
# GITHUB : CO18325
# EMAIL : inderpreet221099@gmail.com
# GIRLSCRIPT BANGLORE SEPTEMBER MEDIUM CHALLENGE



def main():

    # FOOD ITEMS 
    rice_per_day = 0.0 # IN KG
    dal_per_day = 0.0   # IN KG
    cerelac = 0
    amul_Powder = 0
    nandini_milk = 0
    bread = 0
    tiger_parle_g = 0
    canned_veggies = 0
    canned_fruits = 0
    medicine_pack = 0
    calcium_sandoz_tablets = 0

    # A DICTIONARY TO STORE THE PRICE R PACKET/KG AND QUANTITY REQUIRED PER MONTH
    price_quantity_dict = {
        'rice' :                    {'price': 40,   'quantity' : 30},
        'dal' :                     {'price': 65,   'quantity' : 30},
        'cerelac' :                 {'price': 140,  'quantity' : 3},
        'amul_Powder' :             {'price': 240,  'quantity' : 1},
        'nandini_milk' :            {'price': 45,   'quantity' : 8},
        'bread' :                   {'price': 25,   'quantity' : 4},
        'tiger_parle_g' :           {'price': 3,    'quantity' : 30},
        'canned_veggies' :          {'price': 100,  'quantity' : 4},
        'canned_fruits' :           {'price': 100,  'quantity' : 4},
        'medicine_pack' :           {'price': 500,  'quantity' : 1},
        'calcium_sandoz_tablets' :  {'price': 500,  'quantity' : 1},
    }



    # FOOD REQUIREMENTS AS PER AGE CATEGORIES

    # Infants: Below 2years	?
    infant_food = ["Cerelac", "Amul powder", "Nandini Milk TetraPacks"]
    # Children: Between 3 to 18 years	?
    childern_food = ["Bread", "Tiger/Parle G", "Nandini Milk TetraPacks", "Canned Fruits", "Canned Veggies"]
    # Old Age: Above 70 years	?
    old_age_food = ["Canned Fruits", "Canned Veggies", "Nandini Milk TetraPacks", "Medicine Packs"]
    # Adult Female: Between 18 to 69 years	?
    adult_female_food = ["Canned Fruits", "Canned Veggies", "Nandini Milk TetraPacks", "Calcium Sandoz Tablets"]
    # Adult Male: Between 18 to 69 years	?
    adult_male_food = ["Canned Fruits", "Canned Veggies", "Nandini Milk TetraPacks"]
    # Adult Other: Between 18 to 69 years
    adult_other_food = ["Canned Fruits", "Canned Veggies", "Nandini Milk TetraPacks", "Calcium Sandoz Tablets"]



    # NUMBER OF PEOPLE OF VARIOUS CATEGORIES
    infants = 0
    childern = 0
    old_aged = 0
    adult_females = 0
    adult_males = 0
    adult_others = 0

    # GENDER LIST
    gender_list = ["Male", "Female", "Other"]


    # START THE REGISTRATION PROCESS
    while True:
        # INTIALIZING A DICTIONARY TO STORE PERSON INFORMATION
        Person = {}

        # ASK FOR REGISTRATION OF A NEW REGISTRATION
        choose = input("REGISTER FOR THE SURVEY [Y || N]: ")

        if( choose == 'y' or choose == 'Y'):
            Person['aadhar_num'] = input("AADHAR NUMBER : ")
            Person['name'] = input("NAME AS PER AADHAR NUMBER: ")
            
            # LOOP UNTIL USER DOEESN'T INPUT CORRECT GENDER TYPE
            while True:
                # Printing the Gender Catageories
                for index,gender in enumerate(gender_list):
                    print(gender + "-" + str(index))
                
                opt = None
                # CHECK FOR THE INPUT BY USER
                # THROW ERROR IN CASE OF WRONG INPUT TYPE
                try:
                    opt = int(input("\nENTER THE NUMBER CORRESPONDING TO YOUR GENDER : "))
                except ValueError:
                    print("INVALID INPUT!")
                    continue

                # CHECK FOR THE OPTION CHOOSEN BY THE USER
                if opt ==  0:
                    Person['gender'] = gender_list[opt]
                    break
                elif opt == 1:
                    Person['gender'] = gender_list[opt]
                    break
                elif opt == 2:
                    Person['gender'] = gender_list[opt]
                    break
                else:
                    # FOR INVALID NUMBER INPUT
                    print("INVALID NUMBER CHOOSEN. PLEASE TRY AGAIN")
                    
            # LOOP UNTIL THE USER DOESN'T ENTER CORRECT AGE TYPE
            while True:
                try:
                    Person['age'] = int(input("\nEnter the person age: "))
                    break
                except ValueError:
                    # FOR INVALID AGE TYPE INPUT
                    print("ENTER A VALID AGE !")
                    continue

            # INCREMENT THE CATEGORY COUNT FOR THIS AGE PEOPLE
            if (Person['age'] <= 2):
                infants += 1
            elif Person['age'] >= 3 and Person['age'] < 18:
                childern += 1
            elif Person['age'] > 70:
                old_aged += 1
            elif Person['age'] >= 18 and Person['age'] < 69 and Person['gender'] == "Female":
                adult_females += 1
            elif Person['age'] >= 18 and Person['age'] < 69 and Person['gender'] == "Male":
                adult_males += 1
            elif Person['age'] >= 18 and Person['age'] < 69 and Person['gender'] == "Other":
                adult_others += 1

            # LOOP UNTIL THE USER INPUTS A VALID VALUE OF RICE INTAKE BY HIM.
            while True:
                try:
                    # IN THE PERSON DICTIONARY, RICE AMOUNT IS STORED IN GRAMS
                    Person['rice'] = float(input("\nRICE INTAKE BY YOU IN A DAY (IN GRAMS) : "))
                    break
                except ValueError:
                    # IN CASE OF INVALID INPUT BY THE USER
                    print("INVALID INPUT GIVEN. PLEASE TRY AGAIN!")
                    continue

            # STORING IN rice VARIABLE IN KGs
            rice_per_day += Person['rice'] / 1000

            # LOOP UNTIL THE USER INPUTS A VALID VALUE OF DAL INTAKE BY HIM.
            while True:
                try:
                    # IN THE PERSON DICTIONARY, DAL AMOUNT IS STORED IN GRAMS
                    dalIntakeContent = float(input("\nDAL INTAKE BY YOU IN A DAY (IN GRAMS) : "))
                    break
                except ValueError:
                    # IN CASE OF INVALID INPUT BY THE USER
                    print("INVALID INPUT GIVEN. PLEASE TRY AGAIN!")
                    continue
            # STORING IN dal VARIABLE IN KGs
            dal_per_day += (dalIntakeContent/1000)


            #################################### SPECIAL PRODUCTS OFFER ####################################

            food_list = []

            # CREATING THE FOOD LIST
            # BASED ON THE AGE CATEGORY OF THE PERSON
            if(Person['age'] <= 2):
                food_list = infant_food
            elif (Person['age'] >= 3 and Person['age'] < 18):
                food_list = childern_food
            elif (Person['age'] > 70):
                food_list = old_age_food
            elif Person['age'] >= 18 and Person['age'] < 69 and Person['gender'] == "Female":
                food_list = adult_female_food
            elif Person['age'] >= 18 and Person['age'] < 69 and Person['gender'] == "Male":
                food_list = adult_male_food
            elif Person['age'] >= 18 and Person['age'] < 69 and Person['gender'] == "Other":
                food_list = adult_other_food


            # LIST TO STORE THE SPECIAL OFFERS SELECTED BY THE PERSON
            Person['special'] = list()

            # SHOWING THE LIST OF THE FOOD OFFERS AVAILABLE ALONG WITH THE INDEX NUMBERS
            for index,item in enumerate(food_list):
                print(str(index) + "--" + item)
            
            # LOOP UNTIL THE USER CHOOSE VALID 2 SPECIAL OFFERS
            while len(Person['special']) != 2:
                item_choosen_index = None
                try:
                    item_choosen_index = int(input("\nENTER THE NUMBER CORRESPONDING TO THE SPECIAL FOOD YOU WANT TO SELECT : "))
                except ValueError:
                    #IF THERE IS AN INVALID INPUT TYPE BY USER
                    print("INVALID INPUT GIVEN. PLEASE TRY AGAIN!")
                    continue

                # INDEX OF CHOOSEN ITEM SHOULD BE LESS THAN EQUAL TO 2
                if(item_choosen_index < len(food_list)):
                    (Person['special']).append(food_list[item_choosen_index])
                # FOR A OUT OF BOUND INDEX NUMBER
                else:
                    print("PLEASE ENTER A VALID CORESSPONDING NUMBER")
                    continue
            

            # INCREASE THE TOTAL COUNT OF THE TOTAL ITEMS
            # OF THE ITEMS SELECTED BY THE PERSON
            for item in Person['special']:
                if (item == "Cerelac"):
                    cerelac += 1
                elif (item == "Amul powder"):
                    amul_Powder += 1
                elif (item == "Nandini Milk TetraPacks"):
                    nandini_milk += 1
                elif (item == "Bread"):
                    bread += 1
                elif (item == "Tiger/Parle G"):
                    tiger_parle_g += 1
                elif (item == "Canned Fruits"):
                    canned_fruits += 1
                elif (item == "Canned Veggies"):
                    canned_veggies += 1
                elif (item == "Medicine Packs"):
                    medicine_pack += 1
                elif (item == "Calcium Sandoz Tablets"):
                    calcium_sandoz_tablets += 1


            print("\nINFORMATION ENTERED BY PERSON : ")
            print(Person)
            print("\n-------------------------------------------------------------------------------\n")
                
        elif( choose == 'n' or choose=='N'):
            break
        else:
            print("INVALID KEY DOWN!!")
            continue

        
    # OUTPUT THE GENERATED RESULT:
    print("\n\n\n-------------------------------------- REPORT GENERATED --------------------------------------\n\n")

    print("INFORMATION REGARDING POPULATION")

    print("Infants: Below 2years: {}".format(infants))
    print("Children: Between 3 to 18 years: {}".format(childern))
    print("Old Age: Above 70 years: {}".format(old_aged))
    print("Adult Female: Between 18 to 69 years: {}".format(adult_females))
    print("Adult Male: Between 18 to 69 years: {}".format(adult_males))
    print("Adult Other: Between 18 to 69 years: {}".format(adult_others))
    
    
    print("\n\n------------------------------------------------------------------------------------\n\n")
    print("FOOD QUANTITY REQUIREMENT INFORMATION")
    print("Rice in Kg per day:      {0:.2f} KG".format(rice_per_day))
    print("Dal in Kg per day:       {0:.2f} KG".format(dal_per_day))
    print("Cerelac:                 {}".format(cerelac))
    print("Amul powder:             {}".format(amul_Powder))
    print("Nandini Milk TetraPacks: {}".format(nandini_milk))
    print("Bread:                   {}".format(bread))
    print("Tiger/Parle G Biscuits:  {}".format(tiger_parle_g))
    print("Canned Veggies:          {}".format(canned_veggies))
    print("Canned Fruits:           {}".format(canned_fruits))
    print("Medicine Packs:          {}".format(medicine_pack))
    print("Calcium Sandoz Tablets:  {}".format(calcium_sandoz_tablets))


    print("\n\n------------------------------------------------------------------------------------\n\n")
    print("FOOD MONTHLY QUANTITY REQUIREMENT INFORMATION")
    print("Rice in Kg per day:      {0:.2f} KG".format(rice_per_day * price_quantity_dict['rice']['quantity']))
    print("Dal in Kg per day:       {0:.2f} KG".format(dal_per_day * price_quantity_dict['dal']['quantity']))
    print("Cerelac:                 {}".format(cerelac * price_quantity_dict['cerelac']['quantity']))
    print("Amul powder:             {}".format(amul_Powder * price_quantity_dict['amul_Powder']['quantity']))
    print("Nandini Milk TetraPacks: {}".format(nandini_milk * price_quantity_dict['nandini_milk']['quantity']))
    print("Bread:                   {}".format(bread * price_quantity_dict['bread']['quantity']))
    print("Tiger/Parle G Biscuits:  {}".format(tiger_parle_g * price_quantity_dict['tiger_parle_g']['quantity']))
    print("Canned Veggies:          {}".format(canned_veggies * price_quantity_dict['canned_veggies']['quantity']))
    print("Canned Fruits:           {}".format(canned_fruits * price_quantity_dict['canned_fruits']['quantity']))
    print("Medicine Packs:          {}".format(medicine_pack * price_quantity_dict['medicine_pack']['quantity']))
    print("Calcium Sandoz Tablets:  {}".format(calcium_sandoz_tablets * price_quantity_dict['calcium_sandoz_tablets']['quantity']))


    print("\n\n------------------------------------------------------------------------------------\n\n")
    print("TOTAL MONEY REQUIREMENT REQUIREMENT INFORMATION")
    print("Rice cost per month:                     Rs {0:.2f}.".format(rice_per_day * price_quantity_dict['rice']['quantity'] * price_quantity_dict['rice']['price']))
    print("Dal cost per month:                      Rs {0:.2f}.".format(dal_per_day * price_quantity_dict['dal']['quantity']  * price_quantity_dict['dal']['price']))
    print("Cerelac cost per month:                  Rs {}.".format(cerelac * price_quantity_dict['cerelac']['quantity'] * price_quantity_dict['cerelac']['price']))
    print("Amul powder cost per month:              Rs {}.".format(amul_Powder * price_quantity_dict['amul_Powder']['quantity'] * price_quantity_dict['amul_Powder']['price']))
    print("Nandini Milk TetraPacks cost per month:  Rs {}.".format(nandini_milk * price_quantity_dict['nandini_milk']['quantity'] * price_quantity_dict['nandini_milk']['price']))
    print("Bread cost per month:                    Rs {}.".format(bread * price_quantity_dict['bread']['quantity'] * price_quantity_dict['bread']['price']))
    print("Tiger/Parle G Biscuits cost per month:   Rs {}.".format(tiger_parle_g * price_quantity_dict['tiger_parle_g']['quantity'] * price_quantity_dict['tiger_parle_g']['price']))
    print("Canned Veggies cost per month:           Rs {}.".format(canned_veggies * price_quantity_dict['canned_veggies']['quantity'] * price_quantity_dict['canned_veggies']['price']))
    print("Canned Fruits cost per month:            Rs {}.".format(canned_fruits * price_quantity_dict['canned_fruits']['quantity'] * price_quantity_dict['canned_fruits']['price']))
    print("Medicine Packs cost per month:           Rs {}.".format(medicine_pack * price_quantity_dict['medicine_pack']['quantity'] * price_quantity_dict['medicine_pack']['price']))
    print("Calcium Sandoz Tablets cost per month:   Rs {}.".format(calcium_sandoz_tablets * price_quantity_dict['calcium_sandoz_tablets']['quantity'] * price_quantity_dict['calcium_sandoz_tablets']['price']))




# CALL THE MAIN FUNCTION
main()