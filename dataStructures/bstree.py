class BSTNode:
	def __init__(self,value): # initialize with data and left and right equal to none
		self.value= value
		self.left= None
		self.right= None

	def __str__(self):
		return str(self.value) 

	def size(self):
		left = self.left.size() if self.left else 0 # recursively find size of left subtree
		right=  self.right.size() if self.right else 0 # recursively find size of right subtree
		return 1 + left+ right # add together along with root node
	
	def height(self):
		if self.left is None and self.right is None:
			return 0 # only 1 node has height of zero
		return 1 +max(self.left.height() if self.left else 0,
					self.right.height() if self.right else 0)
	
	def search(self,val): #compare value against node values, return True if value in tree
		if val == self.value:
			return True
		elif val < self.value:
			if self.left: # if left node exists, recurse on left node
				return self.left.search(val)
			else:
				return False
		else:
			if self.right: # if right node exists, recurse on left node
				return self.left.search(val)
			else:
				return False
	
	def insert(self,val):
		if self.value is None:
			self.value = val
		else:
			if val < self.value:
				if self.left: # if left node exists, recurse on left node
					self.left.insert(val)
				else: # if left node does not exist, create new node
					self.left= BSTNode(val) 
			else:
				if self.right: # if right node exists, recurse on left node
					self.right.insert(val)
				else: # if right node does not exist, create new node
					self.right= BSTNode(val)


	def remove(self,val):
		pass # have not created yet

	def minVal(self):
		curr= self # pointer to root node
		while curr.left: #traverse left nodes until None
			curr=curr.left
		return curr.value #return last node encountered

	def maxVal(self):
		curr=self # pointer to root node
		while curr.right: #traverse right nodes until None
			curr=curr.right
		return curr.value #return last node encountered


def delete(root):
	if root: # can't figure out how to delete root node
		delete(root.left)
		delete(root.right)
		root.left=None
		root.right=None

def preOrder(root):
	if root:
		print root.value #print data 
		preOrder(root.left)# traverse left recursively
		preOrder(root.right)# traverse right recursively

def inOrder(root):
	if root:
		inOrder(root.left)# traverse left recursively
		print root.value #print data
		inOrder(root.right)# traverse right recursively

def postOrder(root):
	if root:
		postOrder(root.left)# traverse left recursively
		postOrder(root.right)# traverse right recursively
		print root.value #print data

def levelOrder(root):
	q=[root] # list with node object

	while q != []:
		root= q.pop(0) # return first element of list
		print root,
		if root.left: # if left node exists add it to list
			q.append(root.left)
		if root.right: # if right node exists add it to list
			q.append(root.right)



