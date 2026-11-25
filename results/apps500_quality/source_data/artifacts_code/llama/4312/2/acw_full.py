# Read input from standard input
A, B, C, D = map(int, input().split())

# Initialize health of monsters
health_Takahashi = A
health_Aoki = C

# Simulate the battle
for _ in range(1, 1000):
	if 0 >= health_Takahashi:
		print("No")
		break
	if 0 >= health_Aoki:
		print("Yes")
		break

	health_Takahashi -= B
	health_Aoki -= D

	if (0 >= health_Takahashi and 0 < health_Aoki) or (0 >= health_Aoki and 0 < health_Takahashi):
		continue

	health_Takahashi -= C
	health_Aoki -= B
