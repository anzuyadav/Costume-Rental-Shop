import rent
import returnC
def welcome():
    print("------------------------------------------------------------")
    print()
    print("             Welcome to Costume Rental Shop                 ")
    print()
    print("------------------------------------------------------------")

def display():
    
    while True: 
        print("\n")
        print("Select a desirable option")
        print("(1) || Press 1 to rent a costume.")
        print("(2) || Press 2 to return a costume.")
        print("(3) || Press 3 to exit.")
        print("\n")
        userOption = input("Enter a option: ")
        if userOption == "1":
            print("\n")
            print("Let's rent a costume")
            print("\n")
            rent.rentCostume()

        elif userOption == "2":
            print("\n")
            print("Let's return a costume")
            print("\n")
            returnC.returnCostume()

        elif userOption == "3":
            print("\n")
            print("            Thank You for Visiting Our Shop. ")


        else:
            print("\n")
            print("Invalid input !!")
            print("Please select from the given Options.")


welcome()
display()


