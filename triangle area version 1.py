# Program Name:     Triangle Area Version 1
#
# Author:           Chinenye Okpalanze
#
# Date:             10-January-2020
#
# Description:      Compute the area of a triangle by first asking for the base length, then the height length.
#                   Calculate and store the average. 
#

baseLength     = float(input("Please enter triangle base length (cm) : "))
triangleHeight = float(input("Please enter triangle base length (cm) : "))

area           = (0.5 * baseLength * triangleHeight) / (100 * 100)  # convert to square metres

print("A triangle with base {} cm and height {} cm has an area of {:.2f} square metres".format(baseLength, triangleHeight, area))
