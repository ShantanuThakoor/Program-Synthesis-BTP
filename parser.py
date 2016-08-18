import xml.etree.ElementTree as ET 
from grammar import *

tree = ET.parse('input.xml')
root = tree.getroot()

def createExpTree(node):
	e = node.tag
	mapping = node.attrib
	treeList = [createExpTree(c) for c in node]
	tree = TreeExp.ListTree(treeList)
	return TreeExp.RootTree(e, mapping, tree)


