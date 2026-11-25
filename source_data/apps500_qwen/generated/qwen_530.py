import sys
input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])

# Press the larger button twice
max_coins = A + (A - 1)

# Press both buttons once
max_coins = max(max_coins, A + B)

# Press the smaller button twice
max_coins = max(max_coins, B + (B - 1))

print(max_coins)
