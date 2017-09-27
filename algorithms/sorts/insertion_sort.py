def insertion_sort(lst):
	for i in range(1,len(lst)):
		pos= i #starting position
		val= lst[i] #value at starting position
		while pos >0 and lst[pos-1]>val: # loop that places value
			lst[pos]=lst[pos-1]		# correctly in sorted array portion
			pos-=1
		lst[pos]= val