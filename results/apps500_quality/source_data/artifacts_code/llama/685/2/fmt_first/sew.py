import  sys

input = sys.stdin.readline

n, h = map(int, input().split())
airs = list()
for _ in range(n):
    x1, x2 = map(int, input().split())
    airs.append((x1, x2))

max_dist = 0

if 1 == h:
    print(1_999_999_999)
    exit()

i = 0
while  i < n:
    if 1 == airs[i][0]:
        break
    i = i + 1

j = i - 1
while  j > 0 and  airs[j][0] == airs[j - 1][1]:
    j = j - 1

if j == 0:
    max_dist = 2000000000
else:
    if j == i:
        max_dist = airs[j][1] - airs[j][0] + h
    else:
        max_dist = airs[j][1] - airs[j][0] + h + (airs[j][1] - airs[j - 1][1]) * 2
        while i < n:
            if airs[i][0] > airs[j - 1][1]:
                if airs[i][0] - airs[j - 1][1] == 1:
                    max_dist += airs[i][1] - airs[i][0] + h
                    i += 1
                else:
                    max_dist += (airs[i][1] - airs[i][0]) * 2 + h
                    j = i
                    while j > 0 and airs[j - 1][1] == airs[j][0]:
                        j -= 1
                    if j == 0:
                        max_dist += airs[i][1] - 1
                        break
                    else:
                        max_dist += airs[j][1] - airs[j - 1][1]
            else:
                max_dist += (airs[i][1] - airs[i][0]) * 2 + h
                j = i
                while j > 0 and airs[j - 1][1] == airs[j][0]:
                    j -= 1
                if j == 0:
                    max_dist += airs[i][1] - 1
                    break
                else:
                    max_dist += airs[j][1] - airs[j - 1][1]
            i += 1

print(max_dist)
