import random
from string import ascii_uppercase

fonts = ['Comic Sans','Arial']

f1 = open('input_train.xml','w')
f2 = open('output_train.xml','w')

# f2 = open('input_rank.xml','w')
# f21 = open('output_rank.xml','w')

# f3 = open('input_test.xml','w')
# f31 = open('output_test.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

for j in range(15):
	
	f1.write("<textbox>\n")

	font_option = random.randrange(0,3)
	if(font_option != 2):
			font = fonts[font_option];
	else:
		font = ''.join(random.choice(ascii_uppercase) for i in range(5))

	if(font_option == 0):
		f2.write("<table>\n")
	elif(font_option == 1):
		f2.write("<list>\n")
	else:
		f2.write("<textbox>\n")

	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		size = random.randrange(10,20)
		bold = random.randrange(0,5)
		
		if(font_option == 0):
			f2.write("<tableRow>\n")
			f2.write("<tableCell text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></tableCell>\n")
			f2.write("</tableRow>\n")
	
		elif(font_option == 1):
			f2.write("<item text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></item>\n")

		else:
			f2.write("<para text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></para>\n")
		
		f1.write("<para text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></para>\n")

	if(font_option == 0):
		f2.write("</table>\n")
	elif(font_option == 1):
		f2.write("</list>\n")
	else:
		f2.write("</textbox>\n")
	f1.write("</textbox>\n")

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()

##################################################################################################3

f1 = open('input_rank.xml','w')
f2 = open('output_rank.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

for j in range(100):
	
	f1.write("<textbox>\n")

	font_option = random.randrange(0,3)
	if(font_option != 2):
			font = fonts[font_option];
	else:
		font = ''.join(random.choice(ascii_uppercase) for i in range(5))

	correct = random.randrange(0,10)

	if(font_option == 0):
		f2.write("<table>\n")
	
	elif(font_option == 1):
		f2.write("<list>\n")
	
	else:
		f2.write("<textbox>\n")

	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		size = random.randrange(10,20)
		bold = random.randrange(0,5)
		
		if(font_option == 0):
			f2.write("<tableRow>\n")
			f2.write("<tableCell text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></tableCell>\n")
			f2.write("</tableRow>\n")
	
		elif(font_option == 1):
			f2.write("<item text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></item>\n")

		else:
			f2.write("<para text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></para>\n")
		
		f1.write("<para text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></para>\n")

	if(font_option == 0):
		f2.write("</table>\n")
	elif(font_option == 1):
		f2.write("</list>\n")
	else:
		f2.write("</textbox>\n")
	f1.write("</textbox>\n")

f1.write("</input>")
f1.close()
f2.write("</output")
f2.close()