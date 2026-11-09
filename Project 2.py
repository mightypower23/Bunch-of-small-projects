import random
import sys
answerlist=["yes","Hell yes", "yeah","No","Hell no","Not in ten lifetimes"]

def eightball():
    print("Welcome to Marlon's magic eight ball")
    print("What is your question")
    question=input()
    getanswers=random.randint(0,5)
    answers= answerlist[getanswers]
    print(answers)

eightball()
anotherone=''
while True:
    anotherone=str(input("Do you want another fortune: "))
    if anotherone == "Yes" or anotherone == "yes":
        eightball()
    elif anotherone == "No" or anotherone == "no":
        print("Okay, Goodbye.")
        break
    else:
        print("Sorry didn't catch that what did you say.")
        continue
      