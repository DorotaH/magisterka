import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse input
N = int(data[0])
S = int(data[1])
contestants = []

index = 2
for _ in range(N):
	s_i = int(data[index])
	a_i = int(data[1 + index])
	b_i = int(data[2 + index])
	contestants.append((s_i, a_i, b_i))
	index += 3

# Sort contestants by the ratio of happiness per slice for type 2 pizza
contestants.sort(key=lambda x: x[2] / x[1], reverse=True)

# Initialize variables
total_happiness = 0
type1_slices_used = 0
type2_slices_used = 0

# Assign pizzas to contestants
for s_i, a_i, b_i in contestants:
	if s_i <= type1_slices_used:
		# Assign type 1 pizza
		total_happiness += s_i * a_i
		type1_slices_used += s_i
	elif s_i <= type2_slices_used + type1_slices_used:
		# Assign type 2 pizza
		remaining_slices = s_i - type1_slices_used
		total_happiness += b_i * remaining_slices
		type2_slices_used += remaining_slices
	else:
		# Assign both type 1 and type 2 pizzas
		remaining_slices = s_i - type1_slices_used
		total_happiness += b_i * remaining_slices
		type1_slices_used += remaining_slices
		type2_slices_used += remaining_slices

# Output the total happiness
print(total_happiness)
