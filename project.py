# Description: 
# Author: Declan Derible
# Date(s): March 20th, 2024


# Define Required Libraries
import datetime

# Define Program Constants
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
ADD_CAR_DISCOUNT = .25
EXTRA_LIABILITY = 125
GLASS_COVERAGE = 86
LOANER_CAR = 58
HST = .15
PROCESSING_FEE = 39.99
DATE = datetime.datetime.now()

# Define Program Functions


# Main Program Begins

    # Gather User Inputs
allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
Provinces = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
Option = ["Y", "y", "n", "N"]
Pay = ["Full", "Monthly", "Down Pay", "full", "monthly", "down pay", "Down pay"]
Claim1 = ["983", "2019/08/03", "$1,422"]
Claim2 = ["1337", "2022/11/21", "$711"]

Date = datetime.datetime.strftime(DATE, "%Y-%b-%d")

while True:
    FirstName = input("Enter your first name: ")
    if FirstName == "":
        print("ERROR: First Name must be entered.")
    elif set(FirstName).issubset(allowed_char) == False:
        print("ERROR: Name contains invalid characters.")
    else:
        break

while True:
    LastName = input("Enter your last name: ")
    if LastName == "":
        print("ERROR: First Name must be entered.")
    elif set(LastName).issubset(allowed_char) == False:
        print("ERROR: Name contains invalid characters.")
    else:
        break

while True:
    Address = input("Enter your street address: ")
    if Address == "":
        print("ERROR: Street Address must be entered.")
    else:
        break

while True:
    City = input("Enter your city of residence: ")
    if City == "":
        print("ERROR: City must be entered.")
    elif set(City).issubset(allowed_char) == False:
        print("ERROR: City contains invalid characters.")
    else:
        break

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

while True:
    PostalCode = input("Enter your postal code of residence: ")
    if PostalCode == "":
        print("ERROR: Postal Code must be entered.")
    else:
        break

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

while True:
    CarQuantity = input("Enter the quantity of cars being insured: ")
    if CarQuantity == "":
        print("ERROR: Car Quantity must be entered.")
    elif CarQuantity.isdigit() == False:
        print("ERROR: Car Quantity contains invalid characters.")
    else:
        break

while True:
    ExtraLiability = input("Would you like Extra Liability up to $1,000? (Y/N): ")
    if ExtraLiability == "":
        print("ERROR: Option must be entered.")
    elif len(ExtraLiability) != 1:
        print("ERROR: Option must be 1 character long.")
    elif ExtraLiability not in Option:
        print("ERROR: Option contains invalid characters, or has been spelt incorrectly.")
    else:
        break

while True:
    GlassCoverage = input("Would you like Glass Coverage? (Y/N): ")
    if GlassCoverage == "":
        print("ERROR: Option must be entered.")
    elif len(GlassCoverage) != 1:
        print("ERROR: Option must be 1 character long.")
    elif GlassCoverage not in Option:
        print("ERROR: Option contains invalid characters, or has been spelt incorrectly.")
    else:
        break

while True:
    CarLoan = input("Would you like a Car Loan? (Y/N): ")
    if CarLoan == "":
        print("ERROR: Option must be entered.")
    elif len(CarLoan) != 1:
        print("ERROR: Option must be 1 character long.")
    elif CarLoan not in Option:
        print("ERROR: Option contains invalid characters, or has been spelt incorrectly.")
    else:
        break

while True:
    Payment = input("How would you like to pay? (Full/Monthly/Down Pay): ")
    if Payment == "":
        print("ERROR: Option must be entered.")
    elif Payment not in Pay:
        print("ERROR: Options contains invalid characters, or has been spelt incorrectly.")
    elif Payment == ["Down Pay", "down pay"]:
        DownPay = input("How much would you like to pay?: ")
        if DownPay == "":
            print("ERROR: Amount must be entered.")
        elif DownPay.isdigit() == False:
            print("ERROR: Amount contains invalid characters.")
        else:
            break

    # Converting Variables

    TFirstName = FirstName.title()
    TLastName = LastName.title()
    TCity = City.title()
    TPayment = Payment.title()

    UExtraLiability = ExtraLiability.upper()
    UGlassCoverage = GlassCoverage.upper()
    UCarLoan = CarLoan.upper()

    ICarQuantity = int(CarQuantity)
    IDownPay = int(DownPay)

    # Generate Program Results Through Calculations

    ExtraCarPremium = BASIC_PREMIUM * .25
    ExtraPremiumCost = BASIC_PREMIUM - ExtraCarPremium
    ExtraCars = ExtraCarPremium * ICarQuantity

    FullPremium = BASIC_PREMIUM + ExtraCars

    while True:
        if UExtraLiability == "Y":
            AExtraLiability = 130
        elif UExtraLiability == "N":
            AExtraLiability = 0
        else:
            break
            
    while True:
            if UGlassCoverage == "Y":
                AGlassCoverage = 86
            elif UGlassCoverage == "N":
                AGlassCoverage = 0
            else:
                break

    while True:
        if UCarLoan == "Y":
            ACarLoan = 58
        elif UCarLoan == "N":
            ACarLoan = 0
        else:
            break

    FExtraLiability = AExtraLiability * ICarQuantity
    FGlassCoverage = AGlassCoverage * ICarQuantity
    FCarLoan = ACarLoan * ICarQuantity

    TotalExtra = FExtraLiability + FGlassCoverage + FCarLoan
    TotalInsurance = FullPremium + TotalExtra

    Taxes = TotalInsurance * HST
    FinalCost = TotalInsurance + Taxes

    DownPayCost = FinalCost - IDownPay
    TempMonthlyPay = DownPayCost + 39.99
    MonthlyPay = TempMonthlyPay / 8

# Output Results to User


# Any Outstanding Duties or Comments