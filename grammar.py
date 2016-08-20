
EMPTY = 0
LIST = 1
ROOT = 2
LOOP = 3


class Program:
	def __init__(self, input, output):
		self.input = input
		self.output = output

def pretty(m):
	s = "{"
	for i in m:
		s += str(i) + " : " + ("fof " if m[i]._type == FEXP else "") + str(m[i].v) + "| "
	s += "}"
	return s

class TreeExp:
	def printTree(self, indent=0):
		if self._type == EMPTY:
			print " "*indent,"[EMPTY]"
		if self._type == ROOT:
			print " "*indent,"[ROOT",self.tag," ",pretty(self.map)," ]"
			if self.children._type == LIST:
				for x in self.children.list:
					x.printTree(indent+4)
		if self._type == LIST:
			print " "*indent,"[BEGINLIST"
			for x in self.list:
				x.printTree(indent+4)
			print " "*indent,"ENDLIST]"
		if self._type == LOOP:
			print " "*indent,"[LOOP",self.I.v,"]"
			self.tree.printTree(indent+4)

	def replace(self, x, y):
		if self._type == EMPTY:
			return EmptyTree()
		if self._type == ROOT:
			m = self.map
			for a in m:
				if m[a].v == x.v:
					m[a] = y
			return RootTree(self.tag, m, self.children.replace(x, y))
		if self._type == LOOP:
			return LoopTree(self.I, self.tree.replace(x, y))
		if self._type == LIST:
			l = [z.replace(x, y) for z in self.list]
			return ListTree(l)

	def toXML(self, indent=0):
		if self._type == EMPTY:
			return ""
		if self._type == LOOP:
			raise Exception('printXML', 'Not concrete')
		s = ""
		if self._type == ROOT:
			s += " " * indent
			s += "<"
			s += self.tag
			for x in self.map:
				s += " "
				s += x
				s += "="
				s += self.map[x].v
			s += ">\n"
			s += self.children.toXML(indent+4)
			s += " " * indent
			s += "</"
			s += self.tag
			s += ">\n"
			return s
		if self._type == LIST:
			for t in self.list:
				s += t.toXML(indent)
			return s

def EmptyTree():
	inst = TreeExp()
	inst._type = EMPTY
	return inst

def RootTree(tag, _map, children):
	inst = TreeExp()
	inst.tag = tag
	inst.map = _map
	inst.children = children
	inst._type = ROOT
	return inst


def ListTree(treeList, o=None):
	if o is not None:
		return ListTree2(treeList, o)
	inst = TreeExp()
	inst._type = LIST
	inst.list = treeList
	return inst

def ListTree2(head, tail):
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
	return inst


def LoopTree(I, tree):
	inst = TreeExp()
	inst.I = I
	inst.tree = tree
	inst._type = LOOP
	return inst


def asList(tree):
	if tree._type == EMPTY:
		return ListTree([])
	return ListTree(tree, EmptyTree())

def asAtomic(tree):
	if tree._type in [ROOT, LOOP, EMPTY]:
		return tree
	if len(tree.list) == 1:
		inst = tree.list[0]
		return inst
	if len(tree.list) == 0:
		return EmptyTree()
	return tree

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



	