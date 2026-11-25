def is_lucky(year):
	"""Check if a year is lucky."""
	return all(digit in ['0', '1', '4'] for digit in str(year))


def next_lucky_year(year):
	"""Find the next lucky year."""
	year += 1
	while not is_lucky(year):
		year += 1
	return year


current_year = int(input())
next_year = next_lucky_year(current_year)
print(next_year - current_year)
