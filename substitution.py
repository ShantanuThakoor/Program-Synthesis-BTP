
from grammar import *
def merge(x, y):
	z = x.copy()
	z.update(y)
	return z

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
	if tau._type == EMPTY and t._type == EMPTY:
		return {}

	if tau._type == LIST and t._type == LIST:
		if tau.list[0]._type == ROOT and t.list[0]._type == ROOT:
			if tau.list[0].tag == t.list[0].tag:
				temp1 = MatchMap(tau.list[0].map, t.list[0].map)
				temp2 = MatchTree(tau.list[0].children, t.list[0].children)
				temp3 = MatchTree(tau.list[1:], t.list[1:])
				return merge(temp1, merge(temp2, temp3))

	if tau._type == LIST and tau.list[0]._type == LOOP:
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
	if tau._type == EMPTY:
		return tau
	

def MatchMap(phi, m):
	d = {}
	for a in Var:
		if not phi[a] in Var:
			if not phi[a] == m[a]:
				raise Exception('MatchMap', 'Not a substitution')
		d = merge(d, {phi[a] : m[a]})
	return d

def ApplyMap(phi, sigma):
	ret = {}
	for a in phi.keys():
		if phi[a]._type == VAR and sigma[phi[a].v]._type == LIT:
			ret[a] = Val(LIT, sigma[phi[a].v])
		elif phi[a]._type == FEXP and sigma[phi[a].v]._type == LIT:
			ret[a] = Val(LIT, phi[a].f(sigma[phi[a].v]))
		else:
			ret[a] = phi[a]

