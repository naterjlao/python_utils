############################################################
# File: helpers.py
# Path: python_utils/
# Author: Nathaniel Lao (lao.nathan95@gmail.com)
# 
# General utility functions for various use cases.
############################################################

import random

############################################################
# Returns a random list of n integers.
############################################################
def gen_randomlist(n=10,low=-10,high=10):
	rlist = []
	for i in range(0,n):
		rlist.append(random.randrange(low,high))
	return rlist

############################################################
# Returns the integer root of n in respect to the base number.
# Return None if n is not a power of the base.
############################################################
def get_root(n,base=2):
	if (not isinstance(n, int) or n <= 0):
		print("ERROR: n must be an integer greater than 0.")
		return None
	else:
		exponent = 0
		while (base ** exponent <= n):
			if (base ** exponent == n):
				return exponent
			else:
				exponent += 1
			
		return None
	
