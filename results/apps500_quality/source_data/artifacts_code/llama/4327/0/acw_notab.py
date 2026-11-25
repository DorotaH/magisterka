A, P = map(int, input().split())
cuts = P + A

max_pies = 0
while 2 <= cuts:
    pies = 2 * (cuts // 3)
    max_pies += pies
    cuts = cuts - (3 * pies)

print(max_pies)
