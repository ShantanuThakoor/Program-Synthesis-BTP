
EMPTY = 0
LIST = 1
ROOT = 2
LOOP = 3


class Program:
	def __init__(self, input, output):
		self.input = input
		self.output = output

class TreeExp:
	def __init__(self):
		self._type = EMPTY

	def __init__(self, tag, _map, children):
		self.tag = tag
		self.map = _map
		self.children = children
		self._type = ROOT

	def __init__(self, head, tail):
		self.list = append(head, tail)
		self._type = LIST

	def __init__(self, I, tree):
		self.I = I
		self.tree = tree
		self._type = LOOP


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



	