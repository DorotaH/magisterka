def calculate_flicks(n, sherlock_card, moriarty_card):
    # Count the frequency of each digit in both cards
    sherlock_count = [0] * 10
    moriarty_count = [0] * 10
    for digit in sherlock_card:
        sherlock_count[int(digit)] += 1
    for digit in moriarty_card:
        moriarty_count[int(digit)] += 1

    # Calculate the minimum possible number of flicks Moriarty will get
    min_flicks = 0
    for i in range(10):
        min_flicks = min_flicks + max(0, sherlock_count[i] - moriarty_count[i])

    # Calculate the maximum possible number of flicks Sherlock can get
    max_flicks = 0
    for i in range(10):
        max_flicks = max_flicks + max(0, moriarty_count[i] - sherlock_count[i])

    return (min_flicks, max_flicks)


# Read input
n = int(input().strip())
sherlock_card = input().strip()
moriarty_card = input().strip()

# Calculate and print the results
min_flicks, max_flicks = calculate_flicks(n, sherlock_card, moriarty_card)
print(min_flicks)
print(max_flicks)
