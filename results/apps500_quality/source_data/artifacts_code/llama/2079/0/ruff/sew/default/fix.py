
n, w = int(input()), list(map(int, input().split()))
s=input()

rows=[(i, w[i]) for i in range(n)]
rows.sort(key=lambda x: x[1])

ans, empty = [], []
occupied, occupied_capacity = {}, 0
for i in range(n * 2):
    if not s[i] == '0':
        if occupied_capacity > 0:
            index = min(occupied.keys())
            ans.append(index + 1)
            occupied[index] += 1
            occupied_capacity -= 1
        else:
            ans.append(rows[-1][0] + 1)
            occupied[rows[-1][0]] = 1
            occupied_capacity += 1
            rows.pop(-1)
    else:
        ans.append(rows[0][0] + 1)
        empty.append(rows[0])
        occupied_capacity += 1
        occupied[rows[0][0]] = 1
        rows.pop(0)
        rows.sort(key=lambda x: x[1])

print(*ans)