# Special Food Items List
infantsItems = ["Cerelac", "Amul powder", "Nandini Milk TetraPacks"]
childernItems = ["Bread", "Tiger/Parle G", "Nandini Milk TetraPacks", "Canned Fruits", "Canned Veggies"]
oldAgeItems = ["Canned Fruits", "Canned Veggies", "Nandini Milk TetraPacks", "Medicine Packs"]
adultFemaleItems = ["Canned Fruits", "Canned Veggies", "Nandini Milk TetraPacks", "Calcium Sandoz Tablets"]
adultMaleItems = ["Canned Fruits", "Canned Veggies", "Nandini Milk TetraPacks"]
adultOtherItems = ["Canned Fruits", "Canned Veggies", "Nandini Milk TetraPacks", "Calcium Sandoz Tablets"]

# calculating Items
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

# People Count

infantCount = 0
childernCount = 0
oldAgeCount = 0
adultFemaleCount = 0
adultMaleCount = 0
adultOtherCount = 0

# Monthly Quantity Values
riceMonthlyQuantity = 30
dalMonthlyQuantity = 30
cerelacMonthlyQuantity = 3
amulPowderMonthlyQuantity = 1
nandhiniMilkMonthlyQuantity = 8
breadMonthlyQuantity = 4
tigerParleMonthlyQuantity = 30
cannedVeggiesMonthlyQuantity = 4
cannedFruitsMonthlyQuantity = 4
medicinePackMonthlyQuantity = 1
calciumSandozMonthlyQuantity = 1


# Item Prices
ricePrice = 40
dalPrice = 65
cerelacPrice = 140
amulPowderPrice = 240
nandhiniMilkPrice = 45
breadPrice = 25
tigerParlePrice = 3
cannedVeggiesPrice = 100
cannedFruitsPrice = 100
medicinePrice = 500
calciumSandozPrice = 500

# Overall Variable
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


