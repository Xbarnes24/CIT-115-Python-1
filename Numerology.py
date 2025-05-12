
#class file

class Numerology:
    def __init__(self, sName, sDOB):

        self.name = sName
        self.birthdate = sDOB


        self.lifePath = 0
        for letter in self.birthdate.replace("-", "").replace("/", ""): #"03/10/1995"
            #print(letter)
            self.lifePath += int(letter)
        self.lifePath = self.reduceNumber(self.lifePath)
        #print(f"Life Path: {self.lifePath}")


        self.birthday = 0
        iBirthdayDay = int(self.birthdate[3:5])
        #print(iBirthdayDay)
        self.birthday = self.reduceNumber(iBirthdayDay)
        #print(f"Birthday: {self.birthday}")


        self.iAttitude = 0
        for strNumber in self.birthdate.replace("-", "").replace("/", "")[:4]:
            #print(strNumber)
            self.iAttitude += int(strNumber)
        #print(self.iAttitude)
        self.iAttitude = self.reduceNumber(self.iAttitude)
        #print(f"Attitude: {self.iAttitude}")






        #----------------------------------------------------

        """
        A, J, S 1 
        B, K, T 2 
        C, L, U 3 
        D, M, V 4 
        E, N, W 5 
        F, O, X 6 
        G, P, Y 7 
        H, Q, Z 8 
        I, R 9 
        """

        # self.dictCharacters =   {("A", "J", "S"):1,
        #                          ("B", "K", "T"):2,
        #                          ("C", "L", "U"):3,
        #                          ("D", "M", "V"):4,
        #                          ("E", "N", "W"):5,
        #                          ("F", "O", "X"):6,
        #                          ("G", "P", "Y"):7,
        #                          ("H", "Q", "Z"):8,
        #                          ("I", "R")     :9}


        self.dictCharacters = { "A":1, "J":1, "S": 1,
                                "B":2, "K":2, "T": 2, 
                                "C":3, "L":3, "U": 3, 
                                "D":4, "M":4, "V": 4, 
                                "E":5, "N":5, "W": 5, 
                                "F":6, "O":6, "X": 6, 
                                "G":7, "P":7, "Y": 7, 
                                "H":8, "Q":8, "Z": 8, 
                                "I":9, "R":9}
        
    
        self.soul = 0
        self.personality = 0

        for sLetter in self.name.upper(): 

            #print(sLetter)

            #print(self.dictCharacters.get(sLetter, 0))

            if sLetter in "AEIOU":

                #print(sLetter)
                self.soul += self.dictCharacters.get(sLetter, 0)

            else:
                #print(sLetter)
                self.personality += self.dictCharacters.get(sLetter, 0)


        #print(self.soul)
        self.soul = self.reduceNumber(self.soul)
        #print(self.soul)

        #print(self.personality)
        self.personality = self.reduceNumber(self.personality)
        #print(self.personality)


        self.power = 0
        #8 (Soul) + 5 (Personality)
        self.power = self.reduceNumber(self.soul + self.personality)
        #print(self.power)



        """
        Soul Number: Is computed by taking all the vowels (A,E,I,O,U) in the inputted birth name adding them together.   
        The Soul Number is supposed to denote what a person feels on the inside. 
        For example: 
        I A A I O are the vowels in Brian Candido would be computed as: 9+1+1+9+6 = 26 
        26 would then be reduced again by 2+6 = 8 and 8 would be the Soul Numbe
        """




        #


    def reduceNumber(self, iNumber):
        strNumber = str(iNumber)
        while len(strNumber) > 1:
            iNumber = int(strNumber[0]) + int(strNumber[1])
            strNumber = str(iNumber)
        #print(iNumber)
        return iNumber


    def getName(self):
        return self.name
    
    def getBirthdate(self): #03-10-1995
        return self.birthdate
    

    def getLifePath(self):
        return self.lifePath
    
    def getBirthday(self): # 6
        return self.birthday
    
    def getAttitude(self):
        return self.iAttitude
    
    def getSoul(self):
        return self.soul
    
    def getPersonality(self):
        return self.personality
    
    def getPower(self):
        return self.power

    def __str__(self):
        return f"""
        Name: {self.getName()}
        Birthdate: {self.getBirthdate()}
        Life Path: {self.getLifePath()}
        Birthday: {self.getBirthday()}
        Attitude: {self.getAttitude()}
        Soul: {self.getSoul()}
        Personality: {self.getPersonality()}
        Power: {self.getPower()}"""


"""
Test Name: John Smith  
Test DOB: 03/15/1962 
Life Path Number:  9 
Birth Day Number:  6 
Attitude Day Number:  9 
Soul Number:   6 
Personality Number:  2 
Power Name Number:  8
"""

#myNumerologyObject = Numerology("Brian Candido", "04-04-2001")

#myNumerologyObject.getpower()


