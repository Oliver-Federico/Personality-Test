from random import randint
import sys
#if current person is chosen as middle
LM = lambda number: "a" if number >= 1 and number <= 4 else ("b" if number >= 5 and number <= 8 else "-")

#if current person is chosen as extrovert
LE = lambda number: "a" if number >= 1 and number <= 5 else("b" if number >= 6 and number <= 8 else "-")

#if current person is chosen as introvert
LI = lambda number: "a" if number >= 1 and number <= 3 else("b" if number >=4 and number <= 8 else "-")

#you can change how many tests to generate from command line
try:
    participants = int(sys.argv[1])
except:
    participants = 20

#open file to get a list of all possible names
names = open("USAnames.txt", "rt")
names_list = names.readlines()
names.close()

#opens the file in which you will output all generated tests
outputFile = open("personality.txt", "at")

#this for loop will create all generated participants
for i in range(participants):
    #system allows for random first and last name
    randnum1 = randint(1,2001)
    randnum2 = randint(1,2001)
    nameFirst = names_list[randnum1].replace('\n', "")
    nameLast = names_list[randnum2].replace('\n',"")

    #writes the first and last name in the output file
    outputFile.write(nameFirst + " " + nameLast + "\n")

    #chooses if the person will be Introvert, Extrovert, and Middle
    introvert_o_extrovert = lambda n: "Extrovert" if n == 1 else ("Introvert" if n == 2 else "Middle")
    IOE = introvert_o_extrovert(randint(1,3))

    #loop is responsable for generating each character of the test results
    for x in range(70):
        #checking if the current person is Introvert, Extrovert, or Middle 
        valididate_IOE = lambda IOE:LE(randint(1,9))if IOE=="Extrovert"else(LI(randint(1,9))if IOE=="Introvert"else LM(randint(1,9)))
        letter = valididate_IOE(IOE)

        #outputs the letter
        outputFile.write(letter)
    outputFile.write("\n")
outputFile.close()

