def merge_sort(lst):
	if len(lst)>1: #split lst into left and right sublists -->
		mid=len(lst)//2 # until all lists are of length 1
		left=lst[:mid]
		right=lst[mid:]
		merge_sort(left) # recursion
		merge_sort(right)

		k,l,r=0,0,0
		
		'''
		merge all individual list into orginal list
		based on value
		'''
		while l < len(left) and r < len(right):
			if left[l]<= right[r]:
				lst[k]=left[l]
				l+=1
			else:
				lst[k]=right[r]
				r+=1
			k+=1
		while l <len(left):
			lst[k]=left[l]
			l+=1
			k+=1
		while r < len(right):
			lst[k]=right[r]
			r+=1
			k+=1