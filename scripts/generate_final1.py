import random
from string import ascii_uppercase
import sys

args = sys.argv
impurity = float(args[1])
impurity_test = float(args[2])
rank_examples = int(args[3])

random.seed(1301)

fonts = ['Comic Sans','Arial','Times New Roman','Arial Bold']
sizes = [1,2,3,4,5,6,8,10,12,14,16,18,20]
colors = ['red','blue','green','yellow','black']

f1 = open('../training/input4.xml','w')
f2 = open('../training/output4.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

for j in range(100):
	
	font = fonts[random.randrange(0,4)]
	size = sizes[random.randrange(0,13)]
	color = colors[random.randrange(0,5)]
	textlist = []

	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	if(size == 10 and color=="red"):
		f2.write("<list>\n");
		for i in textlist:
			f2.write("<item text=\""+i+"\" font=\""+str(font)+"\" size=\"12\" color=\"blue\"></item>\n")
		f2.write("</list>\n")

		f1.write("<textbox>\n")
		for i in textlist:
			f1.write("<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n")
		f1.write("</textbox>\n")

	elif(font == "Arial"):
		f2.write("<table>\n");
		for i in textlist:
			f2.write("<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" color=\"red\"></tableRow>\n")
		f2.write("</table>\n")

		f1.write("<textbox>\n")
		for i in textlist:
			f1.write("<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n")
		f1.write("</textbox>\n")

	elif(font == "Times New Roman" and color=="blue"):
		f2.write("<textbox>\n");
		for i in textlist:
			f2.write("<para text=\""+i+"\" font=\"Comic Sans\" size=\""+str(size)+"\" color=\"blue\"></para>\n")
		f2.write("</textbox>\n")

		f1.write("<textbox>\n")
		for i in textlist:
			f1.write("<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n")
		f1.write("</textbox>\n")

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()

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

while j < impurity*rank_examples:
	
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

while j < impurity_test*50:
	
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


while j < 50:
	
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