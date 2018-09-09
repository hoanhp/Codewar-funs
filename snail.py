array = [[1,2,3,1,2,2],
         [4,5,6,4,3,4],
         [7,8,9,7,6,2],
         [7,8,9,7,8,6],
         [4,5,6,4,3,7],
         [1,2,3,1,2,2]]

def snail(array):
	if array == [[]]:
		return []
	final = []
	while (array.count([]) != len(array)):
		first_part = []
		rev_second_part = []
		size = len(array)
		first_part.extend(array[0])
		if len(array) > 1:
			for i in range(1,size-1):
				rev_second_part.append(array[i][0])
				first_part.append(array[i][-1])
				del array[i][0]
				del array[i][-1]

			first_part.extend(array[-1][::-1])
			del array[0]
			del array[-1]
			final.extend(first_part) 
			final.extend(rev_second_part[::-1])
		else:
			final.append(array[0][0])
			del (array[0][0])
	return final

print snail(array)