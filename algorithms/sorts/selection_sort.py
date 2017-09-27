def selection_sort(lst):
	for i in range(len(lst)-1):
		mini= i # position of min value
		for j in range(i+1,len(lst)): # loop to compare min --> 
			if lst[j]< lst[mini]:	# value to rest of list
				mini=j # assign a new min
		lst[mini],lst[i] = lst[i],lst[mini] #exchange min with -->
		# first position of unsorted part
