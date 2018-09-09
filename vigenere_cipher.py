import string

class VigenereCipher(object):
    def __init__(self, key, chars_set):
        self.key = key
    	self.chars_set = chars_set
    	self.matrix = []
    	for i in range(0,len(self.chars_set)):
			self.matrix.append(self.chars_set[i:] + self.chars_set[:i])

    def encode(self, _str):
    	_str = _str.decode('utf-8')
    	full_key = self.key*(len(_str)/len(self.key)) + self.key[:(len(_str)%len(self.key))]
    	cipher = ""
    	for i in range(0,len(_str)):
    		if (_str[i] not in self.chars_set):
    			cipher += _str[i]
    		else: 
    			cipher += self.matrix[self.chars_set.index(_str[i])][self.chars_set.index(full_key[i])]
    	return cipher

    def decode(self, _str):
    	_str = _str.decode('utf-8')
    	full_key = self.key*(len(_str)/len(self.key)) + self.key[:len(_str)%(len(self.key))]
    	message = ""
    	for i in range(0,len(_str)):
    		if (_str[i] not in self.chars_set):
    			message += _str[i]
    		else:
	    		dis = (ord(_str[i]) - ord(full_key[i]))
	    		message += self.chars_set[dis]
    	return message

test = VigenereCipher('password', string.ascii_lowercase)
print test.encode('CODEWaRS')
print test.decode('RovWsoiv')