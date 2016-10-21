import random
from string import ascii_uppercase
import sys
from datetime import datetime

args = sys.argv
date_object = datetime.strptime(args[2],"%Y-%m-%d %H:%M:%S.%f")
x =  date_object
print x
random.seed(x)

impurity_rank = float(args[1])
impurity_test = float(args[1])
impurity_train = 0.9

train_examples = 100
rank_examples = 300
test_examples = 100

# random.seed(1301)

fonts = ['Arial','Times New Roman']
sizes = [6,8,10,12,14]

######################################################################

f1 = open('../training/input8.xml','w')
f2 = open('../training/output8.xml','w')

inputs = []
outputs = []
j = 0
a = 0

b = 0
c = 0
d = 0

f1.write("<input>\n")
f2.write("<output>\n")

limit1 = int(impurity_train*train_examples/3 + random.randrange(0,4))

while j < impurity_train*train_examples:
	
	font = fonts[random.randrange(0,2)]
	size = sizes[random.randrange(0,5)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(font == "Times New Roman" and size == 10):
		unique.append(0)
	if(font == "Arial"):
		unique.append(1)
	if(size == 8):
		unique.append(2)

	if len(unique) == 1:

		valid = True

		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" style=\"normal\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 2:
			b = b + 1
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"" + str(size) +"\" style=\"underline\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 1:
			if c < limit1:
				c = c + 1
				out = "<table>\n";
				for i in textlist:
					out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" style=\"italic\"></tableRow>\n"
				out = out + "</table>\n"
			else:
				valid  = False
		
		elif unique[0] == 0:
			d =  d + 1
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\"Times New Roman\" size=\""+str(size)+"\" style=\"bold\"></para>\n"
			out = out + "</textbox>\n"
		
		if valid:
			inputs.append(inp)
			outputs.append(out)
			j = j + 1


while j < train_examples:
	
	font = "Arial"
	size = 8
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(paras > 10):
		a = a+1
		unique.append(0)
	if(paras <= 10):
		unique.append(1)

	if len(unique) == 1:

		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" style=\"normal\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 1:
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" style=\"italic\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 0:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"" + str(size) +"\" style=\"underline\"></item>\n"
			out = out + "</list>\n"
		
		
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

# random.seed(101)

f1 = open('../ranking/input8.xml','w')
f2 = open('../ranking/output8.xml','w')

inputs = []
outputs = []
j = 0
a = 0

b = 0
c = 0
d = 0

f1.write("<input>\n")
f2.write("<output>\n")

limit1 = int(impurity_rank*rank_examples/3 + random.randrange(0,10))

while j < impurity_rank*rank_examples:
	
	font = fonts[random.randrange(0,2)]
	size = sizes[random.randrange(0,5)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(font == "Times New Roman" and size == 10):
		unique.append(0)
	if(font == "Arial"):
		unique.append(1)
	if(size == 8):
		unique.append(2)

	if len(unique) == 1:

		valid = True
		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" style=\"normal\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 2:
			b = b + 1
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"" + str(size) +"\" style=\"underline\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 1:
			if c < limit1:
				c = c + 1
				out = "<table>\n";
				for i in textlist:
					out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" style=\"italic\"></tableRow>\n"
				out = out + "</table>\n"
			else:
				valid = False

		elif unique[0] == 0:
			d =  d + 1
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\"Times New Roman\" size=\""+str(size)+"\" style=\"bold\"></para>\n"
			out = out + "</textbox>\n"
		
		if valid:
			inputs.append(inp)
			outputs.append(out)
			j = j + 1


while j < rank_examples:
	
	font = "Arial"
	size = 8
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(paras > 10):
		a = a+1
		unique.append(0)
	if(paras <= 10):
		unique.append(1)

	if len(unique) == 1:

		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" style=\"normal\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 1:
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" style=\"italic\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 0:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"" + str(size) +"\" style=\"underline\"></item>\n"
			out = out + "</list>\n"
		
		
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

# ###########################################################################################

# random.seed(11)

f1 = open('../test/input8.xml','w')
f2 = open('../test/output8.xml','w')

inputs = []
outputs = []
j = 0
a = 0

b = 0
c = 0
d = 0

f1.write("<input>\n")
f2.write("<output>\n")

limit1 = int(impurity_test*test_examples/3 + random.randrange(0,7))

while j < impurity_test*test_examples:
	
	font = fonts[random.randrange(0,2)]
	size = sizes[random.randrange(0,5)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(font == "Times New Roman" and size == 10):
		unique.append(0)
	if(font == "Arial"):
		unique.append(1)
	if(size == 8):
		unique.append(2)

	if len(unique) == 1:
		valid = True
		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" style=\"normal\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 2:
			b = b + 1
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"" + str(size) +"\" style=\"underline\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 1:
			if c < limit1:
				c = c + 1
				out = "<table>\n";
				for i in textlist:
					out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" style=\"italic\"></tableRow>\n"
				out = out + "</table>\n"
			else:
				valid = False

		elif unique[0] == 0:
			d =  d + 1
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\"Times New Roman\" size=\""+str(size)+"\" style=\"bold\"></para>\n"
			out = out + "</textbox>\n"
		
		if valid:
			inputs.append(inp)
			outputs.append(out)
			j = j + 1


while j < test_examples:
	
	font = "Arial"
	size = 8
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(paras > 10):
		a = a+1
		unique.append(0)
	if(paras <= 10):
		unique.append(1)

	if len(unique) == 1:

		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" style=\"normal\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 1:
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" style=\"italic\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 0:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"" + str(size) +"\" style=\"underline\"></item>\n"
			out = out + "</list>\n"
		
		
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