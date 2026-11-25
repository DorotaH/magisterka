n = int(input())
w = list(map(int, input().split()))
order = input()

rows = [0] * n
result = [0] * (2 * n)
introvert_empty = sorted([(w[i], i) for i in range(n)])
extrovert_filled = sorted([(w[i], i) for i in range(n)], reverse=True)

introvert_index = 0
extrovert_index = 0

for i in range(2 * n):
    if order[i] == '0':  # introvert
        while introvert_index < n and rows[introvert_empty[introvert_index][1]] != 0:
            introvert_index += 1
        if introvert_index < n:
            row = introvert_empty[introvert_index][1]
            rows[row] = 1
            result[i] = row + 1
            introvert_index += 1
    else:  # extrovert
        while extrovert_index < n and rows[extrovert_filled[extrovert_index][1]] != 1:
            extrovert_index += 1
        if extrovert_index < n:
            row = extrovert_filled[extrovert_index][1]
            rows[row] = 0
            result[i] = row + 1
            extrovert_index += 1

print(' '.join(map(str, result)))
