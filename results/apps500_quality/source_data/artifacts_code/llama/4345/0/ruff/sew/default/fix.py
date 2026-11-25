n = int(input())
arr = list(map(int, input().split()))

left = []
right = []
up = True
res = [0]*n

for i in range(n):
    if not up:
        if arr[i] > arr[-1]:
            right.append(arr[i])
        elif arr[i] < arr[-1]:
            up = True
            left.append(arr[i])
        else:
            right.append(arr[i])
    else:
        if arr[i] < arr[0]:
            left.append(arr[i])
        elif arr[i] > arr[0]:
            up = False
            right.append(arr[i])
        else:
            left.append(arr[i])

if left == sorted(left) and right == sorted(right, reverse=True):
    print("YES")
    print(' '.join(map(str, res)))
    for i in range(n):
        if arr[i] == left[-1]:
            res[i] = 0
        elif arr[i] == right[0]:
            res[i] = 1
    print(' '.join(map(str, res)))
else:
    print("NO")