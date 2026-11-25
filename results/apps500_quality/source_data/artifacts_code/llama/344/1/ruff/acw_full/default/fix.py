def is_Berlanese(s):
	vowels = 'aeiou'
	return next(
		(
			'NO'
			for i in range(len(s) - 1)
			if s[i] not in vowels and s[i + 1] not in vowels and s[i] != 'n'
		),
		'YES',
	)


s = input()
print(is_Berlanese(s))
