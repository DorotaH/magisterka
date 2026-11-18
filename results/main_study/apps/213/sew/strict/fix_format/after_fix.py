def floo(num, k):
	return  1 + (num - 1) // k


def main():
	n, m=map(int, input().split())
	low = 1
	high = 10**9

	if  (m == 0):
		if not (n == 1):
			print(-1)
		else:
			print(1)
		return

	for  i in  range(0, m):
		k, f=map(int, input().split())
		low=max(low, (f + k-1)//f)
		if  (f > 1):
			high = min(high, (k - 1) // (f - 1))
	if (floo(n, low) == floo(n, high)):
		print(floo(n, low))
	else:
		print(-1)



main()
