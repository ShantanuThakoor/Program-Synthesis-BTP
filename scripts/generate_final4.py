import random
from string import ascii_uppercase
import sys

args = sys.argv
freq1 = int(args[1])
freq2 = int(args[2])
freq3 = int(args[3])
freq4 = int(args[4])
rank_examples = int(args[5])

random.seed(1301)

colors = ['red','blue','green','black']
colors2 = ['orange','yellow','pink']

f1 = open('../training/input7.xml','w')
f2 = open('../training/output7.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")

for j in range(100):
	
	color1 = random.randrange(0,3)
	color2 = random.randrange(0,3)
	color3 = random.randrange(0,3)
	case = random.randrange(0,40)
	# print case

	if(case < 10):
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[1+color1]+"\"></point>\n")
		f1.write("<point color=\""+colors[color2+1]+"\"></point>\n")
		f1.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet a=\"1\">\n")
		f2.write("<point color=\""+colors[1+color1]+"\"></point>\n")
		f2.write("<point color=\""+colors[color2+1]+"\"></point>\n")
		f2.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f2.write("</bullet>\n")

	elif(case < 20):
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[color2+1]+"\"></point>\n")
		f1.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet b=\"1\">\n")
		f2.write("<point color=\""+colors2[0]+"\"></point>\n")
		f2.write("<point color=\""+colors2[0]+"\"></point>\n")
		f2.write("<point color=\""+colors2[0]+"\"></point>\n")
		f2.write("</bullet>\n")

	elif(case < 30):
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet c=\"1\">\n")
		f2.write("<point color=\""+colors2[1]+"\"></point>\n")
		f2.write("<point color=\""+colors2[1]+"\"></point>\n")
		f2.write("<point color=\""+colors2[1]+"\"></point>\n")
		f2.write("</bullet>\n")

	else:
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet d=\"1\">\n")
		f2.write("<point color=\""+colors2[2]+"\"></point>\n")
		f2.write("<point color=\""+colors2[2]+"\"></point>\n")
		f2.write("<point color=\""+colors2[2]+"\"></point>\n")
		f2.write("</bullet>\n")

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()

##################################################################################################3

random.seed(101)

f1 = open('../ranking/input7.xml','w')
f2 = open('../ranking/output7.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")
j = 0

while j<rank_examples :
	
	color1 = random.randrange(0,3)
	color2 = random.randrange(0,3)
	color3 = random.randrange(0,3)
	case = random.randrange(0,freq1+freq2+freq3+freq4)
	# print case

	if(case < freq1):
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[1+color1]+"\"></point>\n")
		f1.write("<point color=\""+colors[color2+1]+"\"></point>\n")
		f1.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet a=\"1\">\n")
		f2.write("<point color=\""+colors[1+color1]+"\"></point>\n")
		f2.write("<point color=\""+colors[color2+1]+"\"></point>\n")
		f2.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f2.write("</bullet>\n")

	elif(case < freq1+freq2):
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[color2+1]+"\"></point>\n")
		f1.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet b=\"1\">\n")
		f2.write("<point color=\""+colors2[0]+"\"></point>\n")
		f2.write("<point color=\""+colors2[0]+"\"></point>\n")
		f2.write("<point color=\""+colors2[0]+"\"></point>\n")
		f2.write("</bullet>\n")

	elif(case < freq1+freq2+freq3):
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet c=\"1\">\n")
		f2.write("<point color=\""+colors2[1]+"\"></point>\n")
		f2.write("<point color=\""+colors2[1]+"\"></point>\n")
		f2.write("<point color=\""+colors2[1]+"\"></point>\n")
		f2.write("</bullet>\n")

	else:
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet d=\"1\">\n")
		f2.write("<point color=\""+colors2[2]+"\"></point>\n")
		f2.write("<point color=\""+colors2[2]+"\"></point>\n")
		f2.write("<point color=\""+colors2[2]+"\"></point>\n")
		f2.write("</bullet>\n")

	j = j + 1

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()

# # ###########################################################################################

random.seed(11)

f1 = open('../test/input7.xml','w')
f2 = open('../test/output7.xml','w')

f1.write("<input>\n")
f2.write("<output>\n")
j = 0

while j<50:
	
	color1 = random.randrange(0,3)
	color2 = random.randrange(0,3)
	color3 = random.randrange(0,3)
	case = random.randrange(0,freq1+freq2+freq3+freq4)
	# print case

	if(case < freq1):
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[1+color1]+"\"></point>\n")
		f1.write("<point color=\""+colors[color2+1]+"\"></point>\n")
		f1.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet a=\"1\">\n")
		f2.write("<point color=\""+colors[1+color1]+"\"></point>\n")
		f2.write("<point color=\""+colors[color2+1]+"\"></point>\n")
		f2.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f2.write("</bullet>\n")

	elif(case < freq1+freq2):
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[color2+1]+"\"></point>\n")
		f1.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet b=\"1\">\n")
		f2.write("<point color=\""+colors2[0]+"\"></point>\n")
		f2.write("<point color=\""+colors2[0]+"\"></point>\n")
		f2.write("<point color=\""+colors2[0]+"\"></point>\n")
		f2.write("</bullet>\n")

	elif(case < freq1+freq2+freq3):
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[1+color3]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet c=\"1\">\n")
		f2.write("<point color=\""+colors2[1]+"\"></point>\n")
		f2.write("<point color=\""+colors2[1]+"\"></point>\n")
		f2.write("<point color=\""+colors2[1]+"\"></point>\n")
		f2.write("</bullet>\n")

	else:
		f1.write("<bullet>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("<point color=\""+colors[0]+"\"></point>\n")
		f1.write("</bullet>\n")

		f2.write("<bullet d=\"1\">\n")
		f2.write("<point color=\""+colors2[2]+"\"></point>\n")
		f2.write("<point color=\""+colors2[2]+"\"></point>\n")
		f2.write("<point color=\""+colors2[2]+"\"></point>\n")
		f2.write("</bullet>\n")

	j = j + 1

f1.write("</input>")
f1.close()
f2.write("</output>")
f2.close()