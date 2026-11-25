

def can_build_garland(r, g, b):
	return "Yes" if r % 2 == g % 2 or r % 2 == b % 2 or g % 2 == b % 2 else "No"


t = int(input())

for _ in range(t):
	r, g, b = map(int, input().split())
	print(can_build_garland(r, g, b))
