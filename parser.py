import xml.etree.ElementTree as ET 
from grammar import *
from framework import *
from clustering import *
from ranking import *

def createExpTree(node):
	e = node.tag
	mapping = dict()
	for key in node.attrib:
		value = node.attrib[key]
		mapping[key] = Val(LIT, value)
	treeList = [createExpTree(c) for c in node]
	tree = ListTree(treeList)
	return RootTree(e, mapping, tree)

debug = False

def singleTesting():
	i = 1
	inputFile = "inputs/input%d.xml" % i
	outputFile = "outputs/output%d.xml" % i
	testInputFile = "testinputs/testinput%d.xml" % i
	testOutputFile = "testoutputs/testoutput%d.xml" % i

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

		print "Output %d" % i
		print prediction.toXML()
		print "\n"
		print "Expected output %d" % i
		print testOutputList[i].toXML()
		print "\n"
	
def clusterTesting():
	
	i = 4
	inputFile = "inputs/input%d.xml" % i
	outputFile = "outputs/output%d.xml" % i
	# testInputFile = "testinputs/testinput%d.xml" % i
	# testOutputFile = "testoutputs/testoutput%d.xml" % i

	inputs = ET.parse(inputFile).getroot()
	outputs = ET.parse(outputFile).getroot()

	inputList = [createExpTree(x) for x in inputs]
	outputList = [createExpTree(x) for x in outputs]

	clusters = FormClusters(inputList, outputList)
	print len(clusters)
	for i in range(len(clusters)):
		print i
		clusters[i].inputLGG.printTree()
		clusters[i].outputLGG.printTree()
		print "\n"*3

clusterTesting()