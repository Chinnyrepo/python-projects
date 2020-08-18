# Program Name:     Triangle Area Version 2
#
# Author:           Chinenye Okpalanze
#
# Date:             19-June-2020
#
# Description:      Triangle Area Version 2 with Validation
#                   
#


baseLength     = float(input("Please enter triangle base length (cm) : "))
if baseLength <= 0 :
    print("***Error ... base length must be greater than zero. You entered", baseLength)
    quit()
    
triangleHeight = float(input("Please enter triangle height length (cm) : "))
if triangleHeight <= 0 :
    print("***Error ... triangle height length must be greater than zero. You entered", triangleHeight)
    quit()

# calculate the area and output the results

area           = (0.5 * baseLength * triangleHeight) / (100 * 100)  # convert to square metres
print("A triangle with base {} cm and height {} cm has an area of {:.2f} square metres".format(baseLength, triangleHeight, area))
