import xml.etree.ElementTree as ET 
from grammar import *
from framework import *

def createExpTree(node):
	e = node.tag
	mapping = dict()
	for key in node.attrib:
		value = node.attrib[key]
		mapping[key] = Val(LIT, value)
	treeList = [createExpTree(c) for c in node]
	tree = ListTree(treeList)
	return RootTree(e, mapping, tree)

inputs = ET.parse('input1.xml').getroot()
outputs = ET.parse('output1.xml').getroot()

inputList = [createExpTree(x) for x in inputs]
outputList = [createExpTree(x) for x in outputs]

P = InferProgram(inputList, outputList)

tests = ET.parse('test1.xml').getroot()
testList = [createExpTree(x) for x in tests]
t = testList[0]

t.printTree()
t = RunProgram(P, t)

s = t.toXML()
print s
