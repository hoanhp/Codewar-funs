def validate_pin(pin):
	digits = ['1','2','3','4','5','6','7','8','9','0']
	if ((len(pin) == 4) | (len(pin) == 6)):
		for num in pin:
			if (num) not in digits:
				return False
		return True
	else:
		return False
print validate_pin("12345")
print validate_pin("69\d")