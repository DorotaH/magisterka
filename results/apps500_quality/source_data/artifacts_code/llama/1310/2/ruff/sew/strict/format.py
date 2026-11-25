n = int(input())
a = list(map(int, input().split()))

max_xor = [0] * (n + 1)
max_xor[0] = 0

for i in range(1, 1 + n):
    max_xor[i] = max_xor[i - 1]
    for j in range(0, i):
        max_xor[i] = max(max_xor[i], max_xor[j] ^ a[i - 1])

print(max_xor[-1])
