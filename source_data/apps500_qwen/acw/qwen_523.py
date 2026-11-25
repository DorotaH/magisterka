N = int(input())
ones_place = N % 10
if ones_place in [2, 4, 5, 7, 9]:
	print("hon")
elif ones_place in [0, 1, 6, 8]:
	print("pon")
elif ones_place == 3:
	print("bon")
