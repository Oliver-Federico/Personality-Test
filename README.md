# Personality Test Analyzer
Welcome to PTARM (Personality Test Analyzer Read Me) in this read me file you will learn how to use the PTARM and how it works. 

The PTARM is a data analyzer that analyzes the data from the [Keirsey Personality Test](https://www.keirsey.com/). It scores you on 4 categorys, Introvert or extrovert (IE), Sensing or Intution (SE), Thinking or Feeling (TF), Judging or Preceiving (JP).

## How to use the PTARM
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
The main function is like most functions named main, it controls the overall function of the entire script running through different functions and output to get an end result. Here is a simplifed version of the main functions steps:
* Step 1. The function opens the personality.txt file and gets all the answers given in the text file and puts them in a list.
* Step 2. The function creates a variable that counts how many outputs have been completed (starts at 0).
* Step 3. The function opens the output file and deletes all prior data. If you don't want this open the file and delete lines 17,18, and 19.
* Step 4. The function creates a while loop that only changes when the outputs is less than the length of the personality.txt document. Everything else in the main function is within this while loop.
* Step 5. The function runs another function called processData (see documentation below) to get the current test participants name, and a list of current response we are looking at (the 70 character A, B, -'s) and splits it into 10 groups of 7.
* Step 6. The function runs another function called calculations (see documentation below) which returns the number for the introvert or extrovert, sensing or intutition, thinking or feeling, and judging or preceiving.
* Step 7. The function runs another function called analyise (see documentation below) to return the letter that corresponds to the score given for each category.
* Step 8. The function converts the number score of each category into a string to be manipulated.
* Step 9. The function runs another function called output (see documentation below) which takes in all the data we just got from the other functions
* Step 10. The function adds 2 to that output variable we made because each test and name takes up 2 lines of the personality.txt file.
* Step 11. The while loop continues until the outputs is less than the length of the personality.txt file.



