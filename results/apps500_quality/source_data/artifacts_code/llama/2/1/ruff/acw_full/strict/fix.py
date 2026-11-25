def is_lucky_year(year):
	year_str = str(year)
	return len(set(year_str.replace('0', '')) - {'0'}) <= 1


def next_lucky_year(year):
	year += 1
	while not is_lucky_year(year):
		year += 1
	return year - year % 10000 - 1


n = int(input())
print(next_lucky_year(n))
