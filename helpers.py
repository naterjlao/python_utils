############################################################
# File: helpers.py
# Class: CMSC421 - Introduction to Artificial Intelligence
# 
# Helper functions for alpha-beta practice.
############################################################

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
	
