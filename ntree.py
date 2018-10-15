############################################################
# File: ntree.py
# Class: CMSC421 - Introduction to Artificial Intelligence
# Project: 1 - Racetrack
#
# Defines a datastructure for storing racetrack partitions
# This datastructure is an n-dimensional tree where
# any node can have an arbitrary amount of children.
# This represents the "room" structure of the partitions.
############################################################

############################################################
# Imports
############################################################
import sys
if (sys.version_info[0] < 3):
	import Queue as q # python version 2.x.x
else:
	import queue as q # python version 3.x.x

############################################################
# Simple n dimensional tree stucture for storing partitions.
############################################################
class Ntree:
	def __init__(self,key):
		self.key = key
		self.children = []
		
	########################################################
	# Overrides the comparison method. Compares the associated
	# node key.
	########################################################
	def __gt__(self,other):
		return self.key > other.key
	
	########################################################
	# Returns a string representation of the tree.
	########################################################
	def __str__(self):
		output = "{" + str(self.key) + ": "
		for child in self.children:
			output += str(child) + ", "
		output += "}"	
		
		return output

	########################################################
	# Adds a child to the Node and returns the new child's
	# reference.
	########################################################
	def addchild(self,child):
		self.children.append(child)
		return child
	
	########################################################
	# Returns the child at the associated index.
	########################################################	
	def getchild(self,index):
		return self.children[index]

	########################################################
	# Returns a breadth-first traversal list.
	########################################################
	def bft(self):
		queue = q.Queue()
		queue.put(self)
		bfs_out = []
		while (not queue.empty()):
			current = queue.get()
			bfs_out.append(current.key)
			for child in current.children:
				queue.put(child)
				
		return bfs_out





















