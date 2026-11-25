def calculate_flicks(n, sherlock_card, moriarty_card):
	# Count the frequency of each digit in both cards
	sherlock_count = [0] * 10
	moriarty_count = [0] * 10
	for digit in sherlock_card:
		sherlock_count[int(digit)] += 1
	for digit in moriarty_card:
		moriarty_count[int(digit)] += 1

	min_flicks = sum(
		max(0, sherlock_count[i] - moriarty_count[i]) for i in range(10)
	)
	max_flicks = sum(
		max(0, moriarty_count[i] - sherlock_count[i]) for i in range(10)
	)
	return min_flicks, max_flicks


# Read input
n = int(input().strip())
sherlock_card = input().strip()
moriarty_card = input().strip()

# Calculate and print the results
min_flicks, max_flicks = calculate_flicks(n, sherlock_card, moriarty_card)
print(min_flicks)
print(max_flicks)
