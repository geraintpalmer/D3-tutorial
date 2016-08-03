import json
import random


data = []
s = random.random()*300
for i in range(50):
	s += random.normalvariate(2, 3)
	data.append(s)
for i in range(35):
	s += random.normalvariate(-1, 2)
	data.append(s)
for i in range(40):
	s += random.normalvariate(-5, 7)
	data.append(s)

data2 = []
s = random.random()*300
for i in range(50):
	s += random.normalvariate(-2, 5)
	data2.append(s)
for i in range(35):
	s += random.normalvariate(6, 1.5)
	data2.append(s)
for i in range(40):
	s += random.normalvariate(0, 3)
	data2.append(s)



mydata = [{'idx':index, 'point1': data[index], 'point2':data2[index]} for index in range(len(data))]


with open('sampledata2.json', 'w') as outfile:
    json.dump(mydata, outfile)