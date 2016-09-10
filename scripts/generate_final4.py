import random
from string import ascii_uppercase
import sys

import sys

args = sys.argv
impurity_rank = float(args[1])
impurity_test = 0.2
impurity_train = 0.1

train_examples = 100
rank_examples = 300
test_examples = 100

random.seed(1301)

colors = ['red','blue','green','black']
colors2 = ['orange','yellow','pink']

##########################################################################################33

f1 = open('../training/input7.xml','w')
f2 = open('../training/output7.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

inputs = []
outputs = []
j = 0

a=0
b=0
c=0
d=0

while j < impurity_train*train_examples:
	
	color1 = random.randrange(0,3)
	color2 = random.randrange(0,3)
	color3 = random.randrange(0,3)
	case = random.randrange(0,3)

	if(case == 0):
		a = a + 1
		inp = "<bullet>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[color2+1]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[1+color3]+"\"></point>\n"
		inp = inp + "</bullet>\n"

		out = "<bullet a=\"1\">\n"
		out = out + "<point color=\""+colors2[0]+"\"></point>\n"
		out = out + "<point color=\""+colors2[0]+"\"></point>\n"
		out = out + "<point color=\""+colors2[0]+"\"></point>\n"
		out = out + "</bullet>\n"

	elif(case == 1):
		b = b + 1
		inp = "<bullet>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[1+color3]+"\"></point>\n"
		inp = inp + "</bullet>\n"

		out = "<bullet b=\"1\">\n"
		out = out + "<point color=\""+colors2[1]+"\"></point>\n"
		out = out + "<point color=\""+colors2[1]+"\"></point>\n"
		out = out + "<point color=\""+colors2[1]+"\"></point>\n"
		out = out + "</bullet>\n"

	else:
		c = c + 1
		inp = "<bullet>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "</bullet>\n"

		out = "<bullet c=\"1\">\n"
		out = out + "<point color=\""+colors2[2]+"\"></point>\n"
		out = out + "<point color=\""+colors2[2]+"\"></point>\n"
		out = out + "<point color=\""+colors2[2]+"\"></point>\n"
		out = out + "</bullet>\n"

	inputs.append(inp)
	outputs.append(out)

	j = j + 1

while j < train_examples:
	
	color1 = random.randrange(0,3)
	color2 = random.randrange(0,3)
	color3 = random.randrange(0,3)

	d = d + 1
	inp = "<bullet>\n"
	inp = inp + "<point color=\""+colors[color1+1]+"\"></point>\n"
	inp = inp + "<point color=\""+colors[color2+1]+"\"></point>\n"
	inp = inp + "<point color=\""+colors[1+color3]+"\"></point>\n"
	inp = inp + "</bullet>\n"

	out = "<bullet d=\"1\">\n"
	out = out + "<point color=\""+colors[color1+1]+"\"></point>\n"
	out = out + "<point color=\""+colors[color2+1]+"\"></point>\n"
	out = out + "<point color=\""+colors[color3+1]+"\"></point>\n"
	out = out + "</bullet>\n"

	inputs.append(inp)
	outputs.append(out)

	j = j + 1

z = list(zip(inputs, outputs))
random.shuffle(z)
inputs, outputs = zip(*z)

for i in inputs:
	f1.write(i)
for i in outputs:
	f2.write(i)


f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()
print a,b,c,d

##################################################################################################3

random.seed(101)

f1 = open('../ranking/input7.xml','w')
f2 = open('../ranking/output7.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

inputs = []
outputs = []
j = 0

a=0
b=0
c=0
d=0

while j < impurity_rank*rank_examples:
	
	color1 = random.randrange(0,3)
	color2 = random.randrange(0,3)
	color3 = random.randrange(0,3)
	case = random.randrange(0,3)

	if(case == 0):
		a = a + 1
		inp = "<bullet>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[color2+1]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[1+color3]+"\"></point>\n"
		inp = inp + "</bullet>\n"

		out = "<bullet a=\"1\">\n"
		out = out + "<point color=\""+colors2[0]+"\"></point>\n"
		out = out + "<point color=\""+colors2[0]+"\"></point>\n"
		out = out + "<point color=\""+colors2[0]+"\"></point>\n"
		out = out + "</bullet>\n"

	elif(case == 1):
		b = b + 1
		inp = "<bullet>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[1+color3]+"\"></point>\n"
		inp = inp + "</bullet>\n"

		out = "<bullet b=\"1\">\n"
		out = out + "<point color=\""+colors2[1]+"\"></point>\n"
		out = out + "<point color=\""+colors2[1]+"\"></point>\n"
		out = out + "<point color=\""+colors2[1]+"\"></point>\n"
		out = out + "</bullet>\n"

	else:
		c = c + 1
		inp = "<bullet>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "</bullet>\n"

		out = "<bullet c=\"1\">\n"
		out = out + "<point color=\""+colors2[2]+"\"></point>\n"
		out = out + "<point color=\""+colors2[2]+"\"></point>\n"
		out = out + "<point color=\""+colors2[2]+"\"></point>\n"
		out = out + "</bullet>\n"

	inputs.append(inp)
	outputs.append(out)

	j = j + 1

while j < rank_examples:
	
	color1 = random.randrange(0,3)
	color2 = random.randrange(0,3)
	color3 = random.randrange(0,3)

	d = d + 1
	inp = "<bullet>\n"
	inp = inp + "<point color=\""+colors[color1+1]+"\"></point>\n"
	inp = inp + "<point color=\""+colors[color2+1]+"\"></point>\n"
	inp = inp + "<point color=\""+colors[1+color3]+"\"></point>\n"
	inp = inp + "</bullet>\n"

	out = "<bullet d=\"1\">\n"
	out = out + "<point color=\""+colors[color1+1]+"\"></point>\n"
	out = out + "<point color=\""+colors[color2+1]+"\"></point>\n"
	out = out + "<point color=\""+colors[color3+1]+"\"></point>\n"
	out = out + "</bullet>\n"

	inputs.append(inp)
	outputs.append(out)

	j = j + 1

z = list(zip(inputs, outputs))
random.shuffle(z)
inputs, outputs = zip(*z)

for i in inputs:
	f1.write(i)
for i in outputs:
	f2.write(i)


f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()
print a,b,c,d

# # ###########################################################################################

random.seed(11)

f1 = open('../test/input7.xml','w')
f2 = open('../test/output7.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

inputs = []
outputs = []
j = 0

a=0
b=0
c=0
d=0

while j < impurity_test*test_examples:
	
	color1 = random.randrange(0,3)
	color2 = random.randrange(0,3)
	color3 = random.randrange(0,3)
	case = random.randrange(0,3)

	if(case == 0):
		a = a + 1
		inp = "<bullet>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[color2+1]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[1+color3]+"\"></point>\n"
		inp = inp + "</bullet>\n"

		out = "<bullet a=\"1\">\n"
		out = out + "<point color=\""+colors2[0]+"\"></point>\n"
		out = out + "<point color=\""+colors2[0]+"\"></point>\n"
		out = out + "<point color=\""+colors2[0]+"\"></point>\n"
		out = out + "</bullet>\n"

	elif(case == 1):
		b = b + 1
		inp = "<bullet>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[1+color3]+"\"></point>\n"
		inp = inp + "</bullet>\n"

		out = "<bullet b=\"1\">\n"
		out = out + "<point color=\""+colors2[1]+"\"></point>\n"
		out = out + "<point color=\""+colors2[1]+"\"></point>\n"
		out = out + "<point color=\""+colors2[1]+"\"></point>\n"
		out = out + "</bullet>\n"

	else:
		c = c + 1
		inp = "<bullet>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "<point color=\""+colors[0]+"\"></point>\n"
		inp = inp + "</bullet>\n"

		out = "<bullet c=\"1\">\n"
		out = out + "<point color=\""+colors2[2]+"\"></point>\n"
		out = out + "<point color=\""+colors2[2]+"\"></point>\n"
		out = out + "<point color=\""+colors2[2]+"\"></point>\n"
		out = out + "</bullet>\n"

	inputs.append(inp)
	outputs.append(out)

	j = j + 1

while j < test_examples:
	
	color1 = random.randrange(0,3)
	color2 = random.randrange(0,3)
	color3 = random.randrange(0,3)

	d = d + 1
	inp = "<bullet>\n"
	inp = inp + "<point color=\""+colors[color1+1]+"\"></point>\n"
	inp = inp + "<point color=\""+colors[color2+1]+"\"></point>\n"
	inp = inp + "<point color=\""+colors[1+color3]+"\"></point>\n"
	inp = inp + "</bullet>\n"

	out = "<bullet d=\"1\">\n"
	out = out + "<point color=\""+colors[color1+1]+"\"></point>\n"
	out = out + "<point color=\""+colors[color2+1]+"\"></point>\n"
	out = out + "<point color=\""+colors[color3+1]+"\"></point>\n"
	out = out + "</bullet>\n"

	inputs.append(inp)
	outputs.append(out)

	j = j + 1

z = list(zip(inputs, outputs))
random.shuffle(z)
inputs, outputs = zip(*z)

for i in inputs:
	f1.write(i)
for i in outputs:
	f2.write(i)


f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()
print a,b,c,d