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
	except:
		return None

def FormClusters(inputList, outputList):
	clusters = []
	for i in range(len(inputList)):
		input, output = inputList[i], outputList[i]
		best = -1
		for j in range(len(clusters)):
			newProgram = combine(input, output, clusters[j])
			if newProgram is None:
				continue
			clusters[j].inputList = clusters[j].inputList + [input]
			clusters[j].outputList = clusters[j].outputList + [output]
			clusters[j].inputLGG, clusters[j].outputLGG = newProgram.input, newProgram.output
			best = j
			break
		if best >= 0:
			continue
		clusters.append(Cluster(input, output, [input], [output]))
	return clusters


