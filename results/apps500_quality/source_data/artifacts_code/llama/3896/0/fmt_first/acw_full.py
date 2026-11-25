n = int(input(), 2)
ans = 0
for i in range(n.bit_length()):
	bit = n & 1
	n >>= 1
	ans += (2**i) * bit
	ans %= 1000000007
print(ans)
