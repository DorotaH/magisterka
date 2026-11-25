def min_complexity():
	n = int(input())
	p = list(map(int, input().split()))
	p = [x for x in p if x != 0]

	even = [x for x in p if x % 2 == 0]
	odd = [x for x in p if x % 2 != 0]

	complexity = 0

	# Try to place the odd numbers in between the even numbers
	while odd and even:
		complexity += 1
		even.pop(0)
		odd.pop(0)

	# Add any remaining odd numbers to the end of the list
	even.extend(odd.pop() for _ in range(len(odd)))
	return complexity


print(min_complexity())
