from grammar import *
from substitution import *

VarMap = dict()
InverseVarMap = dict()
IterMap = dict()
Var = set()

def flatten(l):
	return [val for sublist in l for val in sublist]

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

def InferTreeExp(s, treeList):
	allEmpty = True
	for x in treeList:
		if asAtomic(x)._type != EMPTY:
			allEmpty = False
			break
	if allEmpty:
		return TreeExp.EmptyTree()
	candidates = [flatten(Root(x)) for x in treeList]
	filtered = []
	for x in candidates:
		works = False
		for t in treeList:
			if firstRoot(t, x):
				works = True
				break
		if works:
			filtered.append(x)
	e = None
	for x in filtered:
		works = True
		for t in treeList:
			if x in Root(t) and not FirstRoot(t, x):
				works = False
				break
		if works:
			e = x
			break
	if e is None:
		raise Exception('InferTreeExp', 'No e')
	


def InferAttMap(s, mlist):
	domain = mlist[0].keys()
	for x in mlist:
		if x.keys() != domain:
			raise Exception('InferAttMap', 'Domains mismatch')
	phi = dict()
	for a in domain:
		v = mlist[0][a]
		allSame = True
		for x in mlist:
			if x[a] != v:
				allSame = False
				break
		if allSame:
			phi[a] = v
		else:
			phi[a] = VarMap[(s, [y[a] for y in mlist])]
	return phi

def GetLiterals(x1, x2):
	if x1 not in InverseVarMap or x2 not in InverseVarMap:
		raise Exception('Get Literals', 'Unknown variables')
	preimage1 = InverseVarMap[x1]
	preimage2 = InverseVarMap[x2]
	if len(preimage1[1]) != len(preimage2[1]):
		raise Exception('Get Literals', 'Lengths not same')
	if preimage1[0] != preimage2[0]:
		raise Exception('Get Literals', 'Scope different')
	R = set()
	for i in range(len(preimage1[1])):
		if preimage1[1][i] in Var and preimage2[1][i] in Var:
			R = R | GetLiterals(preimage1[1][i], preimage2[1][i])
		elif preimage1[1][i] not in Var and preimage2[1][i] not in Var:
			R = R | set([preimage1[1][i], preimage2[1][i]])
		else:
			raise Exception('Get Literals', 'Apparent mismatch of literal and variable')
	return R
