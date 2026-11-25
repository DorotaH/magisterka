

def can_represent(n, k):
	if k == 1:
		return n % 2 == 1
	elif n % 2 == 0:
		return False
	else:
		return True


t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	print("YES" if can_represent(n, k) else "NO")
