import random
from string import ascii_uppercase

random.seed(10)

fonts = ['Comic Sans','Arial']

f1 = open('../training/input3.xml','w')
f2 = open('../training/output3.xml','w')

# f2 = open('input_rank.xml','w')
# f21 = open('output_rank.xml','w')

# f3 = open('input_test.xml','w')
# f31 = open('output_test.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

for j in range(5):
	
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
		size = 10
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

random.seed(0)

fonts = ['Comic Sans','Arial']

f1 = open('../ranking/input3.xml','w')
f2 = open('../ranking/output3.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

inc = 0

for j in range(5):
	
	f1.write("<textbox>\n")

	font_option = random.randrange(0,3)
	if(font_option != 2):
			font = fonts[font_option];
	else:
		font = ''.join(random.choice(ascii_uppercase) for i in range(5))

	correct = random.randrange(0,10)
	rnd = random.randrange(0,2)
	if(correct <= 7):
		inc = inc + 1

	if(font_option == 0):
		if(correct <= 7):
			option = 1
		else:
			option = 3
	
	elif(font_option == 1):
		if(correct <= 7):
			option = 2
		else:
			option = 3
	
	else:
		option = 3

	if(option == 1):
		f2.write("<table>\n")
	elif(option == 2):
		f2.write("<list>\n")
	else:
		f2.write("<textbox>\n")

	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		size = 10
		bold = random.randrange(0,5)
		
		if(option == 1):
			f2.write("<tableRow>\n")
			f2.write("<tableCell text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></tableCell>\n")
			f2.write("</tableRow>\n")
	
		elif(option == 2):
			f2.write("<item text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></item>\n")

		else:
			f2.write("<para text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></para>\n")
		
		f1.write("<para text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></para>\n")

	if(option == 1):
		f2.write("</table>\n")
	elif(option == 2):
		f2.write("</list>\n")
	else:
		f2.write("</textbox>\n")
	f1.write("</textbox>\n")

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()

print inc

###########################################################################################

random.seed(1010)

fonts = ['Comic Sans','Arial']

f1 = open('../test/input3.xml','w')
f2 = open('../test/output3.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

inc = 0

for j in range(5):
	
	f1.write("<textbox>\n")

	font_option = random.randrange(0,3)
	if(font_option != 2):
			font = fonts[font_option];
	else:
		font = ''.join(random.choice(ascii_uppercase) for i in range(5))

	correct = random.randrange(0,10)
	rnd = random.randrange(0,2)
	if(correct < 6):
		inc = inc + 1

	if(font_option == 0):
		if(correct < 6):
			option = 1
		else:
			option = 3
	
	elif(font_option == 1):
		if(correct < 6):
			option = 2
		else:
			option = 3

	
	else:
		option = 3

	if(option == 1):
		f2.write("<table>\n")
	elif(option == 2):
		f2.write("<list>\n")
	else:
		f2.write("<textbox>\n")

	paras = random.randrange(1,20);
	
	for i in range(paras):
		text = ''.join(random.choice(ascii_uppercase) for i in range(10))
		size = 13
		bold = random.randrange(0,5)
		
		if(option == 1):
			f2.write("<tableRow>\n")
			f2.write("<tableCell text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></tableCell>\n")
			f2.write("</tableRow>\n")
	
		elif(option == 2):
			f2.write("<item text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></item>\n")

		else:
			f2.write("<para text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></para>\n")
		
		f1.write("<para text=\""+text+"\" font=\""+str(font)+"\" size=\""+str(size)+"\" bold=\""+str(bold)+"\"></para>\n")

	if(option == 1):
		f2.write("</table>\n")
	elif(option == 2):
		f2.write("</list>\n")
	else:
		f2.write("</textbox>\n")
	f1.write("</textbox>\n")

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()

print inc