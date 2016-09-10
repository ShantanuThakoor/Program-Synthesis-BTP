import random
from string import ascii_uppercase
import sys

args = sys.argv
impurity_rank = float(args[1])
impurity_test = 0.2
impurity_train = 0.1

train_examples = 200
rank_examples = 300
test_examples = 100

random.seed(1301)

aligns = ['left','right','center']
nums = [1,2,3,4,5,6,7]

################################################################################

f1 = open('../training/input6.xml','w')
f2 = open('../training/output6.xml','w')

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
	
	alignlist = []

	numimages = nums[random.randrange(0,3)]
	
	for i in range(numimages):
		align = aligns[random.randrange(0,3)]
		alignlist.append(align)

	if(numimages == 1):
		out = "<slide type=\"1\">\n"
		a = a + 1
		out = out + "<image align=\"center\"></image>\n"
	
	elif(numimages == 2):
		out = "<slide type=\"2\">\n"
		b = b + 1
		out = out + "<image align=\"left\"></image>\n"
		out = out + "<image align=\"right\"></image>\n"

	elif(numimages == 3):
		out = "<slide type=\"3\">\n"
		c = c + 1
		out = out + "<image align=\"left\"></image>\n"
		out = out + "<image align=\"center\"></image>\n"
		out = out + "<image align=\"right\"></image>\n"

	out = out + "</slide>\n"

	inp = "<slide>\n"
	for i in alignlist:
		inp = inp + "<image align=\""+i+"\"></image>\n"
	inp = inp + "</slide>\n"

	inputs.append(inp)
	outputs.append(out)

	j = j + 1

while j < train_examples:
	
	alignlist = []

	numimages = nums[random.randrange(0,4)]+3
	
	for i in range(numimages):
		align = aligns[random.randrange(0,3)]
		alignlist.append(align)

	out = "<slide type=\"4\">\n"	
	d = d + 1
	for i in alignlist:
		out = out + "<image align=\""+i+"\"></image>\n"
	out = out + "</slide>\n"

	inp = "<slide>\n"
	for i in alignlist:
		inp = inp + "<image align=\""+i+"\"></image>\n"
	inp = inp + "</slide>\n"

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

random.seed(101)

f1 = open('../ranking/input6.xml','w')
f2 = open('../ranking/output6.xml','w')

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
	
	alignlist = []

	numimages = nums[random.randrange(0,3)]
	
	for i in range(numimages):
		align = aligns[random.randrange(0,3)]
		alignlist.append(align)

	if(numimages == 1):
		out = "<slide type=\"1\">\n"
		a = a + 1
		out = out + "<image align=\"center\"></image>\n"
	
	elif(numimages == 2):
		out = "<slide type=\"2\">\n"
		b = b + 1
		out = out + "<image align=\"left\"></image>\n"
		out = out + "<image align=\"right\"></image>\n"

	elif(numimages == 3):
		out = "<slide type=\"3\">\n"
		c = c + 1
		out = out + "<image align=\"left\"></image>\n"
		out = out + "<image align=\"center\"></image>\n"
		out = out + "<image align=\"right\"></image>\n"

	out = out + "</slide>\n"

	inp = "<slide>\n"
	for i in alignlist:
		inp = inp + "<image align=\""+i+"\"></image>\n"
	inp = inp + "</slide>\n"

	inputs.append(inp)
	outputs.append(out)

	j = j + 1

while j < rank_examples:
	
	alignlist = []

	numimages = nums[random.randrange(0,4)]+3
	
	for i in range(numimages):
		align = aligns[random.randrange(0,3)]
		alignlist.append(align)

	out = "<slide type=\"4\">\n"	
	d = d + 1
	for i in alignlist:
		out = out + "<image align=\""+i+"\"></image>\n"
	out = out + "</slide>\n"

	inp = "<slide>\n"
	for i in alignlist:
		inp = inp + "<image align=\""+i+"\"></image>\n"
	inp = inp + "</slide>\n"

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

# # # ###########################################################################################

random.seed(11)

f1 = open('../test/input6.xml','w')
f2 = open('../test/output6.xml','w')

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
	
	alignlist = []

	numimages = nums[random.randrange(0,3)]
	
	for i in range(numimages):
		align = aligns[random.randrange(0,3)]
		alignlist.append(align)

	if(numimages == 1):
		out = "<slide type=\"1\">\n"	
		a = a + 1
		out = out + "<image align=\"center\"></image>\n"
	
	elif(numimages == 2):
		out = "<slide type=\"2\">\n"
		b = b + 1
		out = out + "<image align=\"left\"></image>\n"
		out = out + "<image align=\"right\"></image>\n"

	elif(numimages == 3):
		out = "<slide type=\"3\">\n"
		c = c + 1
		out = out + "<image align=\"left\"></image>\n"
		out = out + "<image align=\"center\"></image>\n"
		out = out + "<image align=\"right\"></image>\n"

	out = out + "</slide>\n"

	inp = "<slide>\n"
	for i in alignlist:
		inp = inp + "<image align=\""+i+"\"></image>\n"
	inp = inp + "</slide>\n"

	inputs.append(inp)
	outputs.append(out)

	j = j + 1

while j < test_examples:
	
	alignlist = []

	numimages = nums[random.randrange(0,4)]+3
	
	for i in range(numimages):
		align = aligns[random.randrange(0,3)]
		alignlist.append(align)

	out = "<slide type=\"4\">\n"	
	d = d + 1
	for i in alignlist:
		out = out + "<image align=\""+i+"\"></image>\n"
	out = out + "</slide>\n"

	inp = "<slide>\n"
	for i in alignlist:
		inp = inp + "<image align=\""+i+"\"></image>\n"
	inp = inp + "</slide>\n"

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