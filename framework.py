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
	rList = []
	tPrimeList = []
	for t in treeList:
		tempList = asList(t)
		tempRList = []
		while tempList:
			r = tempList[0]
			if Root(r) == set([e]):
				tempRList.append(r)
				tempList.pop(0)
			else:
				break
		tempTPrime = TreeExp.ListTree(tempList)
		rList.append(tempRList)
		tPrimeList.append(tempTPrime)
	tau = InferTreeExp(s, tPrimeList)
	M = len(rList[0])
	if M*len(rList) == [len(x) for x in rList]:
		rhoList = []
		for j in range(M):
			rhoj = InferRootExp(s, [x[j] for x in rList])
			rhoList.append(rhoj)
		rhoList.append(tau)
		return TreeExp.ListTree(rhoList)
	I = IterMap((s, [len(x) for x in rList]))
	rho = InferRootExp([s, I], flatten(rList))
	loopTree = TreeExp.LoopTree(I, rho)
	return TreeExp.ListTree(loopTree, tau)

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
	return TreeExp.RootTree(e, phi, tau)

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
