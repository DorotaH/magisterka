import math

n, s = map(int, input().split())
slices = []
happiness = []

for _ in range(n):
	s_i, a_i, b_i = map(int, input().split())
	slices.append(s_i)
	happiness.append([a_i, b_i])

# Calculate the number of pizzas needed for each type
pizzas_1 = math.ceil(sum(slices) / s)
pizzas_2 = math.ceil(sum(slices) / s)

# Calculate the happiness for each type
total_happiness_1 = sum(a * s for a, _ in happiness)
total_happiness_2 = sum(b * s for _, b in happiness)

# Calculate the happiness for each type when buying one pizza of each type
pizza1_happiness = sum(a * min(s, slices[i]) for i, (a, _) in enumerate(happiness))
pizza2_happiness = sum(min(s, slices[i]) * b for i, (_, b) in enumerate(happiness))

# Check which type gives more happiness when buying one pizza of each type
if pizza1_happiness > pizza2_happiness:
	max_happiness = pizza1_happiness + total_happiness_1
else:
	max_happiness = total_happiness_2 + pizza2_happiness

print(max_happiness)
