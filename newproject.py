# Description: 
# Author: Declan Derible
# Date(s): March 20th-22nd, 2024

# Define Required Libraries
import datetime
import FormatValues as FV
import extras as EX
outfile = open('data.txt', 'w')

# Main Program Begins
    # Define Program Constants

    # Gather User Inputs

CustomerFN = EX.FirstName("Enter your first name: ")

CustomerLN = EX.LastName("Enter your last name: ")

CustomerADD = EX.Address("Enter your address: ")

CustomerCITY = EX.City("Enter your city: ")

CustomerPROV = EX.Province("Enter your province: ")

CustomerPC = EX.PostalCode("Enter your postal code: ")

CustomerPHONE = EX.PhoneNumber("Enter your phone number")

outfile.write(EX.FirstName + '\n')
outfile.write(EX.LastName + '\n')
outfile.write(EX.Address + '\n')
outfile.write(EX.City + '\n')
outfile.write(EX.Province + '\n')
outfile.write(EX.PostalCode + '\n')
outfile.write(EX.PhoneNumber + '\n')
outfile.close()