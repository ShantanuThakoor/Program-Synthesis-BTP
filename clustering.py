from framework import *
from grammar import *
from substitution import *

class Cluster:
	def __init__(self, inputLGG, outputLGG, inputList, outputList):
		self.inputLGG = inputLGG
		self.outputLGG = outputLGG
		self.inputList = inputList
		self.outputList = outputList

def combine(input, output, cluster):
	try:
		return InferProgram(cluster.inputList + [input], cluster.outputList + [output])
		# return InferProgram([cluster.inputLGG, input], [cluster.outputLGG, output])
	except:
		return None

def isJustList(tree):
	if tree._type != LIST:
		return False
	count = 0
	for x in tree.list:
		if x._type != EMPTY:
			count = count + 1
	if count > 1:
		return True
	return False

def tooGeneral(program):
	if isJustList(program.input) or isJustList(program.output):
		return True
	return False

def FormClusters(inputList, outputList):
	clusters = []
	for i in range(len(inputList)):
		input, output = inputList[i], outputList[i]
		best = -1
		for j in range(len(clusters)):
			newProgram = combine(input, output, clusters[j])
			if newProgram is None:
				continue
			if tooGeneral(newProgram):
				continue
			clusters[j].inputList = clusters[j].inputList + [input]
			clusters[j].outputList = clusters[j].outputList + [output]
			clusters[j].inputLGG, clusters[j].outputLGG = newProgram.input, newProgram.output
			best = j
			break
		if best >= 0:
			continue
		# print "New cluster", i
		# input.printTree()
		# output.printTree()
		
		clusters.append(Cluster(input, output, [input], [output]))
	return clusters

def execute(cluster, input):
	return RunProgram(Program(cluster.inputLGG, cluster.outputLGG), input)