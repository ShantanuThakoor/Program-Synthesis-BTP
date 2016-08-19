import xml.etree.ElementTree as ET 
from grammar import *
from framework import *

def createExpTree(node):
	e = node.tag
	mapping = dict()
	for key in node.attrib:
		value = node.attrib[key]
		mapping[key] = Val('LIT', value)
	treeList = [createExpTree(c) for c in node]
	tree = ListTree(treeList)
	return RootTree(e, mapping, tree)

inputs = ET.parse('input.xml').getroot()
outputs = ET.parse('output.xml').getroot()

inputList = [createExpTree(x) for x in inputs]
outputList = [createExpTree(x) for x in outputs]

r = Root(inputList[0])

print r
print FirstRoot(asAtomic(inputList[0]), r)

P = InferProgram(inputList, outputList)

P.input.printTree()
P.output.printTree()
