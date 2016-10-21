import random
from string import ascii_uppercase
import sys
from datetime import datetime

args = sys.argv

date_object = datetime.strptime(args[3],"%Y-%m-%d %H:%M:%S.%f")
x =  date_object
print x
random.seed(x)

impurity_rank = float(args[1])
impurity_rank_unseen = float(args[2])

impurity_test = float(args[1])
impurity_test_unseen = float(args[2])
impurity_train = 0.9

train_examples = 100
rank_examples = 300
test_examples = 100

# random.seed(1301)

fonts = ['Arial','Times New Roman', 'Comic Sans MS', 'Gotham']
sizes = [8,10,12,14]
bulletType = ['square' , 'circle' ,'diamond', 'traingle']

######################################################################

f1 = open('../training/input91.xml','w')
f2 = open('../training/output91.xml','w')

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
	
	font = fonts[random.randrange(0,4)]
	size = sizes[random.randrange(0,4)]
	bullet = bulletType[random.randrange(0,4)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(font == "Arial" and bullet == "diamond"):
		unique.append(0)
	if(font == "Comic Sans MS"):
		unique.append(1)
	if(bullet == "square" and size == 12):
		unique.append(2)

	if len(unique) == 1:

		valid = True

		inp = "<list>\n";
		for i in textlist:
			inp = inp + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bulletType=\""+bullet+"\"></item>\n"
		inp = inp + "</list>\n"

		if unique[0] == 2:
			b = b + 1
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" bulletType=\"circle\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 0:
			c = c + 1
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" border=\"full\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 1:
			if(d < 35):
				d =  d + 1
				out = "<textbox>\n";
				for i in textlist:
					out = out + "<para text=\""+i+"\" font=\""+font+"\" size=\""+str(size)+"\" style=\"underline\"></para>\n"
				out = out + "</textbox>\n"
			else:
				valid = False
		
		if(valid):
			inputs.append(inp)
			outputs.append(out)
			j = j + 1		

while j < train_examples:
	
	font = "Comic Sans MS"
	size = 12
	bullet = "square"
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

		inp = "<list>\n";
		for i in textlist:
			inp = inp + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bulletType=\""+bullet+"\"></item>\n"
		inp = inp + "</list>\n"

		if unique[0] == 1:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" bulletType=\"circle\"></item>\n"
			out = out + "</list>\n"
		
		elif unique[0] == 0:
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\""+font+"\" size=\""+str(size)+"\" style=\"underline\"></para>\n"
			out = out + "</textbox>\n"
		
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
##################################################################################################

# random.seed(101)

f1 = open('../ranking/input91.xml','w')
f2 = open('../ranking/output91.xml','w')

inputs = []
outputs = []
j = 0
a = 0

b = 0
c = 0
d = 0

f1.write("<input>\n")
f2.write("<output>\n")
limit = int(impurity_rank*rank_examples/3 + random.randrange(0,7))

while j < impurity_rank*rank_examples:
	
	font = fonts[random.randrange(0,4)]
	size = sizes[random.randrange(0,4)]
	bullet = bulletType[random.randrange(0,4)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(font == "Arial" and bullet == "diamond"):
		unique.append(0)
	if(font == "Comic Sans MS"):
		unique.append(1)
	if(bullet == "square" and size == 12):
		unique.append(2)

	if len(unique) == 1:

		valid = True

		inp = "<list>\n";
		for i in textlist:
			inp = inp + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bulletType=\""+bullet+"\"></item>\n"
		inp = inp + "</list>\n"

		if unique[0] == 2:
			b = b + 1
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" bulletType=\"circle\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 0:
			c = c + 1
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" border=\"full\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 1:
			if(d < limit):
				d =  d + 1
				out = "<textbox>\n";
				for i in textlist:
					out = out + "<para text=\""+i+"\" font=\""+font+"\" size=\""+str(size)+"\" style=\"underline\"></para>\n"
				out = out + "</textbox>\n"
			else:
				valid = False
		
		if(valid):
			inputs.append(inp)
			outputs.append(out)
			j = j + 1		


while j < rank_examples*impurity_rank_unseen:
	
	font = "Arial"
	size = sizes[random.randrange(0,4)]
	bullet = bulletType[random.randrange(0,4)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	if bullet != 'diamond' and size != 12:

		inp = "<list>\n";
		for i in textlist:
			inp = inp + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bulletType=\""+bullet+"\"></item>\n"
		inp = inp + "</list>\n"

		out = "<table>\n";
		for i in textlist:
			out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" border=\"full\"></tableRow>\n"
		out = out + "</table>\n"
		
		inputs.append(inp)
		outputs.append(out)
		j = j + 1


while j < rank_examples:
	
	font = "Comic Sans MS"
	size = 12
	bullet = "square"
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

		inp = "<list>\n";
		for i in textlist:
			inp = inp + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bulletType=\""+bullet+"\"></item>\n"
		inp = inp + "</list>\n"

		if unique[0] == 1:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" bulletType=\"circle\"></item>\n"
			out = out + "</list>\n"
		
		elif unique[0] == 0:
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\""+font+"\" size=\""+str(size)+"\" style=\"underline\"></para>\n"
			out = out + "</textbox>\n"
		
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
##################################################################################################

# random.seed(11)

f1 = open('../test/input91.xml','w')
f2 = open('../test/output91.xml','w')

inputs = []
outputs = []
j = 0
a = 0

b = 0
c = 0
d = 0

f1.write("<input>\n")
f2.write("<output>\n")
limit = int(impurity_test*test_examples/3 + random.randrange(0,7))

while j < impurity_test*test_examples:
	
	font = fonts[random.randrange(0,4)]
	size = sizes[random.randrange(0,4)]
	bullet = bulletType[random.randrange(0,4)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	unique = []

	if(font == "Arial" and bullet == "diamond"):
		unique.append(0)
	if(font == "Comic Sans MS"):
		unique.append(1)
	if(bullet == "square" and size == 12):
		unique.append(2)

	if len(unique) == 1:

		valid = True

		inp = "<list>\n";
		for i in textlist:
			inp = inp + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bulletType=\""+bullet+"\"></item>\n"
		inp = inp + "</list>\n"

		if unique[0] == 2:
			b = b + 1
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" bulletType=\"circle\"></item>\n"
			out = out + "</list>\n"

		elif unique[0] == 0:
			c = c + 1
			out = "<table>\n";
			for i in textlist:
				out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" border=\"full\"></tableRow>\n"
			out = out + "</table>\n"
		
		elif unique[0] == 1:
			if(d < limit):
				d =  d + 1
				out = "<textbox>\n";
				for i in textlist:
					out = out + "<para text=\""+i+"\" font=\""+font+"\" size=\""+str(size)+"\" style=\"underline\"></para>\n"
				out = out + "</textbox>\n"
			else:
				valid = False
		
		if(valid):
			inputs.append(inp)
			outputs.append(out)
			j = j + 1		


while j < test_examples*impurity_test_unseen:
	
	font = "Arial"
	size = sizes[random.randrange(0,4)]
	bullet = bulletType[random.randrange(0,4)]
	textlist = []
	
	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	if bullet != 'diamond' and size != 12:

		inp = "<list>\n";
		for i in textlist:
			inp = inp + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bulletType=\""+bullet+"\"></item>\n"
		inp = inp + "</list>\n"

		out = "<table>\n";
		for i in textlist:
			out = out + "<tableRow text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" border=\"full\"></tableRow>\n"
		out = out + "</table>\n"
		
		inputs.append(inp)
		outputs.append(out)
		j = j + 1


while j < test_examples:
	
	font = "Comic Sans MS"
	size = 12
	bullet = "square"
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

		inp = "<list>\n";
		for i in textlist:
			inp = inp + "<item text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bulletType=\""+bullet+"\"></item>\n"
		inp = inp + "</list>\n"

		if unique[0] == 1:
			out = "<list>\n"
			for i in textlist:
				out = out + "<item text=\""+i+"\" font=\"Arial\" size=\""+str(size)+"\" bulletType=\"circle\"></item>\n"
			out = out + "</list>\n"
		
		elif unique[0] == 0:
			out = "<textbox>\n";
			for i in textlist:
				out = out + "<para text=\""+i+"\" font=\""+font+"\" size=\""+str(size)+"\" style=\"underline\"></para>\n"
			out = out + "</textbox>\n"
		
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
##################################################################################################