if __name__ == "__main__":

    while True:
        surveyChioce = input("Do you want to register survey [y/n]: ")
        if( surveyChioce.lower() == 'y'):
            personAadharNumber = input("Enter your Aadhar Number: ")
            personName = input("Enter your name as per Aadhar: ")
            genderList = ["Male", "Female", "Other"]
            personGender = None
            
            while True:
                # Printing the Gender Catageories
                for i in range(0, len(genderList)):
                    print(i+1, " ", genderList[i])
                choice = None
                try:
                    choice = int(input("Enter your options from the above list:"))
                except ValueError:
                    print("You have Entered the wrong Input. please follow the steps carefully.!")
                    continue
            
                if(choice ==  1):
                    personGender = genderList[choice - 1]
                    break
                elif (choice == 2):
                    personGender = genderList[choice - 1]
                    break
                elif (choice == 3):
                    personGender = genderList[choice - 1]
                    break
                else:
                    print("You have entered the wrong value! Please fill the details properly")
                    continue
            
            # Person Age Input
            personAge = None
            while True:
                try:
                    personAge = int(input("Enter the person age: "))
                    break
                except ValueError:
                    print("Please enter a valid age.!")
                    continue
            
            # Age Count
            if (personAge <= 2):
                infantCount += 1
            elif (personAge >= 3 and personAge < 18):
                childernCount += 1
            elif (personAge > 70):
                oldAgeCount += 1
            elif (personAge >= 18 and personAge < 69 and personGender == "Female"):
                adultFemaleCount += 1
            elif (personAge >= 18 and personAge < 69 and personGender == "Male"):
                adultMaleCount += 1
            elif (personAge >= 18 and personAge < 69 and personGender == "Other"):
                adultOtherCount += 1

            # Rice Input Intake
            riceIntakeContent = None
            while True:
                try:
                    riceIntakeContent = float(input("Enter How much rice in grams he/she eats per day?: "))
                    break
                except ValueError:
                    print("Please enter a valid value.!")
                    continue
            
            # Calculating the Rice Value
            riceInKgPerDay = riceInKgPerDay + (riceIntakeContent/1000)
            
            # Dal Input Intake
            dalIntakeContent = None
            while True:
                try:
                    dalIntakeContent = float(input("Enter How much dal in grams he/she eats per day?: "))
                    break
                except ValueError:
                    print("Please enter a valid value.!")
                    continue
            dalInKgPerDay = dalInKgPerDay + (dalIntakeContent/1000)

            # Infants Special Products
            if(personAge <= 2):

                # Storing the Items
                specialItemChoices = list()

                for i in range(0, len(infantsItems)):
                    print(i+1, ": ", infantsItems[i])
                
                while len(specialItemChoices) != 2:
                    specialItemChoice = None
                    try:
                        specialItemChoice = int(input("Please enter the special Item based on your choice: "))
                    except ValueError:
                        print("Please enter a valid value.!")
                        continue
                    if(specialItemChoice <= 3):
                        specialItemChoices.append(infantsItems[specialItemChoice - 1])
                    else:
                        print("Please enter a valid value.!")
                        continue
                
                for item in specialItemChoices:
                    if (item == "Cerelac"):
                        cerelacCount += 1
                    elif (item == "Amul powder"):
                        amulPowderCount += 1
                    elif (item == "Nandini Milk TetraPacks"):
                        nandiniMilkItemCount += 1
            
            # Childern Special Items
            elif (personAge >= 3 and personAge < 18):
                 # Storing the Items
                specialItemChoices = list()

                for i in range(0, len(childernItems)):
                    print(i+1, ": ", childernItems[i])
                
                while len(specialItemChoices) != 2:
                    specialItemChoice = None
                    try:
                        specialItemChoice = int(input("Please enter the special Item based on your choice: "))
                    except ValueError:
                        print("Please enter a valid value.!")
                        continue
                    if(specialItemChoice <= 5):
                        specialItemChoices.append(childernItems[specialItemChoice - 1])
                    else:
                        print("Please enter a valid value.!")
                        continue
                
                for item in specialItemChoices:
                    if (item == "Bread"):
                        breadCount += 1
                    elif (item == "Tiger/Parle G"):
                        tigerOrParle_G_Count += 1
                    elif (item == "Nandini Milk TetraPacks"):
                        nandiniMilkItemCount += 1
                    elif (item == "Canned Fruits"):
                        cannedFruitsCount += 1
                    elif (item == "Canned Veggies"):
                        cannedVeggiesCount += 1
            
            # Old Age Special Items

            elif (personAge > 70):
                # Storing the Items
                specialItemChoices = list()

                for i in range(0, len(oldAgeItems)):
                    print(i+1, ": ", oldAgeItems[i])
                
                while len(specialItemChoices) != 2:
                    specialItemChoice = None
                    try:
                        specialItemChoice = int(input("Please enter the special Item based on your choice: "))
                    except ValueError:
                        print("Please enter a valid value.!")
                        continue
                    if(specialItemChoice <= 4):
                        specialItemChoices.append(oldAgeItems[specialItemChoice - 1])
                    else:
                        print("Please enter a valid value.!")
                        continue
                
                for item in specialItemChoices:
                    if (item == "Medicine Packs"):
                        medicinePackCount += 1
                    elif (item == "Nandini Milk TetraPacks"):
                        nandiniMilkItemCount += 1
                    elif (item == "Canned Fruits"):
                        cannedFruitsCount += 1
                    elif (item == "Canned Veggies"):
                        cannedVeggiesCount += 1

            # Adult Female Count
            elif (personAge >= 18 and personAge < 69 and personGender == "Female"):
                # Storing the Items
                specialItemChoices = list()

                for i in range(0, len(adultFemaleItems)):
                    print(i+1, ": ", adultFemaleItems[i])
                
                while len(specialItemChoices) != 2:
                    specialItemChoice = None
                    try:
                        specialItemChoice = int(input("Please enter the special Item based on your choice: "))
                    except ValueError:
                        print("Please enter a valid value.!")
                        continue
                    if(specialItemChoice <= 4):
                        specialItemChoices.append(adultFemaleItems[specialItemChoice - 1])
                    else:
                        print("Please enter a valid value.!")
                        continue
                
                for item in specialItemChoices:
                    if (item == "Calcium Sandoz Tablets"):
                        calcimSandozTabletCount += 1
                    elif (item == "Nandini Milk TetraPacks"):
                        nandiniMilkItemCount += 1
                    elif (item == "Canned Fruits"):
                        cannedFruitsCount += 1
                    elif (item == "Canned Veggies"):
                        cannedVeggiesCount += 1
          
            # Adult Male Count
            elif (personAge >= 18 and personAge < 69 and personGender == "Male"):
                # Storing the Items
                specialItemChoices = list()

                for i in range(0, len(adultMaleItems)):
                    print(i+1, ": ", adultMaleItems[i])
                
                while len(specialItemChoices) != 2:
                    specialItemChoice = None
                    try:
                        specialItemChoice = int(input("Please enter the special Item based on your choice: "))
                    except ValueError:
                        print("Please enter a valid value.!")
                        continue
                    if(specialItemChoice <= 3):
                        specialItemChoices.append(adultMaleItems[specialItemChoice - 1])
                    else:
                        print("Please enter a valid value.!")
                        continue
                
                for item in specialItemChoices:

                    if (item == "Nandini Milk TetraPacks"):
                        nandiniMilkItemCount += 1
                    elif (item == "Canned Fruits"):
                        cannedFruitsCount += 1
                    elif (item == "Canned Veggies"):
                        cannedVeggiesCount += 1
            
            # Adult Other Count
            elif (personAge >= 18 and personAge < 69 and personGender == "Other"):
                # Storing the Items
                specialItemChoices = list()

                for i in range(0, len(adultOtherItems)):
                    print(i+1, ": ", adultOtherItems[i])
                
                while len(specialItemChoices) != 2:
                    specialItemChoice = None
                    try:
                        specialItemChoice = int(input("Please enter the special Item based on your choice: "))
                    except ValueError:
                        print("Please enter a valid value.!")
                        continue
                    if(specialItemChoice <= 4):
                        specialItemChoices.append(adultOtherItems[specialItemChoice - 1])
                    else:
                        print("Please enter a valid value.!")
                        continue
                
                for item in specialItemChoices:
                    if (item == "Calcium Sandoz Tablets"):
                        calcimSandozTabletCount += 1
                    elif (item == "Nandini Milk TetraPacks"):
                        nandiniMilkItemCount += 1
                    elif (item == "Canned Fruits"):
                        cannedFruitsCount += 1
                    elif (item == "Canned Veggies"):
                        cannedVeggiesCount += 1
        elif( surveyChioce.lower() == 'n'):
            break
        else:
            print("Please enter a valid response")
            continue

