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

inputList = [createExpTree(ET.parse('input.xml').getroot())]
outputList = [createExpTree(ET.parse('output.xml').getroot())]

inputList[0].printTree()
outputList[0].printTree()

P = InferProgram(inputList, outputList)

P.input.printTree()
P.output.printTree()
