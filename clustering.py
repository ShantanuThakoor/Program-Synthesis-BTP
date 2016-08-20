from framework import *
from grammar import *
from substitution import *
from ranking import *

class Cluster:
	def __init__(inputLGG, outputLGG, inputList, outputList):
		self.inputLGG = inputLGG
		self.outputLGG = outputLGG
		self.inputList = inputList
		self.outputList = outputList

def FormClusters(inputList, outputList):
	clusters = []
	