print("############################################# OVERALL SURVEY REPORT #############################################")
print("\t\t Personal Information")
print("\t\t Age Group\t\t No.Of People")
print("\t\t Infants: Below 2years\t\t {}".format(infantCount))
print("\t\t Children: Between 3 to 18 years\t\t {}".format(childernCount))
print("\t\t Old Age: Above 70 years\t\t {}".format(oldAgeCount))
print("\t\t Adult Female: Between 18 to 69 years\t\t {}".format(adultFemaleCount))
print("\t\t Adult Male: Between 18 to 69 years\t\t {}".format(adultMaleCount))
print("\t\t Adult Other: Between 18 to 69 years\t\t {}".format(adultOtherCount))

print("\n")
print("\t\t\t\t\t Food Information")
print("\n")
print("\t\t Food Item\t\t\tRequired Quantity\t\tMonthly Quantity\tPrice")

# Calculating the Rice Price
if (riceInKgPerDay > 0):
    riceOverallResult = riceOverallResult + (riceInKgPerDay * riceMonthlyQuantity * ricePrice)
    totalAmount += riceOverallResult
    print("\t\t Rice in Kg per day: {:.2f} KG : {} : {}".format(riceInKgPerDay, riceMonthlyQuantity, riceOverallResult))

# Calculating the Dal Price
if (dalInKgPerDay > 0):
    dalOverallResult = dalOverallResult + (dalInKgPerDay * dalMonthlyQuantity * dalPrice)
    totalAmount += dalOverallResult
    print("\t\t Dal in Kg per day: {:.2f} KG : {} : {}".format(dalInKgPerDay, dalMonthlyQuantity, dalOverallResult))

