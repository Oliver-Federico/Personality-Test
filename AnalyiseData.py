#Stupid imports
import sys
from pyfiglet import Figlet
figlet = Figlet()
#unused variable go boop
all_test_responses = []
def main():
    #file opening then getting a list of all answers then getting the length then closing
    answers = open("personality.txt", "rt")
    all_answers = answers.readlines()
    answer_doc_len = len(all_answers)
    answers.close()

    #Checks how many different test have been completed
    outputs = 0

    #opens the output file and deletes all prior contents
    fileOutput = open("output.txt", "wt")
    fileOutput.write("")

    while outputs < answer_doc_len:
        #Proccess data gets the current test into a list of 10 sets of 7
        userName, currentResponseList = processData(all_answers, outputs)

        #calculation counts how many A,B and - are in a given string from the 10 sets of 7 list
        ein, sin, tfn, jpn = calculations(currentResponseList)

        #converts the number of each into a precentage score then converted into numbers of personality types
        feis, fsis, ftfs, fjps = analyise(ein,sin,tfn,jpn)

        #stupid convert float - int - string
        
        ein = str(int(round(ein)))
        sin = str(int(round(sin)))
        tfn = str(int(round(tfn)))
        jpn = str(int(round(jpn)))

        #outputs the current test results into a file called output.txt
        output(ein, sin, tfn, jpn, feis, fsis, ftfs, fjps, userName)

        #adds 2 to the outputs completed because the line is on line one and the test is on line 2
        outputs = outputs + 2

def processData(all_tests, outputsCompleted):
    #current test in a list in 10 sets of 7 characters
    currentResponseList = []

    #gets the name of the test you are looking at
    name = all_tests[outputsCompleted].replace('\n', "")

    #gets the current test in string format (aabbababababab ect) 
    currentTestResponseSTR = all_tests[outputsCompleted+1].replace('\n', "")
    currentTestResponseSTR = currentTestResponseSTR.upper()

    #loops up to 70, 10 groups of 7 characters
    for x in range(0,70,7):
        #appends the group of 7 characters one after another
        currentResponseList.append(currentTestResponseSTR[x:x+7])
    
    #returns the name then the list of characters in the test 10 groups of 7
    return name, currentResponseList

def calculations(currentTestList):
    #count of first character of each of the 10 groups of 7
    numA0=0
    numB0=0
    num_dash0=0

    #count of first - thirds of each of the 10 groups of 7
    numA13=0
    numB13=0
    num_dash13=0

    #count of third - fifth of each of the 10 groups of 7
    numA35=0
    numB35=0
    num_dash35=0

    #count of the fifth - sevent of each of the 10 groups of 7
    numA57=0
    numB57=0
    num_dash57=0
    
    #for each of the 10 groups count the As, Bs, and -s
    for q in range(len(currentTestList)):
        #count of first character of each of the 10 groups of 7
        numA0 = numA0 + currentTestList[q][0].count("A")
        numB0 = numB0 + currentTestList[q][0].count("B")
        num_dash0 = num_dash0 + currentTestList[q][0].count("-")

        #count of first - thirds of each of the 10 groups of 7
        numA13 = numA13 + currentTestList[q][1:3].count("A")
        numB13 = numB13 + currentTestList[q][1:3].count("B")
        num_dash13 = num_dash13 + currentTestList[q][1:3].count("-")

        #count of third - fifth of each of the 10 groups of 7
        numA35 = numA35 + currentTestList[q][3:5].count("A")
        numB35 = numB35 + currentTestList[q][3:5].count("B")
        num_dash35 = num_dash35 + currentTestList[q][3:5].count("-")

        #count of the fifth - sevent of each of the 10 groups of 7
        numA57 = numA57 + currentTestList[q][5:7].count("A")
        numB57 = numB57 + currentTestList[q][5:7].count("B")
        num_dash57 = num_dash57 + currentTestList[q][5:7].count("-")

    #converts introvert extrovert data into precent
    extrovert_introvert_number = (numB0 / (numB0+numA0)) * 100

    #converts sensing intuition data into precent
    sensing_intuition_number = (numB13 / (numB13+numA13)) * 100

    #converts thinking feeling data into precent
    thinking_feeling_number = (numB35 / (numA35+numB35)) * 100

    #converts judging preceiving data into precent
    judging_preceiving_number = (numB57 / (numA57+numB57)) * 100

    #returns precentage of each of each of values
    return extrovert_introvert_number, sensing_intuition_number, thinking_feeling_number, judging_preceiving_number

def analyise(ein, sin, tfn, jpn):
    #checks if the extrovert introvert score is more towards the Extrovert, Introvert, or Middle
    eis = lambda score_number: "I" if score_number > 50 else ("X" if score_number == 50 else "E")

    #checks if the Intuition Sensing score is more towards the Intuition, Sensing, or Middle
    sis = lambda score_number: "N" if score_number > 50 else ("X" if score_number == 50 else "S")

    #checks if the Feeling Thinking score is more towards the Feeling, Thinking or Middle
    tfs = lambda score_number: "F" if score_number > 50 else ("X" if score_number == 50 else "T")

    #checks if the Preceiving Judging score is more toward Preceiving, Judging, or Middle
    jps = lambda score_number: "P" if score_number > 50 else ("X" if score_number == 50 else "J")
    
    #outputs Introvert Extrovert score
    final_extrovert_introvert_score = eis(ein)

    #outputs Sensing Intuition score
    final_sensing_intuition_score = sis(sin)

    #outputs Thinking Feeling score
    final_thinking_feeling_score = tfs(tfn)

    #outputs Judging Preceiving score
    final_judging_preceiving_score = jps(jpn)

    #Returns all scores as strings
    return final_extrovert_introvert_score, final_sensing_intuition_score, final_thinking_feeling_score, final_judging_preceiving_score

def output(ein, sin, tfn, jpn, feis, fsis, ftfs, fjps, name):
    #adds all the score% together into one list for easy formatting
    score_list = [ein, sin, tfn, jpn]

    #adds all the letter string score into format like: ESFP
    score = " = " + feis + fsis + ftfs + fjps

    #creates the section of the output that displays the name
    nameSection = name + ": "

    #adds all of the parts of the formatting together then gets rid of these: ' because they are printed when list formatting
    #which is stupid lol
    final = nameSection + str(score_list) + score
    final = final.replace("'","")

    #outputs the current test results into an file called output.txt
    fileOutput = open("output.txt", "at")
    fileOutput.write(final + "\n")

main()