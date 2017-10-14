class minHeap:
	def __init__(self):
		self.items= [0]
		self.size= 0
	def getMin(self):
		return self.items[1]
	def percUp(self,i):
		while i//2 > 0:
			if self.items[i]<self.items[i//2]:
				self.items[i],self.items[i//2]=self.items[i//2],self.items[i]
			i//=2

	def percDown(self,i):
	
		while 2*i<= self.size:
			minchild= self.minChild(i)
			
			if self.items[i]> self.items[minchild]:
				self.items[i],self.items[minchild]=self.items[minchild],self.items[i]
			i=minchild


	def minChild(self,i):
		r= 2*i+1
		l=2*i
		if r > self.size:
			return l
		else:
			if self.items[l]< self.items[r]:
				return l
			else:
				return r

	def insert(self,k):
		self.items.append(k)
		self.size+=1
		self.percUp(self.size)

	def delMin(self):
		val=self.items[1]
		self.items[1]=self.items[self.size]
		self.items.pop()
		self.size-=1
		self.percDown(1)
		return val

	def buildHeap(self,lst):
		i = len(lst) // 2
		self.size = len(lst)
		self.items = [0] + lst[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1



mini= minHeap()
mini.buildHeap([9,6,5,2,3])
'''
mini.insert(5)

mini.insert(7)

mini.insert(3)
mini.insert(14)

mini.insert(2)
'''
'''
mini.insert(19)
mini.insert(121)
mini.insert(13)
mini.insert(27)

mini.insert(18)
mini.insert(1)
'''
#print mini.delMin()

print mini.items