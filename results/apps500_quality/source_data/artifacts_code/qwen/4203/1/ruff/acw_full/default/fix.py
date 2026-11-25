import sys

input = sys.stdin.read
data = input().split()

S = data[0]

if S[0] == 'A' and S[2] == 'C' and S[1].islower() and S[3].islower() and all(c.islower() for c in S[4:-1]) and S[-1].islower():
	print('AC')
else:
	print('WA')
