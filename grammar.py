
EMPTY = 0
LIST = 1
ROOT = 2
LOOP = 3


class Program:
	def __init__(self, input, output):
		self.input = input
		self.output = output

class TreeExp:
	@staticmethod
	def EmptyTree():
		inst = TreeExp()
		inst._type = EMPTY
		return inst

	@staticmethod
	def RootTree(tag, _map, children):
		inst = TreeExp()
		inst.tag = tag
		inst.map = _map
		inst.children = children
		inst._type = ROOT

	@staticmethod
	def ListTree(treeList):
		inst = TreeExp()
		inst._type = LIST
		inst.list = treeList

	@staticmethod
	def ListTree(head, tail):
		inst = TreeExp()

		firstList = []
		secondList = []
		if head._type in [ROOT, LOOP]:
			firstList = [head]
		if head._type == LIST:
			firstList = head.list
		if tail._type in [ROOT, LOOP]:
			secondList = [tail]
		if tail._type == LIST:
			secondList = tail.list

		inst.list = firstList + secondList
		inst._type = LIST

	@staticmethod
	def LoopTree(I, tree):
		inst = TreeExp()
		inst.I = I
		inst.tree = tree
		inst._type = LOOP

def asList(treegit):
	if tree._type == EMPTY:
		return ListTree([])
	return ListTree(tree, EmptyTree())

def asAtomic(tree):
	if tree._type in [ROOT, LOOP, EMPTY]:
		return tree.copy()
	if len(tree.list) == 1:
		inst = tree.list[0]
		return inst
	if len(tree.list) == 0:
		return EmptyTree()
	return tree.copy()



FEXP = 0
VAR = 1
LIT = 2
ITER = 3

class Val:
	def __init__(self, _type, v, f=None):
		self._type = _type
		self.v = v
		if not f is None:
			self.f = f

class Iter:
	def __init__(self, v):
		self._type = ITER
		self.v = v

# Define Var as a set here



	