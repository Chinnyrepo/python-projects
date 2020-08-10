# Program Name:     Triangle Area Version 1
#
# Author:           Scott Thornton
#
# Date:             10-January-2020
#
# Description:      Demonstration program for SAIT CPRG 100 (Manpower)
#
#                   Compute the area of a triangle by first asking for the base length, then the height length.
#                   Calculate and store the average. When the output is done, use the .format() method to ensure
#                   the area is only displayed to two decimal places. Use default codes for all the other values, as
#                   the specification does not say to do anything with them.
#
#                   NOTE: This is version 1 of a sequence of changes that make that make the program more robust
#                   in terms of accepting invalid input. THe assumption here is that the user is "kind" and only gives
#                   valid numerical values as input
#

baseLength     = float(input("Please enter triangle base length (cm) : "))
triangleHeight = float(input("Please enter triangle base length (cm) : "))

area           = (0.5 * baseLength * triangleHeight) / (100 * 100)  # convert to square metres

print("A triangle with base {} cm and height {} cm has an area of {:.2f} square metres".format(baseLength, triangleHeight, area))
