# Personality Test Analyzer
Welcome to PTARM (Personality Test Analyzer Read Me) in this read me file you will learn how to use the PTARM and how it works. 

The PTARM is a data analyzer that analyzes the data from the [Keirsey Personality Test](https://www.keirsey.com/). It scores you on 4 categorys, Introvert or extrovert (IE), Sensing or Intution (SE), Thinking or Feeling (TF), Judging or Preceiving (JP).

## How the the PTRAM works
The first step in using the PTARM is understanding the files given. When you open the repository you are greeted 6 files (excluding README.md), 3 text files and 3 python files. Each file is very important for the operation of the PTARM.

### PTARM .txt files


### output.txt
The output.txt file is the file that has the test results. They are formated in this way:

name: [IE number, SN number, TF number, JP number] = I or E, S or N, T or F, J or P

The IE number is precentage of introvert that the person is. The closer to 100 the more introverted they are, if they are less than 50 they are more extroverted.
The output result of this is put at the first character after the equal sign. The characer will be abbreviated (Introverted: I, Extroverted: E)

The SN number is precentage of iNtution that the person is. The closer to 100 the more Intution they have, if they are less than 50 they are more Sensing.
The output result of this is put at the second character after the equal sign. The characer will be abbreviated (Sensing: S, iNtuition: N)

The TF number is precentage of feeling that the person is. The closer to 100 the more feeling they are, if they are less than 50 they are more thinking.
The output result of this is put at the third character after the equal sign. The characer will be abbreviated (Thinking: T, Feeling: F)

The JP number is precentage of preceiving that the person is. The closer to 100 the more preceiving they are, if they are less than 50 they are more judging.
The output result of this is put at the last character after the equal sign. The characer will be abbreviated (Judging: J, Preceiving: P)

For all of these categorys if the number is 50 than an X will he displayed in the output meaning they are equally both.

##### Real examples:

Erin Blake: [78, 37, 61, 35] = ISFJ

Ben Carlson: [46, 45, 23, 90] = ESTP

Terry McClintic: [50, 37, 12, 58] = XSTP

### personality.txt
The personality.txt file is the file that takes the input tests that need to be processed by the PTARM. What you will input into the file goes as follwed:

Line 1: Name

Line 2: 70 Character long test answers 

The name is as said, the name of the particpant you are processing the test of. 
The 70 Character long test answers are the A, B, and -'s of the answers given. The -'s mean that the person did not answer the question.
You can have as many tests processed at once as your computer can handle. 

#### IMPORTANT:
The first test entry must start on line one, if it is not on line one you will recieve an error with your output.txt file.

##### Real examples:

line 1: Kenna Kashton

line 2: bbaab-bbba-bbbbbbaaabbbabbbb-abbabbbaaabbbbbaaaa-bbababbb-baabab-abb-a

line 3: Ramona Aila

line 4: aaab-babbbaaabb-aabbbbbba-baaabababbbaba-baabaab-abbababab-ababaaabaa-

line 5: Theo Gia

line 6: bb-bbaaa--aa-bba-babbaaaaabababb-aabbaa-aaabaaaaaabb-bbbaababaa-aaabaa

### USAnames.txt
The USAnames.txt file is only used if you want to generate tests of non real people. It contains 1000 of the most popular male names in the United States and 1000 of the most popular female names in the United States.



## Python Scripts

### AnalyiseData.py
This file is the the main file you will be working with when using the PTARM. This file takes in the data given in the personality.txt file and outputs the results into the output.txt file.

#### "main" function
  The main function is like most functions named main, it controls the overall function of the entire script running through different functions and output to get an     end result. Here is a simplifed version of the main functions steps:
  
*   Step 1. The function opens the personality.txt file and gets all the answers given in the text file and puts them in a list.
*   Step 2. The function creates a variable that counts how many outputs have been completed (starts at 0).
*   Step 3. The function opens the output file and deletes all prior data. If you don't want this open the file and delete lines 17,18, and 19.
*   Step 4. The function creates a while loop that only changes when the outputs is less than the length of the personality.txt document. Everything else after this    step is completed within the while loop.
*   Step 5. The function runs another function called processData (see documentation below) to get the current test participants name, and a list of current response   we are looking at (the 70 character A, B, -'s) and splits it into 10 groups of 7.
*   Step 6. The function runs another function called calculations (see documentation below) which returns the number for the introvert or extrovert, sensing or intutition, thinking or feeling, and judging or preceiving.
*   Step 7. The function runs another function called analyise (see documentation below) to return the letter that corresponds to the score given for each category.
*   Step 8. The function converts the number score of each category into a string to be manipulated.
*   Step 9. The function runs another function called output (see documentation below) which takes in all the data we just got from the other functions and outputs them into the output.txt file.
*   Step 10. The function adds 2 to that output variable we made because each test and name takes up 2 lines of the personality.txt file.
*   Step 11. The while loop continues until the outputs is less than the length of the personality.txt file.


#### "processData" function
  The processData function is a function that takes in all the test answers as a list and how many outputs have been completed to output the current test as a list of 10 groups of 7 and the current participants name. It does this in 4 simple steps:
  
*   Step 1. The current particpants name is found by looking at the all tests list and looking at the index of the how many outputs have been completed. This correlates to the line in which the name will be on for the test we are trying to process, giving us the current participants name.
*   Step 2. The function then goes to the index that is one higher than the outputs completed to find the current test we are trying to process, storing it in a list.
*   Step 3. The function will then split that list into 10 groups of 7.
*   Step 4. The function outputs the name, and that list which is split in 10 groups of 7.


#### "calculations" function
  The calculations function will calculate the given particpants IE, SN, TF, and JP number and output it. Here are the steps it takes:
  
*   Step 1. The function will first create 4 groups of variables corresponding to the questions in each of the 10 groups of 7. The first group being the number of A, B, and -'s in the first index (index 0 because it is zero based) of each of the 10 groups of 7. We need this because is what will give us the particpants IE number. The second group corresponds to the number of A, B, and -'s in the index between 1 - 3 which correspond to the SN number. The third group corresponds to the number of A, B, and -'s in the index between 3 - 5 which correspond to the TF number. The second group corresponds to the number of A, B, and -'s in the index between 5 - 7 which correspond to the JP number.
*   Step 2. We then convert those numbers into their proper precentages while excluding dashes (unanswered questions).
*   Step 3. Then the function will output these values.


#### "analyise" function
  The analyise function will analyise the different category numbers into their letter counterpart. It does this is 2 steps:

*   Step 1. The function sends each of the category numbers through their corresponding lambda where the lambda makes the decision if the number is greater than 50, less than 50, or equal to 50. Then it outputs the correct letter for the category based on this answer.
*   Step 2. The function outputs these letters.


#### "output" function
  The output function is what wraps up the entire process for each given test. It formats the results into a specific way then writes them onto the output.txt file. Steps:
  
*   Step 1. The output function will first format all the score numbers for each category into a list to add brackets around them (it's just easier). Example formating: "'[80, 23, 52, 78]'".
*   Step 2. The function will then format the score letters starting first with the IE score letter, then the SN score letter, then the TF score letter, lastly the JP score letter. Formated as such: " = ENFJ"
*   Step 3. Then the name is formated as such: "Lenard White: "
*   Step 4. The function will then remove the " ' " from the category score list before writing this information all into output.txt and adding a new line.



### GRN.py
The GRN.py script is used only if you want to generate random tests to use when executing the AnalyiseData.py file. The steps of the GRN.py are quite simple:

*   Step 1. The script will first look to see if you have put a number into the first command line, this number being the number of partipants you want to generate. If you do not enter anything into the command line the program will by default generate 20 different participants.
*   Step 2. The script will then open the USAnames.txt file and get a list of all the names.
*   Step 3. The personality.txt file will be opened before a loop with the length of the number of participants is used to run the remaining code.
*   Step 4. The "random import" generates 2 numbers between 1 - 2001 then sets the first name to the index of the first random number in the names list, same with the second number and the last name.
*   Step 5. The first and last name is then outputed into the personality.txt file.
*   Step 6. The program will then generate another random number which will decide if the person being generated is more of a introvert, an extrovert, or in the middle.
*   Step 7. A loop will run 70 times (70 questions) and each iteration will choose a random number corresponding to a more introverted, extroverted, or middle answer based on if the generated person is more introverted, extroverted, or in the middle.
  


## Using the PTARM
The PTRAM it is quite a simple process. The process goes as followed:
*   First either import all of your tests you want to process into the personality.txt file, or generate a set amount of random participants by using the GRN.py file with command arguments (command arguments for if you want 100 random participants: python GRN.py 100). 
*   Second run the AnalyiseData.py script to process the data.
*   Third Find the data in the output.txt file for you to use. 
   







