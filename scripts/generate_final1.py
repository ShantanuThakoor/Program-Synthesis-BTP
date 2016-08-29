import random
from string import ascii_uppercase

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
			f2.write("<tableRow text=\""+i+"\" font=\"Comic Sans\" size=\""+str(size)+"\" color=\"blue\"></tableRow>\n")
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

fonts = ['Comic Sans','Arial','Times New Roman','Arial Bold']
sizes = [1,2,3,4,5,6,8,10,12,14,16,18,20]
colors = ['red','blue','green','yellow','black']

f1 = open('../ranking/input4.xml','w')
f2 = open('../ranking/output4.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

for j in range(1000):
	
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
			f2.write("<tableRow text=\""+i+"\" font=\"Comic Sans\" size=\""+str(size)+"\" color=\"blue\"></tableRow>\n")
		f2.write("</textbox>\n")

		f1.write("<textbox>\n")
		for i in textlist:
			f1.write("<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n")
		f1.write("</textbox>\n")

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()

# ###########################################################################################

random.seed(1301)

fonts = ['Comic Sans','Arial','Times New Roman','Arial Bold']
sizes = [1,2,3,4,5,6,8,10,12,14,16,18,20]
colors = ['red','blue','green','yellow','black']

f1 = open('../test/input4.xml','w')
f2 = open('../test/output4.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

for j in range(50):
	
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
			f2.write("<tableRow text=\""+i+"\" font=\"Comic Sans\" size=\""+str(size)+"\" color=\"blue\"></tableRow>\n")
		f2.write("</textbox>\n")

		f1.write("<textbox>\n")
		for i in textlist:
			f1.write("<para text=\""+i+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" color=\""+str(color)+"\"></para>\n")
		f1.write("</textbox>\n")

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()