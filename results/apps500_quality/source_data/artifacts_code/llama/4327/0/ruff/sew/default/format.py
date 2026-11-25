A, P = map(int, input().split())
cuts = A + P

max_pies = 0
while cuts >= 2:
    pies = (cuts // 3) * 2
    max_pies += pies
    cuts = cuts - 3 * pies

print(max_pies)
