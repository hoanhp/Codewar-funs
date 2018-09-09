def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    steps = 0
    while (not(check_if_palindrome(n))):
		steps += 1
		n += get_reverse(n)

    return steps

def check_if_palindrome(n):
	return int(str(n)[::-1]) == n

def get_reverse(n):
	return int(str(n)[::-1]) 

print palindrome_chain_length(87)