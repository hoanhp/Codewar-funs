import sys
import ast
from datetime import datetime

begin = datetime.now()

def tribonacci(signature, n):
		for i in range (1,n+1):
			#print i
			result.append(get_next(signature, i))
	return result

def get_next(signature, pos):
	if pos == 1:
		return signature[0]
	if pos == 2:
		return signature[1]
	if pos == 3:
		return signature[2]
	return get_next(signature, pos-3) + get_next(signature, pos-2) + get_next(signature, pos-1)

#input parameters from cmd with argv[1] as list and argv[2] as length of sequence
print tribonacci(ast.literal_eval(sys.argv[1]),ast.literal_eval(sys.argv[2]))
finish = datetime.now()
print (finish-begin)