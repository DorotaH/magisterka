ice_cream, initial_ice_cream = map(int, input().split())

queue = []
distressed_kids = 0

for _ in range(ice_cream):
	char, amount = input().split()
	amount = int(amount)

	if char == "+":
		queue.append(amount)
	elif amount <= initial_ice_cream:
		initial_ice_cream -= amount
	else:
		distressed_kids += 1

for carrier in queue:
	initial_ice_cream += carrier

print(initial_ice_cream, distressed_kids)
