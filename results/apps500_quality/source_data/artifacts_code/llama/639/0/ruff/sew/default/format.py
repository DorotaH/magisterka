n, x = map(int, input().split())
arr = list(map(int, input().split()))
mex = 0
current = operations = 0

while mex < x:
    if x > current and current not in arr:
        mex = mex + 1
    elif current not in arr:
        operations += 1
        arr.remove(current)
        mex += 1
    current += 1

print(operations)
