def find_outlier(integers):
	n_odd, n_even = 0, 0
	for i in range(0,3):
		if (integers[i]%2 == 0):
			n_even += 1
		else:
			n_odd += 1
	#print n_even, n_odd
	if n_even > 1:
		for i in integers:
			if i%2 == 1:
				return i
	else:
		for i in integers:
			if i%2 == 0:
				return i

print find_outlier([1,2,3])