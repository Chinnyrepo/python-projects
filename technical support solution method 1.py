# Program Name:     Technical Support Assistant
#
# Author:           Chinenye Okpalanze
#
# Date:             17-June-2020
#
# Description:      Ask the user if their computer beeps when powered on, and whether
#                   the hard-drive spins.
#

# first get the input by asking if their computer beeps and whether the drive spins (expecting the user
# to enter either Y or N (either case) if the device does what is asked

answer = input("Does the computer beep when powered on? [Y/N] :")
if answer == 'Y'  or  answer == 'y' :
    computerBeeps = True
elif answer == 'N' or answer == 'n' :
    computerBeeps = False
else :
    print("You must answer either Y or N. You entered ", answer)
    quit()

answer = input("Does the hard-drive spin when powered on? [Y/N] :")
if answer == 'Y'  or  answer == 'y' :
    driveSpins = True
elif answer == 'N' or answer == 'n' :
    driveSpins = False
else :
    print("You must answer either Y or N. You entered ", answer)
    quit()

# now that we have the input, use a nested if's to decide what message to print

if computerBeeps :
    if driveSpins :
        print("Contact Tech Support.")
    else :
        print("Check drive cables.")
else :
    if driveSpins :
        print("Check the speaker contacts.")
    else :
        print("Bring computer to repair centre.")

