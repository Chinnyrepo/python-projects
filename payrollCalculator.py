# Program Name:     Payroll Calculation
#
# Author:           Chinenye Okpalanze
#
# Date:             24-June-2020
#
# Description:      Prepare a Pay Slip to be included in a cheque envelope for the employees of a small business.
#                   The Pay Slip will also be used by the accountant to prepare the actual pay-cheques,

# Define a function to get the number of hours worked by the employee and carry out data validation
def getnumberOfHours(prompt, minimum, maximum) :
    goodValue = False
    while not goodValue :
              try :
                     lineOfInput = input(prompt)
                     value = float(lineOfInput)
                     if (value < minimum) or (value > maximum) :  
                            print("Value out of range. Must be between", minimum, "and", maximum, "You entered", value)
                     else :
                            goodValue = True;
              except ValueError:
                     print("Non numeric characters entered. Must enter only numeric characters. You entered", lineOfInput)

    return value
       
# Define a function to get the rate of pay of the employee and carry out data validation
def getRateOfPay(prompt, minimum, maximum) :
    goodValue = False
    while not goodValue :
              try :
                     lineOfInput = input(prompt)
                     value = float(lineOfInput)
                     if (value < minimum) or (value > maximum) :  
                            print("Value out of range. Must be between", minimum, "and", maximum, "You entered", value)
                     else :
                            goodValue = True;
              except ValueError:
                     print("Non numeric characters entered. Must enter only numeric characters. You entered", lineOfInput)

    return value

# Define a function to get deduction percentage of the employee and carry out data validation
def getdeductionPercentage(prompt, minimum, maximum) :
    goodValue = False
    while not goodValue :
              try :
                     lineOfInput = input(prompt)
                     value = int(lineOfInput)
                     if (value < minimum) or (value > maximum) :  
                            print("Value out of range. Must be between", minimum, "and", maximum, "You entered", value)
                     else :
                            goodValue = True;
              except ValueError:
                     print("Non numeric characters entered. Must enter only numeric characters. You entered", lineOfInput)

    return value


# Define a function to get the tax deduction of the employee and carry out data validation
def getTaxExemptStatus(prompt) :
    goodValue = False
    while not goodValue :
                try :
                     lineOfInput = input(prompt)                     
                     if (lineOfInput == "Y") or (lineOfInput == "N") : 
                         goodValue = True
                     elif (lineOfInput == "y") or (lineOfInput == "n") :  
                         goodValue = True                                               
                     else :
                         print("Value entered is invalid, you must enter Y or N. you entered", lineOfInput)
                except ValueError:
                     print("Value entered is invalid, you must enter Y or N. you entered", lineOfInput)

    return lineOfInput
    
print("Welcome to Payslip calculator page")
print("Please provide the following employees information")

# get user input for the employee
employeeFirstName = input("Please enter the First Name of the employee?  : ")
employeeLastName = input("Please enter the Last Name of the employee?  : ")


numberOfHours = getnumberOfHours("How many Hours did the employee work?  : ", 1, 10000)

rateOfPay = getRateOfPay("What is the rate of pay for the employee per hour?  : ", 1, 1000)

# apply deduction amount based on the input provided by the user
taxExemptStatus = getTaxExemptStatus("Is the employee tax exempt? [Y/N]  : " )
if taxExemptStatus == "N" or taxExemptStatus == "n":
    taxExemptStatus = True
    deductionPercentage = getdeductionPercentage("What is the percentage of the gross pay deducted? [Enter whole numbers]  : ", 1, 100)/100
elif taxExemptStatus == "Y" or taxExemptStatus == "y":
    taxExemptStatus = False
    deductionPercentage = 0
else:
     print("You must answer either Y or N. You entered", taxExemptStatus)

     

# calculation of the requires variables

grossPay = numberOfHours * rateOfPay   
totalDeduction = grossPay * deductionPercentage
netPay = grossPay - totalDeduction


# format and output the result

print("\n********* The Following is the Employee's Payslip ****************\n")
print("{:<25}  {} {}".format("Employee's Name", employeeFirstName, employeeLastName))
print("{:<25}   {:,.2f}".format("Number of Hours worked", numberOfHours))
print("{:<25}  ${:,.2f}".format("Hourly pay", rateOfPay))
print("{:<25}  ${:,.2f}".format("Gross Pay", grossPay))
print("{:<25}   {:,.2f}".format("Percentage Deducted", deductionPercentage))
print("{:<25}  ${:,.2f}".format("Amount Deducted", totalDeduction))
print("{:<25}  ${:,.2f}".format("Net Pay", netPay))
print("\n******************************************************************\n")

