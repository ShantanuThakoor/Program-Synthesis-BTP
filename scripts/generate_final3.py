import random
from string import ascii_uppercase

random.seed(1301)

aligns = ['left','right','center']
nums = [1,2,3,4,5,6,7]

f1 = open('../training/input6.xml','w')
f2 = open('../training/output6.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")
a = 0
b = 0
c = 0
d = 0

for j in range(30):
	
	alignlist = []

	numimages = nums[random.randrange(0,7)]
	
	for i in range(numimages):
		align = aligns[random.randrange(0,3)]
		alignlist.append(align)

	f2.write("<slide>\n")	
	if(numimages == 1):
		a = a + 1
		f2.write("<image align=\"center\"></image>\n")
	
	elif(numimages == 2):
		b = b + 1
		f2.write("<image align=\"left\"></image>\n")
		f2.write("<image align=\"right\"></image>\n")

	elif(numimages == 3):
		c = c + 1
		f2.write("<image align=\"left\"></image>\n")
		f2.write("<image align=\"center\"></image>\n")
		f2.write("<image align=\"right\"></image>\n")

	else:
		d = d + 1
		for i in alignlist:
			f2.write("<image align=\""+i+"\"></image>\n")
	f2.write("</slide>\n")

	f1.write("<slide>\n")
	for i in alignlist:
		f1.write("<image align=\""+i+"\"></image>\n")
	f1.write("</slide>\n")

			
f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c,d
##################################################################################################3

random.seed(101)

aligns = ['left','right','center']
nums = [1,2,3,4,5,6,7]

f1 = open('../ranking/input6.xml','w')
f2 = open('../ranking/output6.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")
a = 0
b = 0
c = 0
d = 0

for j in range(500):
	
	alignlist = []

	numimages = nums[random.randrange(0,7)]
	
	for i in range(numimages):
		align = aligns[random.randrange(0,3)]
		alignlist.append(align)

	f2.write("<slide>\n")	
	if(numimages == 1):
		a = a + 1
		f2.write("<image align=\"center\"></image>\n")
	
	elif(numimages == 2):
		b = b + 1
		f2.write("<image align=\"left\"></image>\n")
		f2.write("<image align=\"right\"></image>\n")

	elif(numimages == 3):
		c = c + 1
		f2.write("<image align=\"left\"></image>\n")
		f2.write("<image align=\"center\"></image>\n")
		f2.write("<image align=\"right\"></image>\n")

	else:
		d = d + 1
		for i in alignlist:
			f2.write("<image align=\""+i+"\"></image>\n")
	f2.write("</slide>\n")

	f1.write("<slide>\n")
	for i in alignlist:
		f1.write("<image align=\""+i+"\"></image>\n")
	f1.write("</slide>\n")

			
f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c,d

# # # ###########################################################################################

random.seed(11)

aligns = ['left','right','center']
nums = [1,2,3,4,5,6,7]

f1 = open('../test/input6.xml','w')
f2 = open('../test/output6.xml','w')

f1.write("<ppt>\n")
f2.write("<ppt>\n")
a = 0
b = 0
c = 0
d = 0

for j in range(20):
	
	alignlist = []

	numimages = nums[random.randrange(0,7)]
	
	for i in range(numimages):
		align = aligns[random.randrange(0,3)]
		alignlist.append(align)

	f2.write("<slide>\n")	
	if(numimages == 1):
		a = a + 1
		f2.write("<image align=\"center\"></image>\n")
	
	elif(numimages == 2):
		b = b + 1
		f2.write("<image align=\"left\"></image>\n")
		f2.write("<image align=\"right\"></image>\n")

	elif(numimages == 3):
		c = c + 1
		f2.write("<image align=\"left\"></image>\n")
		f2.write("<image align=\"center\"></image>\n")
		f2.write("<image align=\"right\"></image>\n")

	else:
		d = d + 1
		for i in alignlist:
			f2.write("<image align=\""+i+"\"></image>\n")
	f2.write("</slide>\n")

	f1.write("<slide>\n")
	for i in alignlist:
		f1.write("<image align=\""+i+"\"></image>\n")
	f1.write("</slide>\n")

			
f1.write("</ppt>")
f1.close()
f2.write("</ppt>")
f2.close()

print a,b,c,d