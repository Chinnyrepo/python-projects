# program to generate compound interest for an initial principal amount
# and a fixed interest rate

SENTINEL = 0

# get user input and validate the input
principal  = float(input("What is your principal amount invested?: "))
while (principal <= 0): 
    print("******Wrong value entered. Principal must be a positive number")
    principal  = float(input("What is your principal amount invested?: "))
    
interest  = float(input("What is the interest rate for year 1 (in percent)?: "))/100
while not (interest > 0) : 
    print("******Wrong value entered. Interest must be a positive number")
    interest  = float(input("What is the interest rate for year 1 (in percent)?: "))/100

# process this value in a while loop to get the required interest rate
count = 1
compoundInterest = principal
while interest != SENTINEL :
    compoundInterest = compoundInterest * (1 + interest)
    count += 1
    interest  = float(input("What is the interest rate for year {} (in percent)?: ".format(count)))/100

averageYearlyIncome = (compoundInterest - principal) / count

# display the final result
print(f"At the end of 3 years, your investment will be worth ${compoundInterest:.2f} Your average yearly income is {averageYearlyIncome:.2f}")


    
    


   
   
