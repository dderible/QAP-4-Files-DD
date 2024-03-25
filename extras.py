allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
Provinces = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
Option = ["Y", "y", "n", "N"]
Pay = ["Full", "Monthly", "Down Pay", "full", "monthly", "down pay", "Down pay"]

def FirstName(FirstName):
    while True:
        FirstName = input("Enter your first name: ")
        if FirstName == "":
            print("ERROR: First Name must be entered.")
        elif set(FirstName).issubset(allowed_char) == False:
            print("ERROR: Name contains invalid characters.")
        else:
            break

def LastName(LastName):
    while True:
        LastName = input("Enter your last name: ")
        if LastName == "":
            print("ERROR: First Name must be entered.")
        elif set(LastName).issubset(allowed_char) == False:
            print("ERROR: Name contains invalid characters.")
        else:
            break

def Address(Address):
    while True:
        Address = input("Enter your street address: ")
        if Address == "":
            print("ERROR: Street Address must be entered.")
        else:
            break

def City(City):
    while True:
        City = input("Enter your city of residence: ")
        if City == "":
            print("ERROR: City must be entered.")
        elif set(City).issubset(allowed_char) == False:
            print("ERROR: City contains invalid characters.")
        else:
            break

def Province(Province):
    while True:
        Province = input("Enter the customer province (XX): ")
        if Province == "":
            print("ERROR: Province must be entered.")
        elif len(Province) != 2:
            print("ERROR: Province must be 2 characters long.")
        elif Province not in Provinces:
            print("ERROR: Province contains invalid characters, or has been spelt incorrectly.")
        else:
            break

def PostalCode(PostalCode):
    while True:
        PostalCode = input("Enter your postal code of residence: ")
        if PostalCode == "":
            print("ERROR: Postal Code must be entered.")
        else:
            break

def PhoneNumber(PhoneNumber):
    while True:
        PhoneNumber = input("Enter your phone number (10 digits): ")
        if PhoneNumber == "":
            print("ERROR: Phone Number must be entered.")
        elif len(PhoneNumber) != 10:
            print("ERROR: Phone Number must be 10 digits long.") 
        elif PhoneNumber.isdigit() == False:
            print("ERROR: Phone Number contains invalid characters.")
        else:
            break