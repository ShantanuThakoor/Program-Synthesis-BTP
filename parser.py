import xml.etree.ElementTree as ET 
from grammar import *
from framework import *

def createExpTree(node):
	e = node.tag
	mapping = node.attrib
	treeList = [createExpTree(c) for c in node]
	tree = TreeExp.ListTree(treeList)
	return TreeExp.RootTree(e, mapping, tree)

inputList = [createExpTree(ET.parse('input.xml').getroot())]
outputList = [createExpTree(ET.parse('output.xml').getroot())]

P = InferProgram(inputList, outputList)

P.input.printTree()
P.output.printTree()
