# Program Name:     Bilbo's Eggs Wholesaler Price Calculator
#
# Author:           Scott Thornton
#
# Date:             10-January-2020
#
# Description:      Demonstration program for SAIT CPRG 100 (Manpower)
#
#                   prompt the user for the number of eggs they
#                   are planning to buy. Using an if elif ladder determine the
#                   price per egg
#
#                   once we know the price per egg we can determine the total
#                   bill and produce some output
#


# first ask how many eggs they wish to buy

numberOfEggs = int(input("How many eggs do you wish to purchase? :"))
if numberOfEggs <= 0 :
    print("You must buy a positive amount of eggs!!")
    quit()

# convert the eggs to the number of whole dozen and then use a ladder to
# determine the price

dozens = numberOfEggs // 12  # note we are doing integer division here

if dozens < 4 :
    pricePerDozen = 0.50
elif dozens < 6 :
    pricePerDozen = 0.45
elif dozens < 11 :
    pricePerDozen = 0.40
else :
    pricePerDozen = 0.35

# now mulitply the toal number of eggs by the perDozen price divided by 12

pricePerEgg = pricePerDozen / 12
totalCost = numberOfEggs * pricePerEgg

# now format and output results

print("Your cost is ${:.2f} per dozen or ${:.3f} per egg.".format(pricePerDozen, pricePerEgg))
print("Your bill comes to ${:.2f}".format(totalCost))
