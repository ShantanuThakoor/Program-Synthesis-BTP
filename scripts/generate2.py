import random
from string import ascii_uppercase

fonts = ['Comic Sans','Arial','Times New Roman']

random.seed(432)

f1 = open('../training/input2.xml','w')
f2 = open('../training/output2.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")

a = 0
b = 0
c = 0

for j in range(30):
	
	f1.write("<slide>\n")
	
	imsize = random.randrange(10,20)
	align = random.randrange(0,3)
	f1.write("<image align=\""+['right','center','left'][align]+"\" size=\""+str(imsize)+"\"></image>\n")
		
	f1.write("<textbox>\n")
	textlist = []
	sizelist = []
	
	for i in range(5):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		size = random.randrange(10,40)
		font = random.randrange(0,3)
		align = random.randrange(0,3)
		
		f1.write("<para text=\""+text+"\" font=\""+fonts[font]+"\" size=\""+str(size)+"\" align=\""+['right','center','left'][align]+"\"></para>\n")

		textlist.append("text=\""+text+"\" font=\""+fonts[font]+"\" size=\"10\" align=\"left\"")
		sizelist.append(size)

	f1.write("</textbox>\n")
	f1.write("</slide>\n")

	minsize = min(sizelist)
	if(minsize < 13):
		a = a + 1
		f2.write("<slide left=\"true\">\n")
		f2.write("<image align=\"left\" size=\"8\"></image>\n")
	elif(minsize < 20):
		b = b + 1
		f2.write("<slide center=\"true\">\n")
		f2.write("<image align=\"center\" size=\"8\"></image>\n")
	else:
		c = c + 1
		f2.write("<slide right=\"true\">\n")
		f2.write("<image align=\"right\" size=\"8\"></image>\n")

	f2.write("<textbox>\n")
	for i in textlist:
		f2.write("<para "+i+"></para>\n")
	f2.write("</textbox>\n")

	f2.write("</slide>\n")

f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c
##################################################################################################3

fonts = ['Comic Sans','Arial','Times New Roman']

random.seed(10)

f1 = open('../ranking/input2.xml','w')
f2 = open('../ranking/output2.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")

a = 0
b = 0
c = 0

for j in range(300):
	
	f1.write("<slide>\n")
	
	imsize = random.randrange(10,20)
	align = random.randrange(0,3)
	f1.write("<image align=\""+['right','center','left'][align]+"\" size=\""+str(imsize)+"\"></image>\n")
		
	f1.write("<textbox>\n")
	textlist = []
	sizelist = []
	
	for i in range(5):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		size = random.randrange(10,40)
		font = random.randrange(0,3)
		align = random.randrange(0,3)
		
		f1.write("<para text=\""+text+"\" font=\""+fonts[font]+"\" size=\""+str(size)+"\" align=\""+['right','center','left'][align]+"\"></para>\n")

		textlist.append("text=\""+text+"\" font=\""+fonts[font]+"\" size=\"10\" align=\"left\"")
		sizelist.append(size)

	f1.write("</textbox>\n")
	f1.write("</slide>\n")

	minsize = min(sizelist)
	if(minsize < 13):
		a = a + 1
		f2.write("<slide left=\"true\">\n")
		f2.write("<image align=\"left\" size=\"8\"></image>\n")
	elif(minsize < 20):
		b = b + 1
		f2.write("<slide center=\"true\">\n")
		f2.write("<image align=\"center\" size=\"8\"></image>\n")
	else:
		c = c + 1
		f2.write("<slide right=\"true\">\n")
		f2.write("<image align=\"right\" size=\"8\"></image>\n")

	f2.write("<textbox>\n")
	for i in textlist:
		f2.write("<para "+i+"></para>\n")
	f2.write("</textbox>\n")

	f2.write("</slide>\n")

f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c

# ###########################################################################################

fonts = ['Comic Sans','Arial','Times New Roman']

random.seed(1010)

f1 = open('../test/input2.xml','w')
f2 = open('../test/output2.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")

a = 0
b = 0
c = 0

for j in range(20):
	
	f1.write("<slide>\n")
	
	imsize = random.randrange(10,20)
	align = random.randrange(0,3)
	f1.write("<image align=\""+['right','center','left'][align]+"\" size=\""+str(imsize)+"\"></image>\n")
		
	f1.write("<textbox>\n")
	textlist = []
	sizelist = []
	
	for i in range(5):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		size = random.randrange(10,40)
		font = random.randrange(0,3)
		align = random.randrange(0,3)
		
		f1.write("<para text=\""+text+"\" font=\""+fonts[font]+"\" size=\""+str(size)+"\" align=\""+['right','center','left'][align]+"\"></para>\n")

		textlist.append("text=\""+text+"\" font=\""+fonts[font]+"\" size=\"10\" align=\"left\"")
		sizelist.append(size)

	f1.write("</textbox>\n")
	f1.write("</slide>\n")

	minsize = min(sizelist)
	if(minsize < 13):
		a = a + 1
		f2.write("<slide left=\"true\">\n")
		f2.write("<image align=\"left\" size=\"8\"></image>\n")
	elif(minsize < 20):
		b = b + 1
		f2.write("<slide center=\"true\">\n")
		f2.write("<image align=\"center\" size=\"8\"></image>\n")
	else:
		c = c + 1
		f2.write("<slide right=\"true\">\n")
		f2.write("<image align=\"right\" size=\"8\"></image>\n")

	f2.write("<textbox>\n")
	for i in textlist:
		f2.write("<para "+i+"></para>\n")
	f2.write("</textbox>\n")

	f2.write("</slide>\n")

f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c