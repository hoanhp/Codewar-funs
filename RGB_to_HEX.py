def rgb(r, g, b):
	result = ''
	for i in (r,g,b):
		if i in range(0,256):
			result += format(i,"02X")
		else:
			if abs(i-0) > abs(i-255):
				result += "FF"
			else:
				result += "00"
	return result

print rgb(255, 255, 255) # returns FFFFFF
print rgb(255, 255, 300) # returns FFFFFF
print rgb(0,0,0) # returns 000000
print rgb(148, 0, 211) # returns 9400D3