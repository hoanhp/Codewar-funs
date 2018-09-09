def Tribonacci(signature, n):
	result = []
	if n == 0:
		return result
	if n == 1:
		result.append(signature[0])
		return result
	if n == 2:
		result = signature[:2]
		return result
	if n == 3:
		result = signature
		return result
	elif (n > 3):
		a = signature[0]
		b = signature[1]
		c = signature[2]
		result.extend([a,b,c])
		for i in range(3,n):
			tmp = a + b +c 
			result.append(tmp)
			a = b
			b = c
			c = tmp
	return (result)

print Tribonacci([0.5,0.5,0.5], 30)