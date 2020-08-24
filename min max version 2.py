# program to find minimum and maximum of a list of numbers being
# entered one at a time

SENTINEL = 999

#get the first value, validate it and set the initial minimum/maximum values

value   = int(input("Enter a value (999 if done) :"))
while not ( ((value >= -100) and (value <= 100)) or (value == SENTINEL) ) :
    print("*** Bad value entered.  Must be between -100 and 100")
    value   = int(input("Enter a value (999 if done) :"))

maximum = value
minimum = value

#process this value in a while loop, waiting for a sentinel value
#if the value we got is bigger/smaller than the max/min we have seen
#so far, update those variables

while value != SENTINEL :
    if value > maximum :
        maximum = value
    if value < minimum :
        minimum = value

    value   = int(input("Enter a value (999 if done) :"))
    while not ( ((value >= -100) and (value <= 100)) or (value == SENTINEL) ) :
        print("*** Bad value entered.  Must be between -100 and 100")
        value   = int(input("Enter a value (999 if done) :"))


# display the final results

if maximum == SENTINEL :
    print("No data entered")
else :
    print("the maximum value is ", maximum)
    print("the minimum value is ", minimum)
