class Node:
	def __init__(self,data):# node class to hold info
		self.data=data# and pointer to next node
		self.next= None
	def __str__(self):
		return str(self.data)

class LinkedList:
	def __init__(self):
		self.head= None
	def __str__(self): #string/ print out representation of linked list
		temp = self.head
		result='head-->'
		if self.head is None:
			return str(self.head)
		else:
			while temp.next:
				result+= str(temp.data) + "-->"
				temp=temp.next
			return result + str(temp.data)

	def add(self,val):
		if self.head is None: # if head is none, assign head to new node
			self.head = Node(val)
		else:
			temp = Node(val) # create new node
			temp.next= self.head # pointer of new node to head node
			self.head= temp # reassign head to new node 

	def search(self,val):# return true or false if val is in linked list
		curr= self.head
		found = False
		while curr and not found:#traversing through linked list
			if curr.data== val:
				found=True
			else:
				curr=curr.next
		return found


	def size(self):
		count=0
		temp= self.head
		while temp: # traverse through list and add to count until
			count+=1 # there are no more nodes
			temp=temp.next
		return count # return total count

	def remove(self,val):
		curr= self.head
		prev= None
		found= False
		while not found: # traverse through list until node is found
			if curr.data == val:# maintain current and previous node while traversing
				found = True
			else:
				prev= curr
				curr=curr.next
		if prev== None: # if you are removing head node
			self.head= curr.next
		else: # removing nodes throughout the list
			prev.next=curr.next
			#reassign neccessary pointers



