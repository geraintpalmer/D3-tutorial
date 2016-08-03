import json
import random


variableA = [random.expovariate(4) for _ in range(500)]
variableB = [random.normalvariate(3, 2) for _ in range(500)]
variableC = [random.uniform(0, 8) for _ in range(500)]

mydata = [{'variableA':variableA[i], 'variableB':variableB[i], 'variableC':variableC[i]} for i in range(500)]


with open('sampledata.json', 'w') as outfile:
    json.dump(mydata, outfile)