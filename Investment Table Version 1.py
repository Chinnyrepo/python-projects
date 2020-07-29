# program to generate compound interest for an initial principal amount
# and a fixed interest rate

# get user input and validate the input
principal  = float(input("What is your principal amount invested?: "))
while (principal <= 0): 
    print("******Wrong value entered. Principal must be a positive number")
    principal  = float(input("What is your principal amount invested?: "))
    
interest  = float(input("What is the annual interest rate (in percent)?: "))
while (interest <= 0): 
    print("******Wrong value entered. Interest must be a positive number")
    interest  = float(input("What is the annual interest rate (in percent)?: "))
    
year      = float(input("How many years will this be invested for?: "))
while (year <= 0): 
    print("******Wrong value entered. Year must be a positive number")
    interest  = float(input("How many years will this be invested for?: "))
    
interest = interest / 100

# output the principal with the respective year
currentYear = 1
print("Year", "    ","Balance")
while (currentYear <= year) :
    principal = (principal * (1 + interest))
    print("  {}      ${:.2f}".format(currentYear, principal))
    currentYear += 1    
    
  
   
   