# Calculating the Cerelac Items
if (cerelacCount > 0):
    cerelacOverallResult = cerelacOverallResult + (cerelacCount * cerelacMonthlyQuantity * cerelacPrice)
    totalAmount += cerelacOverallResult
    print("\t\t Cerelac: {} : {} : {}".format(cerelacCount, cerelacMonthlyQuantity, cerelacOverallResult))

# Amul Powder Calculation
if (amulPowderCount > 0):
    amulPowderOverallResult = amulPowderOverallResult + (amulPowderCount * amulPowderMonthlyQuantity * amulPowderPrice)
    totalAmount += amulPowderOverallResult
    print("\t\t Amul powder : {} : {} : {}".format(amulPowderCount, amulPowderMonthlyQuantity, amulPowderOverallResult))

# Nandini Milk Tetrapacks Calculation
if (nandiniMilkItemCount > 0):
    nandiniOverallResult = nandiniOverallResult + (nandiniMilkItemCount * nandhiniMilkMonthlyQuantity * nandhiniMilkPrice)
    totalAmount += nandiniOverallResult
    print("\t\t Nandini Milk TetraPacks: {} : {} : {}".format(nandiniMilkItemCount, nandhiniMilkMonthlyQuantity, nandiniOverallResult))

# Bread Calculation
if (breadCount > 0):
    breadOverallResult = breadOverallResult + (breadCount * breadMonthlyQuantity * breadPrice)
    totalAmount += breadOverallResult
    print("\t\t Bread: {} : {} : {}".format(breadCount, breadMonthlyQuantity, breadOverallResult))

# Tiger Parle G Biscuit calculation
if (tigerOrParle_G_Count > 0):
    tigerOverallResult = tigerOverallResult + (tigerOrParle_G_Count * tigerParleMonthlyQuantity * tigerParlePrice)
    totalAmount += tigerOverallResult
    print("\t\t Tiger/Parle G Biscuits: {} : {} : {}".format(tigerOrParle_G_Count, tigerParleMonthlyQuantity, tigerOverallResult))

# Canned Veggies Calculation
if (cannedVeggiesCount > 0):
    cannedVeggiesOverallResult = cannedVeggiesOverallResult + (cannedVeggiesCount * cannedVeggiesMonthlyQuantity * cannedVeggiesPrice)
    totalAmount += cannedVeggiesOverallResult
    print("\t\t Canned Veggies: {} : {} : {}".format(cannedVeggiesCount, cannedVeggiesMonthlyQuantity, cannedVeggiesOverallResult))

# Canned Fruits Calculation
if (cannedFruitsCount > 0):
    cannedFruitsOverallResult = cannedFruitsOverallResult + (cannedFruitsCount * cannedFruitsMonthlyQuantity * cannedFruitsPrice)
    totalAmount += cannedFruitsOverallResult
    print("\t\t Canned Fruits: {} : {} : {}".format(cannedFruitsCount, cannedFruitsMonthlyQuantity, cannedFruitsOverallResult))

# Medicine Packs Calculation
if (medicinePackCount > 0):
    medicinePacksOverallResult = medicinePacksOverallResult + (medicinePackCount * medicinePackMonthlyQuantity * medicinePrice)
    totalAmount += medicinePacksOverallResult
    print("\t\t Medicine Packs: {} : {} : {}".format(medicinePackCount, medicinePackMonthlyQuantity, medicinePacksOverallResult))

# Calcium Sandoz Calculation
if (calcimSandozTabletCount > 0):
    calciumandozOverallResult = calciumandozOverallResult + (calcimSandozTabletCount * calciumSandozMonthlyQuantity * calciumSandozPrice)
    totalAmount += calciumandozOverallResult
    print("\t\t Rice in Kg per day: {} : {} : {}".format(calcimSandozTabletCount, calciumSandozMonthlyQuantity, calciumandozOverallResult))

print("Total Amount Required: {}".format(totalAmount))