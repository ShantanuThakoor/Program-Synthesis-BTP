from grammar import *
from substitution import *

VarMap = dict()
InverseVarMap = dict()
IterMap = dict()

def InferLiteralFunction(inputs, outputs):
	d = dict()
	for i in range(len(inputs)):
		d[inputs[i]] = outputs[i]
	randomElement = outputs[0]
	def func(x):
		if x in d:
			return d[x]
		return randomElement
	return func

def GetLiterals(x1, x2):
	if x1 not in InverseVarMap or x2 not in InverseVarMap:
		raise Exception('Get Literals', 'Unknown variables')
	preimage1 = InverseVarMap[x1]
	preimage2 = InverseVarMap[x2]
	if len(preimage1[1]) != len(preimage2[1]):
		raise Exception('Get Literals', 'Lengths not same')
	if preimage1[0] != preimage2[0]:
		raise Exception('Get Literals', 'Scope different')