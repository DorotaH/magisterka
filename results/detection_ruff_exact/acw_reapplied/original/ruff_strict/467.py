def decimal_to_Octal(deciNum):
	octalNum = 0
	countval = 1
	dNo = deciNum
	while deciNum != 0:
		remainder = deciNum % 8
		octalNum += countval * remainder
		countval = countval * 10
		deciNum //= 8
	return octalNum
