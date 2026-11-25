n = int(input(), 2)
ans = 0
for i in range(n.bit_length()):
    bit = n & 1
    n >>= 1
    ans += bit * (2**i)
    ans %= 1000000007
print(ans)
