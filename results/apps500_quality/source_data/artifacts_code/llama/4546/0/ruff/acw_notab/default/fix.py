a, b, c = map(int, input().split())
if a <= 100 and 100 >= b and 100 >= c:
    if a >= 1 and 1 <= b and 1 <= c:
        if b - a == c - b:
            print('YES')
        else:
            print('NO')
    else:
        print('Invalid input: a, b and c must be integers greater than or equal to 1')
else:
    print('Invalid input: a, b and c must be integers between 1 and 100 (inclusive)')
