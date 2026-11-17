for _ in range(int(input())):
	n = int(input())
	s = list(input().strip())
	temp2 = sorted(s)
	count = sum(s[i] != temp2[i] for i in range(n))
	print(count)
