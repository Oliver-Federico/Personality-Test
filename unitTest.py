import AnalyiseData
import time
from pyfiglet import Figlet
figlet = Figlet()
correctAnswersList = [
    "Betty Boop: [90, 15, 10, 10] = ISTJ\n",
    "Snoopy: [30, 45, 30, 70] = ESTP\n",
    "Bugs Bunny: [20, 45, 15, 55] = ESTP\n",
    "Daffy Duck: [100, 6, 20, 6] = ISTJ\n",
    "The frumious bandersnatch: [86, 95, 75, 78] = INFP\n",
    "Minnie Mouse: [67, 28, 32, 5] = ISTJ\n",
    "Luke Skywalker: [89, 61, 26, 25] = INTJ\n",
    "Han Solo: [80, 50, 45, 25] = IXTJ\n",
    "Princess Leia: [80, 50, 50, 5] = IXXJ\n"
]

def scriptRun():
    setup()
    print(" ")
    print(" ")
    checkCorrectOutput()
    print(" ")
    print(" ")

def setup():
    p = open("personality.txt", "wt")
    p.writelines(
    "Betty Boop\n"
    "BABAAAABAAAAAAABAAAABBAAAAAABAAAABABAABAAABABABAABAAAAAABAAAAAABAAAAAA\n"
    "Snoopy\n"
    "AABBAABBBBBABABAAAAABABBAABBAAAABBBAAABAABAABABAAAABAABBBBAAABBAABABBB\n"
    "Bugs Bunny\n"
    "aabaabbabbbaaaabaaaabaaaaababbbaabaaaabaabbbbabaaaabaabaaaaaabbaaaaabb\n"
    "Daffy Duck\n"
    "BAAAAA-BAAAABABAAAAAABA-AAAABABAAAABAABAA-BAAABAABAAAAAABA-BAAABA-BAAA\n"
    "The frumious bandersnatch\n"
    "-BBaBAA-BBbBBABBBBA-BaBBBBBbbBBABBBBBBABB-BBBaBBABBBBBBB-BABBBBBBBBBBB\n"
    "Minnie Mouse\n"
    "BABA-AABABBBAABAABA-ABABAAAB-ABAAAAAA-AAAABAAABAAABAAAAAB-ABBAAAAAAAAA\n"
    "Luke Skywalker\n"
    "bbbaaabbbbaaba-BAAAABBABBAAABBAABAAB-AAAAABBBABAABABA-ABBBABBABAA-AAAA\n"
    "Han Solo\n"
    "BA-ABABBB-bbbaababaaaabbaaabbaaabbabABBAAABABBAAABABAAAABBABAAABBABAAB\n"
    "Princess Leia\n"
    "BABBAAABBBBAAABBA-AAAABABBABBABBAAABAABAAABBBA-AABAABAAAABAAAAABABBBAA\n"
    )
    p.close()
def checkCorrectOutput():
    try:
        AnalyiseData.main()
        print("Main Exists")
    except:
        print("Error <main> Does not exist in <AnalyiseData> script")
    try:
        c = open("output.txt", "rt")
        l = c.readlines()
        if correctAnswersList == l:
            print("Line 1 Correct\n")
            time.sleep(0.4)
            print("Line 2 Correct\n")
            time.sleep(0.4)
            print("Line 3 Correct\n")
            time.sleep(0.4)
            print("Line 4 Correct\n")
            time.sleep(0.4)
            print("Line 5 Correct\n")
            time.sleep(0.4)
            print("Line 6 Correct\n")
            time.sleep(0.4)
            print("Line 7 Correct\n")
            time.sleep(0.4)
            print("Line 8 Correct\n")
            time.sleep(0.4)
            print("Line 9 Correct\n")
            time.sleep(0.4)
            print("")
            print("Good Job bud!")

        else:
            print("Error of type correct value in text file <output.txt>")
        c.close()
    except:
        print("Error <output.txt> Does not exist in the current directory")

scriptRun()
