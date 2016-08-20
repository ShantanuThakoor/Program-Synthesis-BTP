from grammar import *
from substitution import *

VarMapInternal = dict()
InverseVarMap = dict()
def VarMap(scope, valList):
	global InverseVarMap
	global VarMapInternal
	key = (tuple(scope), tuple(valList))
	if key in VarMapInternal:
		return VarMapInternal[key]
	newX = Val(VAR, "X" + str(len(InverseVarMap)))
	VarMapInternal[key] = newX
	InverseVarMap[newX] = key
	return newX

# Use this one with some modification if the same loop requests an iterator more than once
IterMapInternal = dict()
def IterMap(scope, numList):
	global IterMapInternal
	key = (tuple(scope), tuple(numList))
	if key in IterMapInternal:
		return IterMapInternal[key]
	itersAssigned = len(IterMapInternal)
	newI = Val(ITER, "I" + str(itersAssigned))
	IterMapInternal[key] = newI
	return newI

def setOfPairsToLists(s):
	a = []
	b = []
	for x in s:
		a.append(x[0])
		b.append(x[1])
	return (a, b)

def flatten(l):
	return [val for sublist in l for val in sublist]

def InferIdentity(ios):
	inputs, outputs = setOfPairsToLists(ios)
	inputs = map(lambda x: x.v, inputs)
	outputs = map(lambda x: x.v, outputs)
	if inputs == outputs:
		return lambda x: x
	return None

def InferConst(ios):
	_, outputs = setOfPairsToLists(ios)
	outputs = map(lambda x: x.v, outputs)
	if len(set(outputs)) == 1:
		return lambda x: outputs[0]

def InferDict(ios):
	inputs, outputs = setOfPairsToLists(ios)
	inputs = map(lambda x: x.v, inputs)
	outputs = map(lambda x: x.v, outputs)
	d = dict()
	for i in range(len(inputs)):
		if inputs[i] in d:
			if inputs[i] != outputs[i]:
				return None
		d[inputs[i]] = outputs[i]
	return lambda x : d[x]

def Scope(X):
	if not X in InverseVarMap:
		raise Exception('Scope', 'Variable not mapped to scope')
	return InverseVarMap[X][0]

def InferProgram(inputList, outputList):
	tau1 = InferTreeExp(frozenset(), inputList)
	tau2 = InferTreeExp(frozenset(), outputList)
	for x in Var(tau2) - Var(tau1):
		found = False
		for t in [InferIdentity, InferConst, InferDict]:
			if found:
				break
			for y in [y for y in Var(tau1) if Scope(y) == Scope(x)]:
				f = t(GetLiterals(x, y))
				if f is not None:
					found = True
					tau2 = tau2.replace(x, Val(FEXP, y.v, f))
					break
		if not found:
			raise Exception('InferProgram', 'Could not infer literal functions')
	subsetCond = not Var(tau2).issubset(Var(tau1))
	otherCond = not Iter(tau2).issubset(Iter(tau1))
	if subsetCond or otherCond:
		raise Exception('InferProgram', 'Not subset')
	return Program(tau1, tau2)

def InferTreeExp(s, treeList):
	allEmpty = True
	for x in treeList:
		if asAtomic(x)._type != EMPTY:
			allEmpty = False
			break
	if allEmpty:
		return EmptyTree()
	candidates = flatten([list(Root(x)) for x in treeList])
	candidates = list(frozenset(candidates))
	filtered = []
	for x in candidates:
		works = False
		for t in treeList:
			if FirstRoot(t, x):
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
	rList = []
	tPrimeList = []
	for t in treeList:
		tempList = asList(t)
		tempRList = []
		while tempList.list:
			r = tempList.list[0]
			if Root(r) == frozenset([e]):
				tempRList.append(r)
				tempList.list.pop(0)
			else:
				break
		tempTPrime = ListTree(tempList.list)
		if e in Root(tempTPrime):
			raise Exception('InferTreeExp', 'Weird thing')
		
		rList.append(tempRList)
		tPrimeList.append(tempTPrime)
	tau = InferTreeExp(s, tPrimeList)
	M = len(rList[0])
	if [M]*len(rList) == [len(x) for x in rList]:
		rhoList = []
		for j in range(M):
			rhoj = InferRootExp(s, [x[j] for x in rList])
			rhoList.append(rhoj)
		rhoList.append(tau)
		return ListTree(rhoList)
	I = IterMap(tuple(s), tuple([len(x) for x in rList]))
	rho = InferRootExp(s | frozenset([I]), flatten(rList))
	loopTree = LoopTree(I, rho)
	return ListTree(loopTree, tau)

def InferRootExp(s, rList):
	rList = [asAtomic(x) for x in rList]
	mList = []
	tList = []
	e = rList[0].tag
	for r in rList:
		if r._type != ROOT:
			raise Exception('InferRootExp', 'NonRoot in arguments')
		if r.tag != e:
			raise Exception('InferRootExp', 'Root with different tag')
		mList.append(r.map)
		tList.append(r.children)
	phi = InferAttMap(s, mList)
	tau = InferTreeExp(s, tList)
	return RootTree(e, phi, tau)

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
			if x[a].v != v.v:
				allSame = False
				break
		if allSame:
			phi[a] = v
		else:
			phi[a] = VarMap(s, [y[a] for y in mlist])
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
	R = frozenset()
	for i in range(len(preimage1[1])):
		if preimage1[1][i]._type == VAR and preimage2[1][i]._type == VAR:
			R = R | GetLiterals(preimage1[1][i], preimage2[1][i])
		elif preimage1[1][i]._type == LIT and preimage2[1][i]._type == LIT:
			R = R | frozenset([(preimage1[1][i], preimage2[1][i])])
		else:
			raise Exception('Get Literals', 'Apparent mismatch of literal and variable')
	return R

def RunProgram(P, t):
	sigma = MatchTree(P.input, t)
	P.output.printTree()
	tPrime = ApplyTree(P.output, sigma)
	if len(Var(tPrime)) == 0 and len(Iter(tPrime)) == 0:
		return tPrime
	raise Exception('RunProgram', 'Output not concrete')

def main(inputList, outputList, newInput):
	P = InferProgram(inputList, outputList)
	return RunProgram(P, newInput)
