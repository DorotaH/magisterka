import sys

input = sys.stdin.readline

n, k = map(int, input().split())
beauties = list(map(int, input().split()))
colors = list(input().rstrip())

# Initialize dictionaries to store the maximum beauty of each color
max_beauty = {"W": 0, "O": 0, "R": 0}

# Initialize dictionaries to store the total beauty of each color
total_beauty = {"W": 0, "O": 0, "R": 0}

# Initialize set to store the colors of the roses
colors_set = set(colors)

# Calculate the maximum beauty of each color
for i in range(n):
	total_beauty[colors[i]] += beauties[i]
	max_beauty[colors[i]] = max(max_beauty[colors[i]], beauties[i])

# Calculate the total beauty of the roses of each color
total_beauty["W"] += beauties[colors.index("W")]
total_beauty["O"] += beauties[colors.index("O")]
total_beauty["R"] += beauties[colors.index("R")]

# Initialize the maximum beauty of the bouquet
max_bouquet = 0

# If the number of roses of each color is equal to k
if total_beauty["W"] == k or total_beauty["O"] == k or total_beauty["R"] == k:
	print(-1)
else:
	# Calculate the maximum beauty of the bouquet
	if k % 2 == 0 and (
		total_beauty["W"] == k // 2
		or total_beauty["O"] == k // 2
		or total_beauty["R"] == k // 2
	):
		max_bouquet = max(total_beauty["W"], total_beauty["O"], total_beauty["R"])
	else:
		max_bouquet = max(
			max_beauty["W"] + total_beauty["O"] + total_beauty["R"],
			max_beauty["O"] + total_beauty["W"] + total_beauty["R"],
			max_beauty["R"] + total_beauty["W"] + total_beauty["O"],
			max_beauty["W"] + max_beauty["O"],
			max_beauty["O"] + max_beauty["R"],
			max_beauty["W"] + max_beauty["R"],
		)

	# If the number of roses of each color is not equal to k and the total number of roses of two colors is equal to k
	if (
		total_beauty["O"] + total_beauty["W"] == k
		or total_beauty["R"] + total_beauty["O"] == k
		or total_beauty["R"] + total_beauty["W"] == k
	):
		max_bouquet = max(
			max_bouquet,
			max_beauty["W"] + total_beauty["O"],
			max_beauty["O"] + total_beauty["R"],
			max_beauty["R"] + total_beauty["W"],
		)
	# If the total number of roses of three colors is equal to k
	if total_beauty["O"] + total_beauty["W"] + total_beauty["R"] == k:
		max_bouquet = max(
			max_bouquet,
			max_beauty["W"] + max_beauty["O"] + total_beauty["R"],
			max_beauty["O"] + max_beauty["R"] + total_beauty["W"],
			max_beauty["W"] + max_beauty["R"] + total_beauty["O"],
		)

	print(max_bouquet)
