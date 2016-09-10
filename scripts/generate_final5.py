import random
from string import ascii_uppercase
import sys

args = sys.argv

impurity_rank = float(args[1])
impurity_test = 0.8
impurity_train = 0.9

train_examples = 100
rank_examples = 300
test_examples = 100

random.seed(1301)

fonts = ['Arial','Times New Roman']
sizes = [6,8,10,12,14]

######################################################################

f1 = open('../training/input4.xml','w')
f2 = open('../training/output4.xml','w')

inputs = []
outputs = []
j = 0
a = 0

b = 0
c = 0
d = 0

f1.write("<input>\n")
f2.write("<output>\n")

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
			c = c + 1
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" style=\"italic\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 0:
			d =  d + 1
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\"Times New Roman\" size=\""+str(size)+"\" style=\"bold\"></para>\n"
			out = out + "</textbox>\n"
		
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

	if(size == 10 and color=="red" and font == "Arial" and paras > 10):
		a = a+1
		unique.append(0)
	if(size == 10 and color=="red" and font == "Arial" and paras <= 10):
		unique.append(1)

	if len(unique) == 1:

		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 0:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"12\" color=\"blue\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 1:
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" color=\"red\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 2:
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\"Comic Sans\" size=\""+str(size)+"\" color=\"blue\"></para>\n"
			out = out + "</textbox>\n"
		
		inputs.append(inp)
		outputs.append(out)

		j = j + 1


c = list(zip(inputs, outputs))
random.shuffle(c)
inputs, outputs = zip(*c)

for i in inputs:
	f1.write(i)
for i in outputs:
	f2.write(i)

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()

print a
##################################################################################################3

random.seed(101)

f1 = open('../ranking/input4.xml','w')
f2 = open('../ranking/output4.xml','w')

inputs = []
outputs = []
j = 0
a = 0

f1.write("<input>\n")
f2.write("<output>\n")

while j < impurity_rank*rank_examples:
	
	font = fonts[random.randrange(0,4)]
	size = sizes[random.randrange(0,13)]
	color = colors[random.randrange(0,5)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(size == 10 and color=="red"):
		unique.append(0)
	if(font == "Arial"):
		unique.append(1)
	if(font == "Times New Roman" and color=="blue"):
		unique.append(2)

	if len(unique) == 1:

		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 0:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"12\" color=\"blue\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 1:
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" color=\"red\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 2:
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\"Comic Sans\" size=\""+str(size)+"\" color=\"blue\"></para>\n"
			out = out + "</textbox>\n"
		
		inputs.append(inp)
		outputs.append(out)

		j = j + 1


while j < rank_examples:
	
	font = fonts[random.randrange(0,4)]
	size = sizes[random.randrange(0,13)]
	color = colors[random.randrange(0,5)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(size == 10 and color=="red" and font == "Arial" and paras > 10):
		a = a+1
		unique.append(0)
	if(size == 10 and color=="red" and font == "Arial" and paras <= 10):
		unique.append(1)

	if len(unique) == 1:

		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 0:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"12\" color=\"blue\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 1:
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" color=\"red\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 2:
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\"Comic Sans\" size=\""+str(size)+"\" color=\"blue\"></para>\n"
			out = out + "</textbox>\n"
		
		inputs.append(inp)
		outputs.append(out)

		j = j + 1


c = list(zip(inputs, outputs))
random.shuffle(c)
inputs, outputs = zip(*c)

for i in inputs:
	f1.write(i)
for i in outputs:
	f2.write(i)

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()

print a

# ###########################################################################################

random.seed(11)

f1 = open('../test/input4.xml','w')
f2 = open('../test/output4.xml','w')

inputs = []
outputs = []
j = 0

f1.write("<input>\n")
f2.write("<output>\n")

a = 0

while j < impurity_test*test_examples:
	
	font = fonts[random.randrange(0,4)]
	size = sizes[random.randrange(0,13)]
	color = colors[random.randrange(0,5)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(size == 10 and color=="red"):
		unique.append(0)
	if(font == "Arial"):
		unique.append(1)
	if(font == "Times New Roman" and color=="blue"):
		unique.append(2)

	if len(unique) == 1:

		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 0:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"12\" color=\"blue\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 1:
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" color=\"red\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 2:
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\"Comic Sans\" size=\""+str(size)+"\" color=\"blue\"></para>\n"
			out = out + "</textbox>\n"
		
		inputs.append(inp)
		outputs.append(out)

		j = j + 1


while j < test_examples:
	
	font = fonts[random.randrange(0,4)]
	size = sizes[random.randrange(0,13)]
	color = colors[random.randrange(0,5)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(size == 10 and color=="red" and font == "Arial" and paras > 10):
		unique.append(0)
		a = a + 1
	if(size == 10 and color=="red" and font == "Arial" and paras <= 10):
		unique.append(1)

	if len(unique) == 1:

		inp = "<textbox>\n";
		for i in textlist:
			inp = inp + "<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n"
		inp = inp + "</textbox>\n"

		if unique[0] == 0:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\"12\" color=\"blue\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 1:
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" color=\"red\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 2:
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\"Comic Sans\" size=\""+str(size)+"\" color=\"blue\"></para>\n"
			out = out + "</textbox>\n"
		
		inputs.append(inp)
		outputs.append(out)

		j = j + 1


c = list(zip(inputs, outputs))
random.shuffle(c)
inputs, outputs = zip(*c)

for i in inputs:
	f1.write(i)
for i in outputs:
	f2.write(i)

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()

print a