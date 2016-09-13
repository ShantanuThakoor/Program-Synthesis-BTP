import sys
args = sys.argv

f = open(args[1],'r').readline()
g = open(args[2],'w')

for i in f:
	if i == "<table>\n":
		g.write("1\n")

	elif i == "<list>\n":
		g.write("2\n")

	elif i == "<textbox>\n"
		g.write("3\n")