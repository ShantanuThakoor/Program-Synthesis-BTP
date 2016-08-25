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

def listFromFile(file):
	raw = ET.parse(file).getroot()
	treeList = [createExpTree(x) for x in raw]
	return treeList

inputFile = "training/input%d.xml"
outputFile = "training/output%d.xml"
rankingInputFile = "ranking/input%d.xml"
rankingOutputFile = "ranking/output%d.xml"
testInputFile = "test/input%d.xml"
testOutputFile = "test/output%d.xml"

def EntireTest():
	i = 0
	inputList = listFromFile(inputFile % i)
	outputList = listFromFile(outputFile % i)
	rankingInputList = listFromFile(rankingInputFile % i)
	rankingOutputList = listFromFile(rankingOutputFile % i)
	testInputList = listFromFile(testInputFile % i)
	testOutputList = listFromFile(testOutputFile % i)

	clusters = FormClusters(inputList, outputList)
	# print len(clusters)
	# for x in clusters:
	# 	x.inputLGG.printTree()
	# 	x.outputLGG.printTree()
	# 	print "\n"

	data = CreateIdealMatchings(clusters, rankingInputList, rankingOutputList)
	
	for i in range(len(data[0])):
		print data[0][i], data[1][i]

	classifier = LearnWeights(data)
	print classifier.coef_[0]
	failedInputs = []
	failedPredictions = []
	failedOutputs = []

	for i in range(len(testInputList)):
		input = testInputList[i]
		output = testOutputList[i]

		prediction = GetBestOutput(clusters, input, classifier)
		p = prediction.toXML()
		o = output.toXML()

		if p != o:
			failedInputs += [input.toXML()]
			failedPredictions += [prediction.toXML()]
			failedOutputs += [output.toXML()]



EntireTest()