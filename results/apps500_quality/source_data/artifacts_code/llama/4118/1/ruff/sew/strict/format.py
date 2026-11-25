A, B = map(int, input().split())
result = B * A
if not (1 <= A <= 9 and 1 <= B <= 9):
    print(-1)
else:
    print(result)
