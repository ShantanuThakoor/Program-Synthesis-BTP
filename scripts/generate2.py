import random
from string import ascii_uppercase

fonts = ['Comic Sans','Arial','Times New Roman']

random.seed(4342)

f1 = open('../training/input2.xml','w')
f2 = open('../training/output2.xml','w')

# f2 = open('input_rank.xml','w')
# f21 = open('output_rank.xml','w')

# f3 = open('input_test.xml','w')
# f31 = open('output_test.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")

for j in range(15):
	
	f1.write("<slide>\n")
	f2.write("<slide>\n")

	image_option = random.randrange(0,2)
	if(image_option == 1):
		imsize = random.randrange(10,20)
		align = random.randrange(0,3)
		f1.write("<image align=\""+['right','center','left'][align]+"\" size=\""+str(imsize)+"\"></image>\n")
		f2.write("<image align=\"left\" size=\"8\"></image>\n")
		
	paras = random.randrange(1,20);
	f1.write("<textbox>\n")
	f2.write("<textbox>\n")

	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		size = random.randrange(10,20)
		font = random.randrange(0,3)
		align = random.randrange(0,3)
		
		f1.write("<para text=\""+text+"\" font=\""+fonts[font]+"\" size=\""+str(size)+"\" align=\""+['right','center','left'][align]+"\"></para>\n")

		if(image_option == 1):
			f2.write("<para text=\""+text+"\" font=\""+fonts[font]+"\" size=\""+str(10)+"\" align=\"right\"></para>\n")
		else:
			f2.write("<para text=\""+text+"\" font=\""+fonts[font]+"\" size=\""+str(size)+"\" align=\"center\"></para>\n")

	f1.write("</textbox>\n")
	f1.write("</slide>\n")
	f2.write("</textbox>\n")
	f2.write("</slide>\n")

f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

##################################################################################################3

# random.seed(10)

# fonts = ['Comic Sans','Arial']

# f1 = open('../ranking/input1.xml','w')
# f2 = open('../ranking/output1.xml','w')

# f1.write("<input>\n")
# f2.write("<output>\n")

# inc = 0

# for j in range(100):
	
# 	f1.write("<textbox>\n")

# 	font_option = random.randrange(0,3)
# 	if(font_option != 2):
# 			font = fonts[font_option];
# 	else:
# 		font = ''.join(random.choice(ascii_uppercase) for i in range(5))

# 	paras = random.randrange(1,20);
# 	textlist = []
# 	sizelist = []

# 	for i in range(paras):
# 		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
# 		size = random.randrange(10,20)
# 		bold = random.randrange(0,5)
		
# 		f1.write("<para text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></para>\n")
# 		textlist.append("text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"")
# 		sizelist.append(size)

# 	f1.write("</textbox>\n")
# 	if(min(sizelist) >= 12):
# 		if(font_option != 2):
# 			inc = inc + 1
		
# 		f2.write("<textbox>\n")
# 		for i in textlist:
# 			f2.write("<para "+i+"></para>\n")
# 		f2.write("</textbox>\n")

# 	else:
# 		if(font_option == 0):
# 			f2.write("<table>\n")
# 			for i in textlist:
# 				f2.write("<tableRow>\n")
# 				f2.write("<tableCell "+i+"></tableCell>\n")
# 				f2.write("</tableRow>\n")
# 			f2.write("</table>\n")

# 		elif(font_option == 1):
# 			f2.write("<list>\n")
# 			for i in textlist:
# 				f2.write("<item "+i+"></item>\n")
# 			f2.write("</list>\n")

# 		else:
# 			f2.write("<textbox>\n")
# 			for i in textlist:
# 				f2.write("<para "+i+"></para>\n")
# 			f2.write("</textbox>\n")


# f1.write("</input>")
# f1.close()
# f2.write("</output>")
# f2.close()

# print inc

# ###########################################################################################

# random.seed(1010)

# fonts = ['Comic Sans','Arial']

# f1 = open('../test/input1.xml','w')
# f2 = open('../test/output1.xml','w')

# f1.write("<input>\n")
# f2.write("<output>\n")

# inc = 0

# for j in range(100):
	
# 	f1.write("<textbox>\n")

# 	font_option = random.randrange(0,3)
# 	if(font_option != 2):
# 			font = fonts[font_option];
# 	else:
# 		font = ''.join(random.choice(ascii_uppercase) for i in range(5))

# 	paras = random.randrange(1,20);
# 	textlist = []
# 	sizelist = []

# 	for i in range(paras):
# 		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
# 		size = random.randrange(10,20)
# 		bold = random.randrange(0,5)
		
# 		f1.write("<para text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></para>\n")
# 		textlist.append("text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"")
# 		sizelist.append(size)

# 	f1.write("</textbox>\n")
# 	if(min(sizelist) >= 12):
# 		if(font_option != 2):
# 			inc = inc + 1
		
# 		f2.write("<textbox>\n")
# 		for i in textlist:
# 			f2.write("<para "+i+"></para>\n")
# 		f2.write("</textbox>\n")

# 	else:
# 		if(font_option == 0):
# 			f2.write("<table>\n")
# 			for i in textlist:
# 				f2.write("<tableRow>\n")
# 				f2.write("<tableCell "+i+"></tableCell>\n")
# 				f2.write("</tableRow>\n")
# 			f2.write("</table>\n")

# 		elif(font_option == 1):
# 			f2.write("<list>\n")
# 			for i in textlist:
# 				f2.write("<item "+i+"></item>\n")
# 			f2.write("</list>\n")

# 		else:
# 			f2.write("<textbox>\n")
# 			for i in textlist:
# 				f2.write("<para "+i+"></para>\n")
# 			f2.write("</textbox>\n")


# f1.write("</input>")
# f1.close()
# f2.write("</output>")
# f2.close()

# print inc