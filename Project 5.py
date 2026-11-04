
import argparse
import random
parser=argparse.ArgumentParser(description="Allows you to use  an eightball to answer any question ")

parser.add_argument('-q','--question',help="Gives you a magic 8 ball answer.",metavar="question",required=True)



args=parser.parse_args()


def eightball(question):
    answerlist=["yes","Hell yes", "yeah","No","Hell no","Not in ten lifetimes"]
    print("Welcome to Marlon's magic eight ball")
    print("What is your question")
    nah=question
    getanswers=random.randint(0,5)
    answers= answerlist[getanswers]
    print(answers)

eightball(args.question)
