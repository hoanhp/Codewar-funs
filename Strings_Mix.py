def mix(s1, s2):

	import collections
	result = ''
	list_result = []
	all_chars = [chr(i) for i in range(97,123)]
	s1_dict = collections.Counter(s1.replace(' ', ''))
	s2_dict = collections.Counter(s2.replace(' ', ''))
	
	for char in all_chars:
		if not ((s1_dict[char] == 0) and (s2_dict[char] == 0)):
			tmp = [char, s1_dict[char], s2_dict[char], True]
			list_result.append(tmp)
	
	for i in range(max(len(s1_dict),len(s2_dict)),1,-1):
		tmp_of_round_equal = []
		tmp_of_round_1 = []
		tmp_of_round_2 = []
		for count, j in enumerate(list_result):
			if j[1] == j[2] and j[3] == True:
				if j[1] == i:
					tmp_of_round_equal.append("=:%s/" % (i*j[0]))
					j[3] = False
			else:
				if j[1] == i and j[3] == True:
					tmp_of_round_1.append("1:%s/" % (i*j[0]))
					j[3] = False
				if j[2] == i and j[3] == True:
					tmp_of_round_2.append("2:%s/" % (i*j[0]))
					j[3] = False
		result += ''.join(tmp_of_round_1)
		result += ''.join(tmp_of_round_2)
		result += ''.join(tmp_of_round_equal)
	return result[0:len(result)-1]

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
print mix(s1, s2)

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
print mix(s1, s2)

print mix("Are they here", "yes, they are here")
print mix("looping is fun but dangerous", "less dangerous than coding")





