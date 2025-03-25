from generate_test_data import generate_test_data

def jimmysort(arr):
	#first element becomes pivot, item goes to left or right
	#and recursively calls 

	#empty list base case
	if not arr:
		return []
	
	#get pivot randomly from front. could be improved
	#with a median of medians algo
	pivot = arr.pop(0)

	#initialize lefts (less than pivot)
	#and rights (greater than pivot)
	lefts = []
	rights = []

	#pass over list once and sort elements into left or right
	for i in arr:
		if i <= pivot:
			lefts.append(i)
		else:
			rights.append(i)

	#recursively call on the unsorted wing lists
	return jimmysort(lefts) + [pivot] + jimmysort(rights)


#run it to demonstrate on a size of 20 random numbers
a = generate_test_data(1000)
a2 = a.copy()
sorted_a = jimmysort(a)

#prove it is non-decreasing
if sorted_a == sorted(a2):
	print("Test passed, Jimmysort is good :)")
else:
	print("Test failed. Jimmysort is no good :(")

		