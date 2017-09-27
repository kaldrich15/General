class Stack:
	def __init__(self):
		self.items=[]
	def size(self): # how many items are on stack
		return len(self.items)
	def isEmpty(self): # check if any items are on stack
		return self.items == []
	def peek(self): # shows element at top of stack
		return self.items[len(self.items)-1]
	def push(self,item):# inserts element onto stack
		self.items.append(item)
	def pop(self): #removes and returns element off top of stack
		return self.items.pop()



