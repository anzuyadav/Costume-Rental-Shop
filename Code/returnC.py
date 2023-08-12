import datetime

def extractingContent():
    file = open("costumes.txt","r")
    content = file.readlines()
    file.close()
    return content


def createDictionary(content):
    dictionary = {}
    for index in range(len(content)):
        dictionary[index+1] = content[index].replace("\n","").split(",")
    return dictionary

def printCostumes(dictionaryData):
    print("----------------------------------------------------------------------------------")
    print("S.No.", "\t", "Costume Name", "\t\t", "Brand", "\t\t\t", "Price", "\t\t", "Quantity")
    print("----------------------------------------------------------------------------------")
    for key, value in dictionaryData.items():
        print(key, "\t", value[0], "\t\t", value[1], "\t\t", value[2], "\t\t", value[3])
    print("----------------------------------------------------------------------------------")

    return ""


def validID(dictionaryData):
    
    validId = False
    while validId == False:
        ID = input("Enter the costume ID to return: ")
        if ID.isdigit():
            ID = int(ID)
            if ID > 0 and ID <= len(dictionaryData):
                validID = True
                return ID
                break    
            else:
                print("It appears that you entered an option that was not available.")
                print("\n")
        else:
            print("Please type a number next time.")
            print("\n")


def validReturnQuantity(dictionaryData,ID):

    """we are validating the quantity of costume to be rented."""
    returnCostumeName = []
    returnCostumeBrand = []
    returnCostumeNumber = []
    
    validQuantity = False
    while validQuantity == False:
        quantity = input("Enter the quantity you want to return: ")
        if quantity.isdigit():
            quantity = int(quantity)
            validQuantity = True
            dictionaryData[ID][3] = str(int(dictionaryData[ID][3]) + quantity)
            returnCostumeName.append([dictionaryData[ID][0]])
            returnCostumeBrand.append([dictionaryData[ID][1]])
            returnCostumeNumber.append([quantity])
            return quantity
        else:
            print("Please enter a number not anything else!")
            print("\n")

def returnCostume():

    """This function is executed when the user wants to rent the costumes."""
    
    userReturnsClothes = True
    returnCostumeName = []
    returnCostumeBrand = []
    returnCostumeNumber = []
    
    while userReturnsClothes == True:
        print(printCostumes(dictionaryData))
        ID = validID(dictionaryData)
        quantity = validReturnQuantity(dictionaryData,ID)

        flag = True
        for costume in returnCostumeName:
            if costume[0] == ID:
                costume[1] += quantity
                flag = False
        if flag:
            returnCostumeName.append([dictionaryData[ID][0]])
            returnCostumeBrand.append([dictionaryData[ID][1]])
            returnCostumeNumber.append([quantity])

        valid_input = False
        while valid_input == False:
            returnMore = input("Wanna return more(yes/no)? ")
            if returnMore.lower() == "yes":
                print("\n")
                valid_input = True
                break
            elif returnMore.lower() == "no":
                print("\n")
                generateReturnBill(returnCostumeName, returnCostumeBrand, returnCostumeNumber)
                userReturnsClothes = False
                valid_input = True
            else:
                print("Please enter a option from given options only!")
                print("\n")
                continue 
        updateTextFile(dictionaryData)
        print("\n")

def generateReturnBill(returnCostumeName, returnCostumeBrand, returnCostumeNumber):

    validName = False
    while validName == False:
        Name = str(input("Enter your name: "))
        if Name.replace(" ", "").isalpha():
            validName = True
        else:
            print("You entered your name wrong.")
            print("\n")


    validPhoneNumber = False
    while validPhoneNumber == False:
        phoneNumber = str(input("Enter your Phone Number: "))
        if phoneNumber.isdigit():
            validPhoneNumber = True
        else:
            print("You entered your phone number wrong.")
            print("\n")

    address = str(input("Enter your Address: "))

    validDay = False
    while validDay == False:
        day = input("Enter number of Day from rent days: ")
        if day.isdigit():
            day = int(day)
            validDay = True
        else:
            print("Please enter the days which is always inpositive number!")
            print("\n") 
        
            
    dateTime = datetime.datetime.now()
    print("\n")
    print("=========================================")
    print("             Return Bill Details           ")
    print("=========================================")

    if day > 5:
        fday = day - 5
        fine = fday*10
    else:
        fine = 0
        
    print("Name of customer:",Name)
    print("Address:",address)
    print("Number:",phoneNumber)
    print("Date Time of return:",dateTime)
    print("Total fine: $"+str(fine))
    print("Items in rent are:",returnCostumeName)
    print("Brand of Items are:",returnCostumeBrand)
    print("Number of Items in rent are:",returnCostumeNumber)
    print("-----------------------------------")
    print("Bill is also generated in txt file.")
    print("-----------------------------------")


    text = "Return-"+Name+".txt"
    file = open(text,"w")
    file.write("=========================================")
    file.write("\n")
    file.write("             Return Bill Details           ")
    file.write("\n")
    file.write("=========================================")
    file.write("\n")
    file.write(f"Name of customer: {Name}")
    file.write("\n")
    file.write(f"Address: {address}")
    file.write("\n")
    file.write(f"Number: {phoneNumber}")
    file.write("\n")
    file.write(f"Date Time of return: {dateTime}")
    file.write("\n")
    file.write(f"Total fine: ${fine}")
    file.write("\n")
    file.write(f"Items in rent are: {returnCostumeName}")
    file.write("\n")
    file.write(f"Brand of Items are: {returnCostumeBrand}")
    file.write("\n")
    file.write(f"Number of Items in rent are: {returnCostumeNumber}")

def updateTextFile(dictionaryData):
    
    file = open("costumes.txt", "w")
    for value in dictionaryData.values():
        file.write(str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n")
    file.close() 

content = extractingContent()
dictionaryData = createDictionary(content)
