import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])

# Calculate the maximum coins by pressing the buttons optimally
max_coins = max((A - 1) + A, B + (B - 1))
if max_coins < B + A:
	max_coins = B + A

print(max_coins)
