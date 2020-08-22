# program to calculate the average of three quiz mark, and then output the result

def getIntValue(prompt, minimum, maximum) :
       goodValue = False
       while not goodValue :
              try :
                     lineOfInput = input(prompt)
                     value = int(lineOfInput)
                     if (value < minimum) or (value > maximum) :  # check to see if bad
                            print("Value out of range. Must be between", minimum, "and", maximum, "You entered", value)
                     else :
                            goodValue = True;
              except ValueError:
                     print("Non numeric characters entered. Must enter only numeric characters. You entered", lineOfInput)

       return value

def convertToLetterGrade(average) :
       if average >= 85 :
               return "A"
       elif average >= 70 :
              return "B"
       elif average >= 60 :
              return "C"
       elif average >= 56 :
              return "D"
       else :
              return "F"


# get input from the user consisting of their name and three marks

studentName = input("Please enter the name of the student: ")

#get the number of quizzes from the user

numberOfQuizzes = getIntValue("How many quizzes do you have? :", 1, 1000)

markTotal = 0
for i in range(0, numberOfQuizzes) :
       markTotal      += getIntValue("Please enter a mark: ", 0, 100)

average = markTotal / numberOfQuizzes
print(studentName, "has an average of", average, "which corresponds to a letter of", convertToLetterGrade(average))

