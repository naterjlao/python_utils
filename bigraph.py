############################################################
# File: bigraph.py
# Author: Nathaniel Lao
#
# Class Declaration of a bidirectional graph to be implemented in
# racetrack. This is to serve as a way to store checkpoints
# of the car's track so that it can efficient traverse the
# maze. This will implement Djkstra's algorithm to find
# the least cost path.
#
# Better search algorithms can be used for more harder cases, 
# but since the problem set is relative simple, Djkstra's
# algorithm will offer reasonable efficiency with the added
# benefit of finding the absolute least cost path.
#
# The weights of edges are defined by their Euclidean distances
# their vertices. This is automatically calculated once an
# edge is defined.
#
# This graph is bi-directional. Once an edge is created, a
# corresponding complementary edge is created alongside it.
# In code, this is representated as two independent edges 
# existing in the graph.
############################################################

import math

class Bigraph:
	def __init__(self):
		self.vertices = []
		self.edges = []
	
	########################################################
	# Returns a list of vertices representing the least cost
	# path from the source vertex to the destination vertex.
	# This is calculated using the djkstra function.
	# Returns a list from the source vertex (exclusive) to the
	# destination vertex (inclusive).
	########################################################
	def lcp(self,source,dest):
		# If the source and dest vertices do not exist, return None
		if (source not in self.vertices or dest not in self.vertices): 
			return None
		
		#TODO Debug
		#print("Performing Djkstra")
		preds = self.djkstra(source)[0]
		path = []
		
		while (dest != source and dest != None):
			path.insert(0,dest)
			dest = preds[self.vertices.index(dest)]			
		
		# Finally, add the source vertex
		path.insert(0,source)
		
		if (dest != source):
			print("ERROR: No viable path from source to destination vertex found.")
			return None
		else:
			#TODO Debug
			#print("Finding best path")
			return path
	
	########################################################
	# Performs Djkstra's algorithm on the graph based on the
	# provided source vertex.
	# Returns a 2-tuple containing:
	#	-a list of vertices representing the predecessor of 
	#		each corresponding vertex in vertices.
	#	-a list of all corresponding path weights in vertices
	########################################################	
	def djkstra(self,source):
		if (source not in self.vertices):
			print("ERROR: Source vertex not found in the graph.")
			return None
	
		# Number of vertices in the graph	
		NUM_V = len(self.vertices)
		
		weights = [] # Weight of each vertex
		traversed = [] # True or False depending if the vertex has been traversed
		num_traversed = 0 # Number of vertices processed
		preds = [] # Contains the preceding vertex
		
		# Initialization: set weights to infinity except for source
		# Set traversed for all vertices to False
		# Set predecessor for all vertices to None
		for vertex in self.vertices:
			weights.append(0 if vertex == source else math.inf)
			traversed.append(False)
			preds.append(None)
			
		while num_traversed < NUM_V:
			# Find the vertex with the smallest weight
			min_i = -1
			min_w = math.inf
			for i in range(0,NUM_V):
				if (not traversed[i] and weights[i] <= min_w):
					min_i = i
					min_w = weights[i]
			min_v = self.vertices[min_i]
			
			# Find all outgoing paths from the min vertex
			# Replace the destination's preds and weight 
			# if a shorter distance is found
			out_edges = self.find_edges(min_v)
			for edge in out_edges:
				# The new weight is the sum of the current edge's
				# weight and the current minimum vertex
				new_weight = edge.weight + weights[min_i]
				
				# If the new weight is less than the destination's
				# current weight, replace its predecessor and weight
				dest_i = self.vertices.index(edge.vd)
				if (new_weight < weights[dest_i]):
					weights[dest_i] = new_weight
					preds[dest_i] = edge.vs
			
			# Keep track of the traversed vertices
			traversed[min_i] = True
			num_traversed += 1
			
		return (preds,weights)
	
	########################################################
	# Returns all of the outgoing edges from a given vertex.
	# If the vertex does not exist in the graph or if there 
	# are no outoing edges, an empty list is returned. Otherwise,
	# a list of all outgoing edges are returned.
	########################################################
	def find_edges(self,vertex):
		if vertex in self.vertices:
			out_edges = []
			for edge in self.edges:
				if edge.vs == vertex: out_edges.append(edge)
			return out_edges
		else:
			return []
		
	########################################################
	# Adds a vertex to the graph. If the vertex already exists,
	# nothing is added and False is returned. Else, the 
	# vertex is added and True is returned.
	########################################################
	def add_vertex(self,vertex):
		if vertex in self.vertices:			
			return False
		else:
			self.vertices.append(vertex)
			return True
	
	########################################################
	# Adds an edge to the graph. An edge must consist of
	# existing vertices. If any vertices do not exist, nothing 
	# happens and False is returned. If the edge already exists, 
	# nothing happens and False is returned. Else, the edge
	# is added to the graph and True is returned. Note that
	# a copy of an edge is added, which is flipped version of
	# source and destination vertices, this is to make the graph
	# bi-directional.
	########################################################
	def add_edge(self,vs,vd):
		if (vs not in self.vertices or vd not in self.vertices):
			return False
		else:
			fwd_new_edge = self.Edge(vs,vd)
			bkw_new_edge = self.Edge(vd,vs)
			
			if (fwd_new_edge in self.edges or bkw_new_edge in self.edges):
				return False
			else:
				self.edges.append(fwd_new_edge)
				self.edges.append(bkw_new_edge)
				return True
		
	########################################################
	# Inner class definition of an edge. An edge is defined
	# as a straight line from the source vertex to the destination
	# vertex. The weight of the edge is calculated during
	# initialization. This edge implementation is unidirectional,
	# meaning that there is a source vertex and a destination vertex.
	########################################################	
	class Edge:
		def __init__(self,vs,vd):
			self.vs = vs
			self.vd = vd
			self.weight = self.weight(vs,vd)
			
		####################################################
		# Weight is defined as the euclidean distance between
		# two vertices.
		####################################################
		def weight(self,vs,vd):
			(x0,y0) = vs
			(x1,y1) = vd
			return math.sqrt(math.pow((x0-x1),2) + math.pow((y0-y1),2))

		####################################################
		# Override equals method
		####################################################
		def __eq__(self,other):
			if isinstance(other,Bigraph.Edge):
				return self.vs == other.vs and self.vd == other.vd
			else:
				return False
		
		####################################################
		# String output representation
		####################################################
		def __str__(self):
			return "{} -> {} w: {}".format(self.vs,self.vd,self.weight)
		





