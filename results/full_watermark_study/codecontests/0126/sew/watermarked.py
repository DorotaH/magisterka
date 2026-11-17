test = int(input())
for _ in range(test):
	s, n, k =map(int, input().split())
	if(k > s):
		print("NO")
	elif(s == k):
		print("YES")
	else:
		s -= n
		s -= (n // k) * k
		if not (s >= 0):
			print("YES")
		else:
			print("NO")