A, B = map(int, input().split())
result = A * B
if 1 <= A <= 9 and 1 <= B <= 9:
    print(result)
else:
    print(-1)
