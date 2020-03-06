################################################################################
# File:          requirements.py
# Date created:  03/01/2020
# Author:        Nate Lao (lao.nathan@yahoo.com)
#
# Description:   Defines the classes for representing a software project's
#                Requirements
################################################################################

import config

# Defines a requirement
class Req:
	def __init__(self,id, description):
		# These must be added upon instantiation
		self.id = id
		self.description = description
		
		# This must be set by a method
		self.parent = None
		
		# This is inherited by parent.
		# If at top, use specialized methods
		self.phase	= None
		self.parent_description = None
		
		# Don't care:
		# - parent_phase
		# - comment
		# - num
		
		# Not implemented yet (TBD)
		# - test_procedure
		# - test_id
		
	def __str__(self):
		output = ""
		output += "id: %s\n" % self.id
		output += "description: %s\n" % self.description
		output += "parent: %s\n" % ("None" if self.parent == None else self.parent.id)
		output += "phase: %s\n" % self.phase
		output += "parent_description: %s\n" % self.parent_description
		return output
	
	def setParent(self,parent):
		# Hardcoding typechecking because explicit type on certain 
		# instances do not work
		if (parent.__class__ != Req):
			raise TypeError("requirement parent must be a requirement (Req)")
		if (parent == self):
			raise ValueError("a requirement cannot be a parent of itself")
		self.parent = parent
		self.inherit()
	
	def setPhase(self,phase, force=False):
		# If there is already a parent requirement,
		# do not override the requirement, unless
		# <force>
		if (self.parent != None and not force):
			self.inherit()
		else:
			self.phase = phase
	
	# Recursive call that retrieves
	# the phase and description of the
	# parent and sets it to the child
	# (current object). Halts when there
	# are no parent
	def inherit(self):
		if (self.parent != None):
			self.parent.inherit()
			self.phase = self.parent.phase
			self.parent_description = self.parent.description
		

# TODO
# imports the given <filename> and returns a ReqTable
# object representation
def importCSV(filename):
	pass
	
	
# MAIN TEST DRIVER
if __name__ == "__main__":
	print("fjkdefjdk")
	r = Req("sw2","hjkhjkhjk")
	s = Req("sw1","jfkdhfdklfjdkljfl")
	r.setParent(s)
	print(r)



