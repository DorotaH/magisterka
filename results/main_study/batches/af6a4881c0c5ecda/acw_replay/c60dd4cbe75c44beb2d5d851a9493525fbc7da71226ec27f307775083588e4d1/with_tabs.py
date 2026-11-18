class Solution:
	def romanToInt(self, s: str) -> int:
		letter_dict = {
			"I": 1,
			"V": 5,
			"X": 10,
			"L": 50,
			"C": 100,
			"D": 500,
			"M": 1000,
			"IV": 4,
			"IX": 9,
			"XL": 40,
			"XC": 90,
			"CD": 400,
			"CM": 900,
		}
		sum = 0
		values = []
		start = 0
		while start < len(s):
			second = start + 1
			letter1 = s[start]
			if len(s) > second:
				letter2 = s[second]
				special_case = letter2 + letter1
				if special_case in list(letter_dict.keys()):
					values.append(letter_dict[special_case])
					start += 2
				else:
					values.append(letter_dict[letter1])
					start += 1
			else:
				values.append(letter_dict[letter1])
				start += 1
		for value in values:
			sum += value
		return sum
