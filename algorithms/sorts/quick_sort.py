def quicksort(lst):
	_quicksort(lst,0,len(lst)-1)

def _quicksort(lst,start,end):
	if start < end:
		pivot,l,r= lst[start],start+1,end
		# selection of pivot value, left and right indexes 
		done= False

		while not done:
			while l<=r and pivot >= lst[l]: 
				l+=1 # increase left index while left values less than pivot
			while pivot <= lst[r] and l <=r:
				r-=1 # decrease right index while right vals less than pivot
			if r<l: # checks if indexes have crossed
				done= True  
			else:
				# if they don't cross, swap values of left and right indexex
				lst[l],lst[r]=lst[r],lst[l]

		lst[start],lst[r]= lst[r],lst[start]
		'''
	    if l and r cross pivot is found.
	    swap pivot with right value.
	    '''

		_quicksort(lst,start,r-1) # recursion left of pivot
		_quicksort(lst,r+1,end) # recursion right of pivot


