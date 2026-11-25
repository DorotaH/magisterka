

def get_min_distance():
	w, a, b = map(int, input().split())

	min_distance = min(a, b)
	max_distance = a + w - b

	print(min(min_distance, max_distance))


get_min_distance()
