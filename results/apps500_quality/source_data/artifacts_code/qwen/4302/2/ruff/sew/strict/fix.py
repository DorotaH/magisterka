import sys

input = sys.stdin.read
data = input().split()

A, B = int(data[0]), int(data[1])

# Calculate the maximum coins by pressing the buttons optimally
max_coins = max(A + (A - 1), B + (B - 1))
if  max_coins < A+B:
    max_coins=A+B

print(max_coins)
