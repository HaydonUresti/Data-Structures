class BST:
	"""A binary search tree object. Node is a 
	subclass of BST.
	"""

	class Node:
		""" A node of a BST. Starts with a single 
		node and is added onto to build a BST.
		"""

		def __init__(self, data):
			"""Creates a node storing the given 
			data. 
			"""
			self.data = data
			self.left = None
			self.right = None
	def __init__(self):
		"""Initializes an emoty BST
		"""

		self.root = None

	def insert(self, data):
		"""
		Insert the given data into the BST
		This function is first called by the user
		and will create a root node if the BST is empty.
		If BST is not empty, this function will recursively 
		call insert_ until the proper empty space is found.
		"""
		if self.root is None:
			self.root = BST.Node(data)
		else:
			self.insert_(data, self.root)

	def insert_(self, data, node):
		"""Looks for the proper location of the data that
		is to be stored.
		"""
		if data > node.data:

			# The data should go on the right.
			if node.data == data:
				return
			elif node.right is None:
				#If the right node is none, then will add 
				#the new node here.
				node.right = BST.Node(data)
			elif node.right == data:
				return
			else:
				#We will use recursion and call the function
				#again to continue looking.
				self.insert_(data, node.right)

		else:

			#the data should go on the left side.
			if node.data == data:
				return
			elif node.left is None:
				#If the left node is none, then will add 
				#the new node here.
				node.left = BST.Node(data)

			else:
				#We will use recursion and call the function
				#again to continue looking.
				self.insert_(data, node.left)


	def __iter__(self):
		""" Goes through, or traverses, the BST from the beginning.  
		"""
		yield from self.traverse_forwards_(self.root)
	
	def traverse_forwards_(self, node):
		"""The function called by __iter__ that will recursively
		travers through the BST.
		Uses the "yield" keyword, which acts similarly to "return"
		but does not stop the program. 
		"""
		if node is not None:
			#The left side must go first in order to get the 
			#smaller values first
			yield from self.traverse_forwards_(node.left)
			yield node.data
			yield from self.traverse_forwards_(node.right)


	def __contains__(self, data):
		""" This function makes it possible to use the
		 keyword "in" to determine if data is in the BST 
		 already. 
		"""
		return self.contains_(data, self.root)

	def contains_(self, data, node):
		"""Like insert_, this funciton is called by 
		another (__contains__) recurrsively to look
		through the BST	for a node.
		"""

		if data > node.data:
			
			#The data will be found on the right side
			if data == node.data:
				return True
			elif node.right is None:
				#there is an empty space so it is False
				return False
			else:
				# We will call the function again 
				return self.contains_(data, node.right)

		else:

			#The data will be found on the left side
			if data == node.data:
				return True
			elif node.left is None:
				#there is an empty space so it is False
				return False
			else:
				# We will call the function again 
				return self.contains_(data, node.left)

	def __reversed__(self):
		"""Traverses through the BST in reversed order.
		Recursively calls the travers_backwards_ function
		"""
		yield from self.traverse_backwards_(self.root)


	def traverse_backwards_(self, node):
		"""Traverses backwards through the BST. 
		This function works in the opposite direction as 
		traverse_forwards_ 
		"""
		if node is not None:
			#The right side must go first in order to get the 
			#larger values first
			yield from self.traverse_forwards_(node.right)
			yield node.data
			yield from self.traverse_forwards_(node.left)

	def return_height(self):
		"""Finds the height of the BST using the 
		function return_height_
		"""

		if self.root is None:
			return 0
		else:
			return self.return_height_(self.root)

	
	def return_height_(self, node, curr_height=None):
		"""The function recursively called by return_height
		Finds the total height by adding 1 (the root) to the 
		height of the right or left sub trees depending on 
		which one has the greater height.
		"""

		if node == self.root:
			height = 1
		else: height = curr_height
		
		if node.right == None and node.left == None:
			return height
		
		#If the left node is not none while the right is
		# we will continue down the left side and add 1 to height
		elif node.right == None and node.left != None: 
			return self.return_height_(node.left, height+1)
		
		#If the right node is not none while the left is
		# we will continue down the right side and add 1 to height
		elif node.right != None and node.left == None:
			return self.return_height_(node.right, height+1)
		
		# If both sides have values, we will continue down both
		#sides and the max fucntion will choose the one that is 
		#greater and return it
		else:
			return max(self.return_height_(node.right, height+1), self.return_height_(node.left, height+1))

	def empty(self):
		"""Determines if the BST is empty 
		"""
		# If root is None, the list is empty
		if self.root == None:
			return True
		
		return False

	