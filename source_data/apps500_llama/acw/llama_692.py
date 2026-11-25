import sys
input = sys.stdin.readline

for _ in range(int(input())):
	r, b, k = map(int, input().split())

	if r == b:
		print("REBEL")
	else:
		lcm = (r * b) // math.gcd(r, b)
		if k >= lcm:
			print("REBEL")
		else:
			print("OBEY")
