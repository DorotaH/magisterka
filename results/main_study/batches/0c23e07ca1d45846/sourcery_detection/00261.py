
def process( s ):
	res = s[:]
	for i in range( 1, len(s) ):
		if s[i] == 'G' and s[i - 1] == 'B':
			res[i], res[i - 1] = res[i - 1], res[i]
	return res

fl = input().split()
n = int( fl[0] )
t = int( fl[1] )
s = input().split()[0]
S = [s[i] for i in range(n)]
for _ in range(t):
	S = process( S )
ans = "".join(S[i] for i in range(n))
print( ans )