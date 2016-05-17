#!/bin/python

class face(object):
	"""A Class to represent a face"""
	center = (0,0)
	width = 0
	height = 0
	vector = [0]
	
	def __init__(self, center=(0,0), width=0, height=0, vector):
		""" Input params are (x,y) coords of center of face's bounding box, width
		    and height of box and the 128-dimensional vector representation of the face """ 
		super(face, self).__init__()
		self.center = center
		self.width = width
		self.height = height
		self.vector = vector
	
