import random

def makePair(): #Removes one person from the potential pool (number in options) and assigs them a match (position in goals)
    temp = random.choice(options)
    options.remove(temp)
    goals.append(temp)

def checkResult(): #Counts how many numbers are in their corresponding positions (how many matches are correct)
    beams = 0
    for c in range(1,12):
        if (c == goals[c-1]):
            beams += 1
    return beams

# ======== Main start ============

random.seed()
couples = 11
iterations = 1000000

# Initializes blank list for storing results of many matchup ceremonies
results = []
for i in range(0,couples+1):
    results.append(0)

#Goes through each iteration of the matching ceremony
for itr in range(0,iterations):
    #Resets the couples
    goals = []
    options = list(range(1,couples+1))
    #Matches couples
    for n in range(1,couples+1):
        makePair()
    #Saves a count of how many were correct
    results[checkResult()] += 1

#Prints summary of all iterations and how many matches in all ceremonies
print ("=== RESULTS ===")
for r in range(0,couples+1):
    print (str(r)+": "+str(results[r]))
