def removNb(n):   
	import math
	import time
	result = []
	begin = time.time()
	arr = range(n+1)[1:]
	_sum = sum(arr)
	min_value_possible = int(math.ceil(float(_sum) / arr[-1]))
	max_value_possible = ((_sum - arr[min_value_possible] - arr[min_value_possible + 1]) / min_value_possible)
	for i in range(min_value_possible, max_value_possible + 1):
		candidate = (_sum - i) / (i + 1)
		if (candidate * i + candidate + i) == _sum:
			result.extend([(i,candidate)])
	end = time.time()
	print (end - begin)
	return result

print removNb(26)