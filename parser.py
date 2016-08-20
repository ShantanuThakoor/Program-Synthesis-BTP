import xml.etree.ElementTree as ET 
from grammar import *
from framework import *

def createExpTree(node):
	e = node.tag
	mapping = dict()
	for key in node.attrib:
		value = node.attrib[key]
		mapping[key] = Val(LIT, value)
	treeList = [createExpTree(c) for c in node]
	tree = ListTree(treeList)
	return RootTree(e, mapping, tree)

i = 0
inputFile = "inputs/input" + str(i) + ".xml"
outputFile = "outputs/output" + str(i) + ".xml"
testInputFile = "testinputs/testinput" + str(i) + ".xml"
testOutputFile = "testoutputs/testoutput" + str(i) + ".xml"

inputs = ET.parse(inputFile).getroot()
outputs = ET.parse(outputFile).getroot()

inputList = [createExpTree(x) for x in inputs]
outputList = [createExpTree(x) for x in outputs]

P = InferProgram(inputList, outputList)

testInput = ET.parse(testInputFile).getroot()
testInput = [createExpTree(x) for x in tests][0]

testOutput = ET.parse(testOutputFile).getroot()
testOutput = [createExpTree(x) for x in testOutput][0]


prediction = RunProgram(P, testInput)

print "Output"
print prediction.toXML()
print "\n"*3
print "Expected output"
print testOutput.toXML()
