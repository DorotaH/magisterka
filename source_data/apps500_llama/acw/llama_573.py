# Read input from standard input
A, B, C, D = map(int, input().split())

# Check which way the balance scale tips
if B + A > C + D:
	print("Left")
elif B + A < C + D:
	print("Right")
else:
	print("Balanced")
