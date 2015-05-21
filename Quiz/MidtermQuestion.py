import numpy as np
import random
from matplotlib import pylab

def sampleQuizzes():
    grades = []
    prob = 0
    for i in range(10000):
        mid1 = int(50 + random.random() * 31)
        mid2 = int(60 + random.random() * 31)
        fin = int(55 + random.random() * 41)
        grade = (mid2+mid1)/4. + (fin/2.)
        
        if grade>=70 and grade<=75:
            prob +=1

        grades.append(grade)
    return grades

#print sum([1,2,3])
#print sampleQuizzes()

def plotQuizzes():
    # Your code here
    scores = sampleQuizzes()
    pylab.hist(scores,7)
    pylab.title("Distribution of Scores")
    pylab.xlabel("Final Score")
    pylab.ylabel("Number of Trials")
    pylab.show()

def probTest(limit):
    prob = 1
    step = 0
    while prob >= limit:
        step += 1
        prob = ((5/6.) ** (step-1)) * 1/6.

    return step

print probTest(.1)