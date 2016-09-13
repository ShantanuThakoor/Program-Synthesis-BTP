import random
from string import ascii_uppercase
import sys
from datetime import datetime

print datetime.now()
random.seed(datetime.now())

args = sys.argv

impurity_rank = float(args[1])
impurity_test = 0.8
impurity_train = 0.9

train_examples = 100
rank_examples = 300
test_examples = 100

# random.seed(1301)

sizes = [1,2,3,4,5,6,8,10,12]
colors = ['red','blue','green','yellow','black']
aligns = ['left','right','center']
#############################################################################

f1 = open('../training/input5.xml','w')
f2 = open('../training/output5.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")
a = 0
b = 0
c = 0
d = 0

inputs = []
outputs = []
j = 0

while j < impurity_train*train_examples:
	
	size = sizes[random.randrange(0,9)]
	color = colors[random.randrange(0,5)]
	align = aligns[random.randrange(0,3)]
	textlist = []

	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	satisfied = []

	if(size == 8 and align != "center"):
		a = a + 1
		satisfied.append(0)
	elif(align == "center" and size != 8):
		b = b + 1
		satisfied.append(1)
	elif(size == 6 and align == "right"):
		c = c + 1
		satisfied.append(2)

	if(len(satisfied) == 1):

		if(satisfied[0] == 2):
			out = "<slide image_align=\"left\">\n"
			out = out + "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" size=\"10\" color=\"black\"></item>\n"
			out = out + "</list>\n"
			out = out + "</slide>\n"

		elif(satisfied[0] == 0):
			out = "<slide image_align=\""+align+"\">\n"
			out = out + "<textbox>\n"
			for i in textlist:
				out = out + "<para text=\""+i+"\" size=\"10\" color=\"red\"></para>\n"
			out = out + "</textbox>\n"
			out = out + "</slide>\n"

		elif(satisfied[0] == 1):
			out = "<slide image_align=\"center\">\n"
			out = out + "<table>\n"
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" size=\"12\" color=\"blue\"></tableRow>\n"
			out = out + "</table>\n"
			out = out + "</slide>\n"

		inp = "<slide image_align=\""+align+"\">\n"
		inp = inp + "<textbox>\n"
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
		inp = inp + "</textbox>\n"
		inp =inp + "</slide>\n"

		inputs.append(inp)
		outputs.append(out)
		j = j + 1


while j < train_examples:
	
	size = 8
	color = colors[random.randrange(0,5)]
	align = "center"
	textlist = []

	paras = random.randrange(1,20);
	if paras <= 10:
		case = 1
	else:
		case = 2

	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	if(case == 1):
		d = d + 1
		out = "<slide image_align=\""+align+"\">\n"
		out = out + "<textbox>\n"
		for i in textlist:
			out = out + "<para text=\""+i+"\" size=\"10\" color=\"red\"></para>\n"
		out = out + "</textbox>\n"
		out = out + "</slide>\n"
		
	else:
		out = "<slide image_align=\"center\">\n"
		out = out + "<table>\n"
		for i in textlist:
			out = out + "<tableRow text=\""+i+"\" size=\"12\" color=\"blue\"></tableRow>\n"
		out = out + "</table>\n"
		out = out + "</slide>\n"
		
	inp = "<slide image_align=\""+align+"\">\n"
	inp = inp + "<textbox>\n"
	for i in textlist:
		inp = inp + "<para text=\""+i+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
	inp = inp + "</textbox>\n"
	inp =inp + "</slide>\n"

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
			
f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c,d
##################################################################################################3

# random.seed(101)

f1 = open('../ranking/input5.xml','w')
f2 = open('../ranking/output5.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")
a = 0
b = 0
c = 0
d = 0

inputs = []
outputs = []
j = 0

while j < impurity_rank*rank_examples:
	
	size = sizes[random.randrange(0,9)]
	color = colors[random.randrange(0,5)]
	align = aligns[random.randrange(0,3)]
	textlist = []

	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	satisfied = []

	if(size == 8 and align != "center"):
		a = a + 1
		satisfied.append(0)
	elif(align == "center" and size != 8):
		b = b + 1
		satisfied.append(1)
	elif(size == 6 and align == "right"):
		c = c + 1
		satisfied.append(2)

	if(len(satisfied) == 1):

		if(satisfied[0] == 2):
			out = "<slide image_align=\"left\">\n"
			out = out + "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" size=\"10\" color=\"black\"></item>\n"
			out = out + "</list>\n"
			out = out + "</slide>\n"

		elif(satisfied[0] == 0):
			out = "<slide image_align=\""+align+"\">\n"
			out = out + "<textbox>\n"
			for i in textlist:
				out = out + "<para text=\""+i+"\" size=\"10\" color=\"red\"></para>\n"
			out = out + "</textbox>\n"
			out = out + "</slide>\n"

		elif(satisfied[0] == 1):
			out = "<slide image_align=\"center\">\n"
			out = out + "<table>\n"
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" size=\"12\" color=\"blue\"></tableRow>\n"
			out = out + "</table>\n"
			out = out + "</slide>\n"

		inp = "<slide image_align=\""+align+"\">\n"
		inp = inp + "<textbox>\n"
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
		inp = inp + "</textbox>\n"
		inp =inp + "</slide>\n"

		inputs.append(inp)
		outputs.append(out)
		j = j + 1


while j < rank_examples:

	size = 8
	color = colors[random.randrange(0,5)]
	align = "center"
	textlist = []

	paras = random.randrange(1,20);
	if paras <= 10:
		case = 1
	else:
		case = 2

	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	if(case == 1):
		d = d + 1
		out = "<slide image_align=\""+align+"\">\n"
		out = out + "<textbox>\n"
		for i in textlist:
			out = out + "<para text=\""+i+"\" size=\"10\" color=\"red\"></para>\n"
		out = out + "</textbox>\n"
		out = out + "</slide>\n"
		
	else:
		out = "<slide image_align=\"center\">\n"
		out = out + "<table>\n"
		for i in textlist:
			out = out + "<tableRow text=\""+i+"\" size=\"12\" color=\"blue\"></tableRow>\n"
		out = out + "</table>\n"
		out = out + "</slide>\n"
		
	inp = "<slide image_align=\""+align+"\">\n"
	inp = inp + "<textbox>\n"
	for i in textlist:
		inp = inp + "<para text=\""+i+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
	inp = inp + "</textbox>\n"
	inp =inp + "</slide>\n"

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
			
f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c,d

# # ###########################################################################################

# random.seed(11)

f1 = open('../test/input5.xml','w')
f2 = open('../test/output5.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")
a = 0
b = 0
c = 0
d = 0

inputs = []
outputs = []
j = 0

while j < impurity_test*test_examples:
	
	size = sizes[random.randrange(0,9)]
	color = colors[random.randrange(0,5)]
	align = aligns[random.randrange(0,3)]
	textlist = []

	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	satisfied = []

	if(size == 8 and align != "center"):
		a = a + 1
		satisfied.append(0)
	elif(align == "center" and size != 8):
		b = b + 1
		satisfied.append(1)
	elif(size == 6 and align == "right"):
		c = c + 1
		satisfied.append(2)

	if(len(satisfied) == 1):

		if(satisfied[0] == 2):
			out = "<slide image_align=\"left\">\n"
			out = out + "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" size=\"10\" color=\"black\"></item>\n"
			out = out + "</list>\n"
			out = out + "</slide>\n"

		elif(satisfied[0] == 0):
			out = "<slide image_align=\""+align+"\">\n"
			out = out + "<textbox>\n"
			for i in textlist:
				out = out + "<para text=\""+i+"\" size=\"10\" color=\"red\"></para>\n"
			out = out + "</textbox>\n"
			out = out + "</slide>\n"

		elif(satisfied[0] == 1):
			out = "<slide image_align=\"center\">\n"
			out = out + "<table>\n"
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" size=\"12\" color=\"blue\"></tableRow>\n"
			out = out + "</table>\n"
			out = out + "</slide>\n"

		inp = "<slide image_align=\""+align+"\">\n"
		inp = inp + "<textbox>\n"
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
		inp = inp + "</textbox>\n"
		inp =inp + "</slide>\n"

		inputs.append(inp)
		outputs.append(out)
		j = j + 1


while j < test_examples:
	
	size = 8
	color = colors[random.randrange(0,5)]
	align = "center"
	textlist = []

	paras = random.randrange(1,20);
	if paras <= 10:
		case = 1
	else:
		case = 2

	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	if(case == 1):
		d = d + 1
		out = "<slide image_align=\""+align+"\">\n"
		out = out + "<textbox>\n"
		for i in textlist:
			out = out + "<para text=\""+i+"\" size=\"10\" color=\"red\"></para>\n"
		out = out + "</textbox>\n"
		out = out + "</slide>\n"
		
	else:
		out = "<slide image_align=\"center\">\n"
		out = out + "<table>\n"
		for i in textlist:
			out = out + "<tableRow text=\""+i+"\" size=\"12\" color=\"blue\"></tableRow>\n"
		out = out + "</table>\n"
		out = out + "</slide>\n"
		
	inp = "<slide image_align=\""+align+"\">\n"
	inp = inp + "<textbox>\n"
	for i in textlist:
		inp = inp + "<para text=\""+i+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
	inp = inp + "</textbox>\n"
	inp =inp + "</slide>\n"

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
			
f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c,d