A, B, C = map(int, input().split())

# Check if C is already congruent to 0 modulo B
if C != 0 and A % B == C or C == 0:
	print("YES")
else:
	print("NO")
