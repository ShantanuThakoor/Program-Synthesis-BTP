from grammar import *

def merge(x, y):
	z = x.copy()
	z.update(y)
	return z

def Var(tree):
	if tree._type == EMPTY:
		return set()
	if tree._type == ROOT:
		mapping = tree.map
		temp = [x for x in mapping.values() if x._type == VAR]
		for x in tree.children:
			temp = temp | Var(x)
		return x
	if tree._type == LIST:
		temp = set()
		for x in tree.list:
			temp = temp | Var(x)
		return temp
	if tree._type == LOOP:
		return Var(tree.tree)

def FExp(tree):
	if tree._type == EMPTY:
		return set()
	if tree._type == ROOT:
		mapping = tree.map
		temp = [x for x in mapping.values() if x._type == FEXP]
		for x in tree.children:
			temp = temp | FExp(x)
		return x
	if tree._type == LIST:
		temp = set()
		for x in tree.list:
			temp = temp | FExp(x)
		return temp
	if tree._type == LOOP:
		return FExp(tree.tree)

def Iter(tree):
	if tree._type == EMPTY:
		return set()
	if tree._type == ROOT:
		temp = set()
		for x in tree.children:
			temp = temp | FExp(x)
		return x
	if tree._type == LIST:
		temp = set()
		for x in tree.list:
			temp = temp | FExp(x)
		return temp
	if tree._type == LOOP:
		s = set([tree.I])
		return s | FExp(tree.tree)	


def Root(tree):
	if tree._type == EMPTY:
		return set()
	if tree._type == ROOT:
		return tree.tag
	if tree._type == LOOP:
		if tree.tree._type == ROOT:
			return tree.tree.tag
	if tree._type == LIST:
		temp = set()
		for x in tree.list:
			temp = temp | Root(x)
		return temp

def MatchTree(tau, t):
	
	tau = tau.asList()
	t = t.asList()

	if len(tau.list) == 0 and len(t.list) == 0:
		return dict()

	# currently means that an iterator should have 
	# at least one element in its substitution; may 
	# want to change this later

	if len(tau.list) == 0 or len(t.list) == 0:
		raise Exception('MatchTree', 'Only one argument empty')

	if tau.list[0]._type == ROOT and t.list[0]._type == ROOT:
		if tau.list[0].tag == t.list[0].tag:
			temp1 = MatchMap(tau.list[0].map, t.list[0].map)
			temp2 = MatchTree(tau.list[0].children, t.list[0].children)
			temp3 = MatchTree(tau.list[1:], t.list[1:])
			return merge(temp1, merge(temp2, temp3))

	if tau.list[0]._type == LOOP:
		rho = tau.list[0].tree
		rhoRoot = Root(rho)
		tauPrime = tau.list[1:]
		rList = []
		if not Root(tauPrime).issuperset(rhoRoot):
				while t.list:
					r = t.list[0]
					if Root(r) == rhoRoot:
						rList.append(MatchTree(rho, r))
						t.list.pop(0)
					else:
						break
				d = {tau.list[0].I : rList}
				temp = MatchTree(tauPrime, t.list)
				return merge(temp, d)

	raise Exception('MatchTree', 'No case matched')

def ApplyTree(tau, sigma):
	tau = tau.asAtomic()

	if tau._type == EMPTY:
		return TreeExp.EmptyTree()

	if tau._type == ROOT:
		newMapping = ApplyMap(tau.map, sigma)
		newList = ApplyTree(tau.list, sigma)
		return TreeExp.RootTree(tau.tag, newMapping, newList)

	if tau._type == LOOP:
		if not tau.I in sigma:
			return TreeExp.LoopTree(tau.I, tau.tree)
		sigmaList = sigma[tau.I]
		newList = []
		for x in sigmaList:
			newList = newList + ApplyTree(tau.tree, x)
		return TreeExp.ListTree(newList)

	if tau._type == LIST:
		head = ApplyTree(tau.list[0], sigma)
		tail = ApplyTree(TreeExp.ListTree(tau.list[1:]), sigma)
		return TreeExp.ListTree(head, tail)

	raise Exception('ApplyTree', 'No case matched')

	
def MatchMap(phi, m):
	d = dict()
	for a in Var:
		if not phi[a] in Var:
			if not phi[a] == m[a]:
				raise Exception('MatchMap', 'Not a substitution')
		d = merge(d, {phi[a] : m[a]})
	return d

def ApplyMap(phi, sigma):
	ret = dict()
	for a in phi.keys():
		if phi[a]._type == VAR and sigma[phi[a].v]._type == LIT:
			ret[a] = Val(LIT, sigma[phi[a].v])
		elif phi[a]._type == FEXP and sigma[phi[a].v]._type == LIT:
			ret[a] = Val(LIT, phi[a].f(sigma[phi[a].v]))
		else:
			ret[a] = phi[a]

