from framework import *
from grammar import *
from substitution import *
from clustering import *
from myGlobals import Globals

INFI = 10**5

def getFeatures(cluster, input):
	newInputLGG = InferTreeExp(frozenset(), cluster.inputList + [input])
	Globals.literals = 0
	Globals.variables = 0
	RunProgram(Program(cluster.inputLGG, cluster.outputLGG), input)
	return [len(cluster.inputList),
			len(Var(cluster.inputLGG)),
			len(Var(newInputLGG)),
			len(Iter(cluster.inputLGG)),
			len(Iter(newInputLGG)),
			Globals.literals,
			Globals.variables,
			]

def CreateIdealMatchings(clusters, input, output):
	data = ([], [])
	for i in range(len(input)):
		for j in range(len(clusters)):
			try:
				features = getFeatures(clusters[j], input[i])
			except :
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

def MatchScore(cluster, input, classifier):
	try:
		features = getFeatures(cluster, input)
	except:
		return -1
	return classifier.decision_function([features])[0]

def LearnWeights(data):
	from sklearn import svm
	X = data[0]
	Y = data[1]
	clf = svm.LinearSVC(random_state=0)
	clf.fit(X, Y)
	return clf

def GetBestOutput(clusters, input, classifier):
	bestScore = -INFI
	best = -1
	for i in range(len(clusters)):
		newScore = MatchScore(clusters[i], input, classifier)
		if newScore > bestScore:
			bestScore = newScore
			best = i
	if best < 0:
		return None
	try:
		return execute(clusters[best], input)
	except:
		print "Program failed"
		return None
