sName = input("What is your name: ")

iTest1 = int(input("Enter a test score 1: "))
iTest2 = int(input("Enter a test score 2: "))
iTest3 = int(input("Enter a test score 3: "))
iTest4 = int(input("Enter a test score 4: "))

if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0")
    exit()

#Wrote sLowest_Grade below instead of under the test scores to make the process easier.

sLowest_Grade = input("Do you wish to drop the lowest grade Y or N?: ")

if sLowest_Grade not in ["Y", "N"]:
    print ("Enter Y or N to drop the lowest grade.")
    exit()

if sLowest_Grade == "Y" :
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        fAverage = (iTest2 + iTest3 + iTest4) / 3.0
        
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        fAverage = (iTest1 + iTest3 + iTest4) / 3.0

    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        fAverage = (iTest1 + iTest2 + iTest4) / 3.0

    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        fAverage = (iTest1 + iTest3 + iTest4) / 3.0

    elif iTest4 <= iTest1 and iTest4 <= iTest2 and iTest4 <= iTest3:
        fAverage = (iTest1 + iTest2 + iTest3) / 3.0

    else: fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4.0

    fAverage = round(fAverage, 1)

#Averages that equal letter grades.  

if fAverage >= 97.0:
    sGrade = "A+"
elif fAverage >= 94.0 and fAverage <= 96.9:
    sGrade = "A"
elif fAverage >= 90.0 and fAverage <= 93.9:
    sGrade = "A-"
elif fAverage >= 87.0 and fAverage <= 89.9:
    sGrade = "B+"
elif fAverage >= 84.0 and fAverage <= 86.9:
    sGrade = "B"
elif fAverage >= 80.0 and fAverage <= 83.9:
    sGrade = "B-"
elif fAverage >= 77.0 and fAverage <= 79.9:
    sGrade = "C+"
elif fAverage >= 74.0 and fAverage <= 76.9:
    sGrade = "C"
elif fAverage >= 70.0 and fAverage <= 73.9:
    sGrade = "C-"
elif fAverage >= 67.0 and fAverage <= 69.9:
    sGrade = "D+"
elif fAverage >= 64.0 and fAverage <= 66.9:
    sGrade = "D"
elif fAverage >= 60.0 and fAverage <= 63.9:
    sGrade = "D-"
else:
    sGrade = "F"

print(f"{sName}'s Average: {fAverage:.1f}, Letter Grade: {sGrade}")

               
    


