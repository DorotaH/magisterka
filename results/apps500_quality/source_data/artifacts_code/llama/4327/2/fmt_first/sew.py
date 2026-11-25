A, P = map(int, input().split())
pieces_from_one = 3
pies_from_one = 1
pies_from_pieces = P // 2

max_pies = pies_from_pieces
for _ in range(A):
    max_pies += pies_from_one
print(max_pies)