def shell_sort(lst):
	gap= len(lst)//2 # gap between potentially swapped items
	while gap >0:
		for i in range(gap,len(lst)):
			ind= i # starting position
			val=lst[i] #value at starting position
			while ind >=gap and lst[ind-gap]> val: # loop to -->
				lst[ind]=lst[ind-gap] # allow swaps of values
				ind-=gap
			lst[ind]= val
		gap//=2 # decrease gap as sublists become sorted