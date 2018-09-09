def title_case(title, minor_words=''):
	if title == '':
		return ''
	else:
		title = title.lower()
		title_list = title.split()
		minor_words = minor_words.lower()
		minor_list = minor_words.split()
		title_list[0] = title_list[0][0].upper() + title_list[0][1:]
		for i in range(1,len(title_list)):
			if title_list[i] in minor_list:
				continue
			else:
				title_list[i] = title_list[i][0].upper() + title_list[i][1:]
		return ' '.join(title_list)

print title_case('')
print title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
print title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
print title_case('the quick brown fox') # should return: 'The Quick Brown Fox'