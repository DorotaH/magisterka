import sys
input = sys.stdin.read
data = input().split()

S = data[0]

if S[0] != 'A':
	print('WA')
	exit()

if S.count('C') != 1:
	print('WA')
	exit()

if S[2] != 'C':
	print('WA')
	exit()

for i in range(4, len(S) - 1):
	if S[i].isupper():
		print('WA')
		exit()

print('AC')
