def merge(left, right):
	c = []
    #print(f"Left: {left} and Right: {right}") 
	i = j = 0
	# import pudb; pu.db
	while i < len(left) and j < len(right):
		if left[i] < right [j]:
			c.append(left[i])
			i += 1	
		# left.pop(i)
		else:			
			c.append(right[j])
			j += 1
	for k in range(i, len(left)):
		c.append(left[k])

	for r in range(j,len(right)):
		c.append(right[r])
			
	return c
			

def mergesort(l):
    # FIRST DIVIDE THE LISTS.
	
	if len(l) <= 1:
		return l

	mid = len(l)//2
	left_arr = mergesort(l[0:mid])
	right_arr = mergesort(l[mid:len(l)])
	return merge(left_arr, right_arr)	

if __name__ == '__main__':
    # print([4,2,6])
	print("Sorted_List", mergesort([4,2,5,1])) 	
