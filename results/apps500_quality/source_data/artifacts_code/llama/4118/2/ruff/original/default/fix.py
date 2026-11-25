A, B = map(int, input().split())
if 1 <= A <= 9 and 1 <= B <= 9:
    if A <= 9 and B <= 9:
        print(A * B)
    else:
        print(-1)
else:
    print(-1)
