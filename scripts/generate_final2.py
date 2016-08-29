import random
from string import ascii_uppercase

random.seed(1301)

sizes = [1,2,3,4,5,6,8,10,12]
colors = ['red','blue','green','yellow','black']
aligns = ['left','right','center']

f1 = open('../training/input5.xml','w')
f2 = open('../training/output5.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")
a = 0
b = 0
c = 0

for j in range(100):
	
	size = sizes[random.randrange(0,9)]
	color = colors[random.randrange(0,5)]
	align = aligns[random.randrange(0,3)]
	textlist = []

	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	satisfied = []

	if(size == 6):
		satisfied.append(0)
	if(color == "red"):
		satisfied.append(1)
	if(align == "center"):
		satisfied.append(2)
		
	# print len(satisfied)
	if(len(satisfied) == 1):
		a = a+1
	elif(len(satisfied) == 2):
		b = b+1
	elif(len(satisfied) == 3):
		c = c+1

	if(len(satisfied) > 0):

		option = satisfied[0]

		if(option == 0):
			f2.write("<slide image_align=\"left\">\n")
			f2.write("<list>\n");
			for i in textlist:
				f2.write("<item text=\""+i+"\" size=\"10\" color=\"black\"></item>\n")
			f2.write("</list>\n")
			f2.write("</slide>\n")
			
		elif(option == 1):
			f2.write("<slide image_align=\""+align+"\">\n")
			f2.write("<textbox>\n");
			for i in textlist:
				f2.write("<para text=\""+i+"\" size=\"10\" color=\"red\"></para>\n")
			f2.write("</textbox>\n")
			f2.write("</slide>\n")
			
		elif(option == 2):
			f2.write("<slide image_align=\"center\">\n")
			f2.write("<table>\n");
			for i in textlist:
				f2.write("<tableRow text=\""+i+"\" size=\"12\" color=\"blue\"></tableRow>\n")
			f2.write("</table>\n")
			f2.write("</slide>\n")
			
		f1.write("<slide image_align=\""+align+"\">\n")
		f1.write("<textbox>\n")
		for i in textlist:
			f1.write("<para text=\""+i+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n")
		f1.write("</textbox>\n")
		f1.write("</slide>\n")
			
f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c
##################################################################################################3

random.seed(101)

sizes = [1,2,3,4,5,6,8,10,12]
colors = ['red','blue','green','yellow','black']
aligns = ['left','right','center']

f1 = open('../ranking/input5.xml','w')
f2 = open('../ranking/output5.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")
a = 0
b = 0
c = 0

for j in range(1000):
	
	size = sizes[random.randrange(0,9)]
	color = colors[random.randrange(0,5)]
	align = aligns[random.randrange(0,3)]
	textlist = []

	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	satisfied = []

	if(size == 6):
		satisfied.append(0)
	if(color == "red"):
		satisfied.append(1)
	if(align == "center"):
		satisfied.append(2)
		
	# print len(satisfied)
	if(len(satisfied) == 1):
		a = a+1
	elif(len(satisfied) == 2):
		b = b+1
	elif(len(satisfied) == 3):
		c = c+1

	if(len(satisfied) > 0):

		option = satisfied[0]

		if(option == 0):
			f2.write("<slide image_align=\"left\">\n")
			f2.write("<list>\n");
			for i in textlist:
				f2.write("<item text=\""+i+"\" size=\"10\" color=\"black\"></item>\n")
			f2.write("</list>\n")
			f2.write("</slide>\n")
			
		elif(option == 1):
			f2.write("<slide image_align=\""+align+"\">\n")
			f2.write("<textbox>\n");
			for i in textlist:
				f2.write("<para text=\""+i+"\" size=\"10\" color=\"red\"></para>\n")
			f2.write("</textbox>\n")
			f2.write("</slide>\n")
			
		elif(option == 2):
			f2.write("<slide image_align=\"center\">\n")
			f2.write("<table>\n");
			for i in textlist:
				f2.write("<tableRow text=\""+i+"\" size=\"12\" color=\"blue\"></tableRow>\n")
			f2.write("</table>\n")
			f2.write("</slide>\n")
			
		f1.write("<slide image_align=\""+align+"\">\n")
		f1.write("<textbox>\n")
		for i in textlist:
			f1.write("<para text=\""+i+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n")
		f1.write("</textbox>\n")
		f1.write("</slide>\n")
			
f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c

# # ###########################################################################################

random.seed(11)

sizes = [1,2,3,4,5,6,8,10,12]
colors = ['red','blue','green','yellow','black']
aligns = ['left','right','center']

f1 = open('../test/input5.xml','w')
f2 = open('../test/output5.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")
a = 0
b = 0
c = 0

for j in range(50):
	
	size = sizes[random.randrange(0,9)]
	color = colors[random.randrange(0,5)]
	align = aligns[random.randrange(0,3)]
	textlist = []

	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		textlist.append(text)

	satisfied = []

	if(size == 6):
		satisfied.append(0)
	if(color == "red"):
		satisfied.append(1)
	if(align == "center"):
		satisfied.append(2)
		
	# print len(satisfied)
	if(len(satisfied) == 1):
		a = a+1
	elif(len(satisfied) == 2):
		b = b+1
	elif(len(satisfied) == 3):
		c = c+1

	if(len(satisfied) > 0):

		option = satisfied[0]

		if(option == 0):
			f2.write("<slide image_align=\"left\">\n")
			f2.write("<list>\n");
			for i in textlist:
				f2.write("<item text=\""+i+"\" size=\"10\" color=\"black\"></item>\n")
			f2.write("</list>\n")
			f2.write("</slide>\n")
			
		elif(option == 1):
			f2.write("<slide image_align=\""+align+"\">\n")
			f2.write("<textbox>\n");
			for i in textlist:
				f2.write("<para text=\""+i+"\" size=\"10\" color=\"red\"></para>\n")
			f2.write("</textbox>\n")
			f2.write("</slide>\n")
			
		elif(option == 2):
			f2.write("<slide image_align=\"center\">\n")
			f2.write("<table>\n");
			for i in textlist:
				f2.write("<tableRow text=\""+i+"\" size=\"12\" color=\"blue\"></tableRow>\n")
			f2.write("</table>\n")
			f2.write("</slide>\n")
			
		f1.write("<slide image_align=\""+align+"\">\n")
		f1.write("<textbox>\n")
		for i in textlist:
			f1.write("<para text=\""+i+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n")
		f1.write("</textbox>\n")
		f1.write("</slide>\n")
			
f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c