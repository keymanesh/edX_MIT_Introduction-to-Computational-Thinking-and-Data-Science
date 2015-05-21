def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    import random
    samecolor = 0.0
    for i in range(numTrials):
        red = 0
        green = 0
        for j in range(3):
            ball = random.random() * (6 - j)
            if ball < (3.0 - red) :
                red += 1 
                
            else:
                green+=1
        if red == 3 or green ==3:
            samecolor+=1

    return samecolor/float(numTrials)

print noReplacementSimulation(10)