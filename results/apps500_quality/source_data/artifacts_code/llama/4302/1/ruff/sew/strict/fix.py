a, b = map(int, input().split())
max_coins = float('-inf')

for A in range(a, 0, -1):
    for  B in  range(b, 0, -1):
        coins=A+B+max(0, A+B-max(A, B)-1)
        max_coins=max(max_coins, coins)

print(max_coins)
