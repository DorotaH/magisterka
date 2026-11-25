n = int(input())
a = list(map(int, input().split()))

boxes = sorted([(a[i], i) for i in range(n)])

visible = 0
i = 0
while i < n:
    if i == n - 1 or boxes[i][0] < boxes[i + 1][0]:
        visible += 1
    else:
        j = i + 1
        while j < n and boxes[i][0] >= boxes[j][0]:
            if boxes[j][1] != boxes[i][1]:
                boxes[j] = (-1, boxes[j][1])
            j += 1
        visible += 1
        i = j
    i += 1

print(visible)
