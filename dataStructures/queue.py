class Queue:
	def __init__(self):
		self.items=[]
	def isEmpty(self): # check if items exist on the queue
		return self.item==[]
	def enqueue(self,item): # push item onto the end ofqueue 
		self.items.append(item)
	def dequeue(self): # remove item from of queue and return 
		return self.items.pop(0)
	def size(self): # number of elements on queue
		return len(self.items)