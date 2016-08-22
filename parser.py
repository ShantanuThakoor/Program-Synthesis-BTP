import xml.etree.ElementTree as ET 
from grammar import *
from framework import *
from clustering import *

def createExpTree(node):
	e = node.tag
	mapping = dict()
	for key in node.attrib:
		value = node.attrib[key]
		mapping[key] = Val(LIT, value)
	treeList = [createExpTree(c) for c in node]
	tree = ListTree(treeList)
	return RootTree(e, mapping, tree)

debug = True

i = 1
inputFile = "inputs/input" + str(i) + ".xml"
outputFile = "outputs/output" + str(i) + ".xml"
testInputFile = "testinputs/testinput" + str(i) + ".xml"
testOutputFile = "testoutputs/testoutput" + str(i) + ".xml"

inputs = ET.parse(inputFile).getroot()
outputs = ET.parse(outputFile).getroot()

inputList = [createExpTree(x) for x in inputs]
outputList = [createExpTree(x) for x in outputs]

P = InferProgram(inputList, outputList)

if debug:
	P.input.printTree()
	P.output.printTree()

temp = ET.parse(testInputFile).getroot()
testInputList = [createExpTree(x) for x in temp]

temp = ET.parse(testOutputFile).getroot()
testOutputList = [createExpTree(x) for x in temp]

for i in range(len(testInputList)):
	prediction = RunProgram(P, testInputList[i])

	print "Output"
	print prediction.toXML()
	print "\n"*3
	print "Expected output"
	print testOutputList[i].toXML()
