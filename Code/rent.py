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

def validSNo(dictionaryData):
    validSNo = False
    while validSNo == False:
        SNo = input("Enter the Serial number: ")
        try:
            if SNo.isdigit():
                SNo = int(SNo)
                if SNo > 0 and SNo <= len(dictionaryData):
                    if int(dictionaryData[SNo][3]) == 0:
                        print("\n")
                        print("Out of Stock! ")
                        print("\n")
                        print("Wanna try another Costume?")
                        print("\n")
                        print(printCostumes(dictionaryData))
                        continue
                    else:
                        validSNo == True
                        print("The serial number of Costume is",SNo)
                        print("\n")
                        print("The Costume is available.")
                        print("\n")
                    return SNo
                else:
                    print("Please enter a option from the given options only!")
                    print("\n")
            else:
                print("Please type a number!")
                print("\n")
        except:
            Print("Invalid Serial Number")


def validQuantity(dictionaryData, SNo):

    cart = []
    tempRent = []
    costumeName = []
    costumeBrand = []
    costumeNumber = []
    validQuantity = False

    while validQuantity == False:
        quantity = input("How many dresses you want to rent? ")
        try:
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0 and quantity <= int(dictionaryData[SNo][3]):
                    validQuantity = True
                    dictionaryData[SNo][3] = str(int(dictionaryData[SNo][3])- quantity)
                    return quantity
                elif quantity > int(dictionaryData[SNo][3]):
                    print("Quantity you want is greater than we have in stock.")
                else:
                    print("Invalid Input!")
            else:
                print("Please enter a number.")
        except:
            print("Invalid Quantity !")

        
def rentCostume():

    userWantsClothes = True
    cart = []
    tempRent = []
    costumeName = []
    costumeBrand = []
    costumeNumber = []

    while userWantsClothes == True:
        print(printCostumes(dictionaryData))
        SNo = validSNo(dictionaryData)
        quantity = validQuantity(dictionaryData, SNo)
        #print(quantity)

        flag = True
        for costume in cart:
            if costume[0] == SNo:
                costume[1] += quantity
                flag = False
        if flag:
            cart.append([dictionaryData[SNo][0], quantity])
            tempRent.append([dictionaryData[SNo][0], dictionaryData[SNo][1], dictionaryData[SNo][2], quantity])
            costumeName.append([dictionaryData[SNo][0]])
            costumeBrand.append([dictionaryData[SNo][1]])
            costumeNumber.append([quantity])
            
        valid_input = False
        while valid_input == False:
            rentAnother = input("Wanna rent more(yes/no)? ")
            if rentAnother.lower() == "yes":
                print("\n")        
                print(f"Your Cart: {cart}")
                print("\n")
                valid_input = True
                break
            elif rentAnother.lower() == "no":
                print("\n")
                generateRentBill(tempRent, costumeName, costumeBrand, costumeNumber)
                userWantsClothes = False
                valid_input = True
            else:
                print("Invalid Input !!")
                print("\n")
                continue 
        updateTextFile(dictionaryData)
        print("\n")

def generateRentBill(tempRent, costumeName, costumeBrand, costumeNumber):
    
    validName = False
    while validName == False:
        Name = str(input("Enter your name: "))
        if Name.replace(" ", "").isalpha():
            validName = True
        else:
            print("You entered your name wrong.")
            print("\n")
            
    address = str(input("Enter your Address: "))

    validPhoneNumber = False
    while validPhoneNumber == False:
        phoneNumber = str(input("Enter your Phone Number: "))
        if phoneNumber.isdigit():
            validPhoneNumber = True
        else:
            print("You entered your phone number wrong.")
            print("\n")
            
    dateTime = datetime.datetime.now()
    print("\n")
    print("=========================================")
    print("             Rent Bill Details           ")
    print("=========================================")

    finalPrice = 0
    for i in range(len(tempRent)):
        for j in range(len(tempRent[i])):
            dollarprice = float(tempRent[i][2].replace("$",""))
            priceDetail = dollarprice * tempRent[i][3]    
        finalPrice = finalPrice + priceDetail
        
    print("Name of customer:",Name)
    print("Address:",address)
    print("Number:",phoneNumber)
    print("Date Time of borrow:",dateTime)
    print("Total price is: $"+str(finalPrice))
    print("Items in rent are:",costumeName)
    print("Brand of Items are:",costumeBrand)
    print("Number of Items in rent are:",costumeNumber)
    print("-----------------------------------")
    print("Bill is also generated in txt file.")
    print("-----------------------------------")

    text = "Rent-"+Name+".txt"
    file = open(text,"w")
    file.write("=========================================")
    file.write("\n")
    file.write("             Rent Bill Details           ")
    file.write("\n")
    file.write("=========================================")
    file.write("\n")
    file.write(f"Name of customer: {Name}")
    file.write("\n")
    file.write(f"Address: {address}")
    file.write("\n")
    file.write(f"Number: {phoneNumber}")
    file.write("\n")
    file.write(f"Date Time of borrow: {dateTime}")
    file.write("\n")
    file.write(f"Total price is: ${finalPrice}")
    file.write("\n")
    file.write(f"Items in rent are: {costumeName}")
    file.write("\n")
    file.write(f"Brand of Items are: {costumeBrand}")
    file.write("\n")
    file.write(f"Number of Items in rent are: {costumeNumber}")

def updateTextFile(dictionaryData):
    
    file = open("costumes.txt", "w")
    for value in dictionaryData.values():
        file.write(str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n")
    file.close()

content = extractingContent()
dictionaryData = createDictionary(content)
