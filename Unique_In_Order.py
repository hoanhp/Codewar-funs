def unique_in_order(iterable):
	result = []
	tmp = ''
	for char in (iterable):
		if (tmp == char):
			continue
		else:
			result.append(char)
			tmp = char
	return result


print unique_in_order(['A','A','B','B','C','C','D','C','A','A'])