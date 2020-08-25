# Program Name:     Technical Support Assistant
#
# Author:           Chinenye Okpalanze
#
# Date:             21-June-2020
#
# Description:      Demonstration program for SAIT CPRG 100 (Manpower)
#
#                   As the user if their computer beeps when powered on, and whether
#                   the hard-drive spins.
#
#                   Then based on the four possible answers, produce an appropriate message telling
#                   the user the first step in trying to fix their computer
#
#                  
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

# now that we have the input, use an if elif ladder to decide what to print

if computerBeeps and driveSpins :
        print("Contact Tech Support.")
elif computerBeeps and not driveSpins :
        print("Check drive cables.")
elif not computerBeeps and driveSpins :
        print("Check the speaker contacts.")
elif not computerBeeps and not driveSpins :
        print("Bring computer to repair centre.")

