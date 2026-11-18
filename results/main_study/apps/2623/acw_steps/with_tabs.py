import sys
readline = sys.stdin.readline

T = int(readline())
Ans = T * [None]
for qu in range(T):
	N, K = map(int, readline().split())
	S = list(map(lambda x: ord(x) - 97, readline().strip()))
	S.sort()
	if len(set(S[:K])) != 1:
		Ans[qu] = chr(S[K - 1] + 97)
		continue
	L = len(set(S[K:]))
	res = [S[0]] + (-((K - N) // K)) * [S[K]] if L == 1 else S[K:] + [S[0]]
	Ans[qu] = ''.join(map(lambda x: chr(97 + x), res))

print('\n'.join(map(str, Ans)))
