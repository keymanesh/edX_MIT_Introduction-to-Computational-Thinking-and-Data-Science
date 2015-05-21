def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

import numpy as np 

A = np.array([0,1,2,3,4,5,6,7,8])

B= np.array([5,10,10,10,15])

C= np.array([0,1,2,4,6,8])

D=  np.array([6,7,11,12,13,15])

E= np.array([9,0,0,3,3,3,6,6])



L = [A, B, C, D, E]

L = np.array(L)

for lis in L:
	avg = possible_mean(lis)
	print possible_variance(lis)

