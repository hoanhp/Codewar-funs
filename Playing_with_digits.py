def dig_pow(n,p):
	str_n = str(n)
	total = sum((int(str_n[i]))**(p+i)for i in range(len(str_n)))
	print total
	if total%n == 0:
		return total/n
	else:
		return -1

print dig_pow(46288,3)