A, P = map(int, input().split())
max_pies = 0
for i in range(A + 1):
    if (A - i) * 3 >= P:
        pies_from_apples = (A - i) // 3
        pies_from_pieces = P // 2
        max_pies = max(max_pies, pies_from_apples + pies_from_pieces)
print(max_pies)
