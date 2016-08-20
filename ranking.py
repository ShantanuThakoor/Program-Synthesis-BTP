from framework import *
from grammar import *
from substitution import *

INFI = 10**5

def MatchScore(cluster, input, output):
	try:
		newInputLGG = InferTreeExp(frozenset(), cluster.inputList + [input])
		newOutputLGG = InferTreeExp(frozenset(), cluster.outputList + [output])
	except:
		return INFI
	# define some measure of how much the LGG has changed
	# old and new inputLGG:
	# 1) number of variables 
	# 2) number of iterators 
	# 3) number of variable free nodes
	# 4) number of iterator free nodes
	# 5) many more features...
	# learn a linear combination of these to return the score
	return 1