import xml.etree.ElementTree as ET 
from grammar import *
from framework import *
from clustering import *
from ranking import *
import sys

args = sys.argv


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
	i = int(args[1])
	inputList = listFromFile(inputFile % i)
	outputList = listFromFile(outputFile % i)
	rankingInputList = listFromFile(rankingInputFile % i)
	rankingOutputList = listFromFile(rankingOutputFile % i)
	testInputList = listFromFile(testInputFile % i)
	testOutputList = listFromFile(testOutputFile % i)

	clusters = FormClusters(inputList, outputList)
	print len(clusters)
	for x in clusters:
		x.inputLGG.printTree()
		x.outputLGG.printTree()
		print "\n"

	# for x in testInputList:
	# 	x.printTree()
	# 	output = RunProgram(Program(clusters[0].inputLGG, clusters[0].outputLGG), x)
	# 	output.printTree()
	# 	print "\n"

	data = CreateIdealMatchings(clusters, rankingInputList, rankingOutputList)
	# print data
	classifier = LearnWeights(data)
	print classifier.coef_
	failedInputs = []
	failedPredictions = []
	failedOutputs = []
	printFailues = False

	################################## Train ###############################
	failedInputs = []
	failedPredictions = []
	failedOutputs = []
	for i in range(len(inputList)):
		input = inputList[i]
		output = outputList[i]

		prediction = GetBestOutput(clusters, input, classifier)
		if prediction is not None:
			p = prediction.toXML()
		else:
			p = "No prediction"
		o = output.toXML()

		if p != o:
			inp = input.toXML()
			failedInputs += [inp]
			failedPredictions += [p]
			failedOutputs += [o]
			if printFailues:
				print "Number ", i
				print "Input\n", inp
				print "Prediction\n", p
				print "Output\n", o

	num = len(inputList)
	failed = len(failedInputs)
	print "%d of %d successfully predicted" % (num - failed, num)

	################################## Ranking ###############################
	failedInputs = []
	failedPredictions = []
	failedOutputs = []
	for i in range(len(rankingInputList)):
		input = rankingInputList[i]
		output = rankingOutputList[i]

		prediction = GetBestOutput(clusters, input, classifier)
		if prediction is not None:
			p = prediction.toXML()
		else:
			p = "No prediction"
		o = output.toXML()

		if p != o:
			inp = input.toXML()
			failedInputs += [inp]
			failedPredictions += [p]
			failedOutputs += [o]
			if printFailues:
				print "Number ", i
				print "Input\n", inp
				print "Prediction\n", p
				print "Output\n", o

	num = len(rankingInputList)
	failed = len(failedInputs)
	print "%d of %d successfully predicted" % (num - failed, num)

	##################################### Test #####################################
	failedInputs = []
	failedPredictions = []
	failedOutputs = []
	for i in range(len(testInputList)):
		input = testInputList[i]
		output = testOutputList[i]

		prediction = GetBestOutput(clusters, input, classifier)
		if prediction is not None:
			p = prediction.toXML()
		else:
			p = "No prediction"
		o = output.toXML()

		if p != o:
			inp = input.toXML()
			failedInputs += [inp]
			failedPredictions += [p]
			failedOutputs += [o]
			if printFailues:
				print "Number ", i
				print "Input\n", inp
				print "Prediction\n", p
				print "Output\n", o

	num = len(testInputList)
	failed = len(failedInputs)
	print "%d of %d successfully predicted" % (num - failed, num)

EntireTest()