# class NumerologExtended(Numerology):
#     pass


"""
The output will be six numbers.  Since the art of numerology is based off the numbers derived from a person’s birth 
date and name code needs to be written to compute these numbers.   
 The Birthday Number, Life Path Number and the Attitude Number are computed from the inputted Birth 
Date. 
 The Soul Number, Personality Number and Power Name Number are derived from the Inputted name.  
 
You will have to code TWO Python source files:   
1. Numerology.py that has the class in it and these function (coding details provided below): 
 _init__(sName, sDOB) 
 getName() – returns the subjects name 
 getBirthdate() – returns the subjects Date of Birth 
 getAttitude() – returns the computed attitude number 
 getBirthDay() – returns the computed birthday number 
 getLifePath() – returns the computed life path number 
 getPersonality() – returns the computed personality number 
 getPowerName () – returns the computed power name number 
 getSoul() – returns the computed soul number 
2. Use Numerology.py that will prompt for the user name and birthday and then use the Numerology class to 
get the computed numbers: 
 The two things that are needed to perform a reading is a person’s birth date in mm-dd-yyyy format 
and birth name.  The inputted date should be tested to verify that it is entered as a full 8 digit date 
with dashes or slashes (- or /) as separators.    
 The inputted name should be populated and not empty.   
 Call the Numerology class’ __init__ and each function to get the calculated results 
 Output each of the findings to the screen.  
 
 
Numbers Derived From Birth Date: 
Life Path Number: Is computed by taking all the digits in the inputted birth date and adding them together.   The 
Life Path Number is supposed to denote what a person is to be or perform in this life.  For example: 
 
03-15-1996 would need to be computed: 0+3+1+5+1+9+9+6 = 34 
 
34 would then be reduced again by 3+4 = 7 and 7 would be the Life Path Number 
 
Note: You must reduce every number in numerology down to a single digit.  It is recommended that you 
write a method that will accept in a number as a parameter and you write code to reduce the number down 
to a single digit which the function will return as it’s result.  Keep in mind a number may need to be 
reduced more than once.  The function needs to return back a single digit between 1 and 9.  Do you think 
this method should be a made public or private? 
 
                C       Python          Professor Brian Candido                            Chapter 10 Classes 2 
Birth Day Number: Is simply the extraction of the day from the birth date.  You can assume you are entering the 
date in USA format (mm-dd-yyyy).  The Birth Day Number is supposed to contribute to finding the match of your 
soul mate.  For example:  
 
03-29-1971 would be computed: 2+9 = 11 
11 would then be reduced again by 1+1 = 2 and 2 would be the Birth Day Number. 
 
Attitude Number: Is simply the addition of the birth month and the birth day from the birth date.  You can assume 
you are entering the date in USA format (mm-dd-yyyy).  The Attitude Number is supposed to determine a person’s 
attitude that will reinforce or detract from a person’s life path number. For example:   
04-04-2001 would be computed: 0+4+0+4 = 8 This is the Attitude number. 
 
In this example no further reduction is needed: the number is a single digit between 1 and 9.











Numbers Derived From Birth Name: 
To perform these computations you must first convert the letters to a corresponding number.  Here is a conversion 
grid: 
 
A, J, S 1 
B, K, T 2 
C, L, U 3 
D, M, V 4 
E, N, W 5 
F, O, X 6 
G, P, Y 7 
H, Q, Z 8 
I, R 9 
 
Note: Only convert characters A – Z.  If the character to be evaluated is not between A and Z you will need to use a 
0 (zero) for that character.  It is recommended that you convert the value to either lower case or upper case to reduce 
the coding of both lower and upper case values. 
 
For example: Brian Candido would compute to 29915 3154946 
 
    91        1      9   6 
BRIAN CANDIDO 
29      5  3    54   4 
 
Soul Number: Is computed by taking all the vowels (A,E,I,O,U) in the inputted birth name adding them together.   
The Soul Number is supposed to denote what a person feels on the inside. For example: 
 
I A A I O are the vowels in Brian Candido would be computed as: 9+1+1+9+6 = 26 
 
26 would then be reduced again by 2+6 = 8 and 8 would be the Soul Number 
 
Personality Number: Is computed by taking all the consonants (letters that are not A,E,I,O,U) in the inputted birth 
name adding them together.   The Personality Number is supposed to denote how a person portrays themselves to 
the outside world. For example: 
 
B R N C N D D are the consonants in Brian Candido would be computed as: 2+9+5+3+5+4+4 = 32 
 
32 would then be reduced again by 3+2 = 5 and 5 would be the Personality Number. 
 
Power Name Number: Is computed by adding the Soul Number and the Personality Number together.   The Power 
Name Number is supposed to denote how the Soul and Personality Numbers interact for a person. For example: 
 8 (Soul) + 5 (Personality) = 13 reduced would be 4 which is the power name number.


"""