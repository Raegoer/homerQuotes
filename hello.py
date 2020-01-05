# Homer Simpson Quote Generator

import random

f = open('C:/Users/Georg/OneDrive/Documents/Coding/Python/Python1/quotes.txt', 'r')
fanswers = f.readlines()
f.close()

print ("Welcome to Homer Simpson Quote Generator! \n \n ~~~~~ \n")

print ("From a list of " + str(len(fanswers)) + " quotes, you got... \n")
choice = random.randint(0, len(fanswers) - 1)
print (fanswers[choice])
