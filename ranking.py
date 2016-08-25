from framework import *
from grammar import *
from substitution import *
from clustering import *

INFI = 10**5


def getFeatures(cluster, input):
	newInputLGG = InferTreeExp(frozenset(), cluster.inputList + [input])
	RunProgram(Program(cluster.inputLGG, cluster.outputLGG), input)
	
	return [len(cluster.inputList),
			len(Var(cluster.inputLGG)),
			len(Var(newInputLGG)),
			len(Iter(cluster.inputLGG)),
			len(Iter(newInputLGG)),
			]

def CreateIdealMatchings(clusters, input, output):
	data = ([], [])
	for i in range(len(input)):
		for j in range(len(clusters)):
			try:
				features = getFeatures(clusters[j], input[i])
			except:
				continue
			prediction = execute(clusters[j], input[i])
			predictionXML = prediction.toXML()
			outputXML = output[i].toXML()
			data[0].append(features)
			if predictionXML == outputXML:
				data[1].append(1)
			else:
				data[1].append(0)
	return data

def MatchScore(cluster, input, coeffs):
	try:
		features = getFeatures(cluster, cluster.inputLGG, newInputLGG)
	except:
		return INFI

	sum = 0
	for i in range(len(features)):
		sum = sum + feautures[i] * coeffs[i]

	return sum

def LearnWeights(data):
	from sklearn import svm
	X = data[0]
	Y = data[1]
	clf = svm.LinearSVC()
	clf.fit(X, Y)
	return clf

def GetBestOutput(clusters, input, classifier):
	bestScore = INFI - 1
	best = -1
	weights = classifier.coefs_[0]
	for i in range(len(clusters)):
		newScore = MatchScore(clusters[i], input, weights)
		if newScore <= bestScore:
			bestScore = newScore
			best = i
	if best < 0:
		return input
	try:
		return execute(clusters[best], input)
	except:
		return input
