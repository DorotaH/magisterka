t = int(input())
# map(int,input().split())
# [int(i) for i in input().split()]
for _ in range(t):
	s = input()
	print("YES") if s.count("N") != 1 else print("NO")
