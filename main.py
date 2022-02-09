#!/usr/bin/python3
import sys

class Question:
    def __init__(self):
        self.q = ""
        self.a = ""

    def parseLine(self, line):
        if(line[0:2] == 'a~'):
            self.a = line[2:-1]
            return True
        else:
            self.q += line
            return False

def main(f):
    questions = [Question()]
    ptr = 0
    for line in f:
        if(questions[ptr].parseLine(line)):
            questions.append(Question())
            ptr += 1
    questions.pop()
    score = 0
    l = len(questions)
    for question in questions:
        print(question.q)
        answer = input("")
        if(answer == question.a):
            print("Correct")
            score += 1
        else:
            print(f'Incorrect. Correct answer: {question.a}')
    print(f'Total score: {score} out of {l}')

def openFile(fname):
    try:
        f = open(fname)
        main(f)
    finally:
        f.close()

if(__name__ == "__main__"):
    if(len(sys.argv) == 1):
        sys.exit("Fatal error: No file specified")
    else:
        openFile(sys.argv[1])
        
