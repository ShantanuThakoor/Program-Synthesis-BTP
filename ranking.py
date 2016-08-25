from framework import *
from grammar import *
from substitution import *
from clustering import *

INFI = 10**5

def MatchScore(cluster, input, coeffs):
	try:
		newInputLGG = InferTreeExp(frozenset(), [cluster.inputLGG, input])
		runProgram(Program(cluster.inputLGG, cluster.outputLGG), input)
	except:
		return INFI

	# define some measure of how much the LGG has changed
	# old and new inputLGG:
	# 0) frequency
	# 1) number of variables 
	# 2) number of iterators 
	# 3) number of variable free nodes
	# 4) number of iterator free nodes
	# 5) many more features...
	# learn a linear combination of these to return the score

	features = [len(cluster.inputList),
				len(Var(newInputLGG)),
				len(Var(cluster.inputLGG)),
				len(Iter(newInputLGG)),
				len(Iter(cluster.inputLGG)),
				]

	sum = 0
	for i in range(len(features)):
		sum = sum + feautures[i] * coeffs[i]

	return sum