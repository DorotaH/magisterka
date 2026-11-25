a, b, c = map(int, input().split())
if not (a <= 100 and b <= 100 and c <= 100):
    print('Invalid input: a, b and c must be integers between 1 and 100 (inclusive)')
else:
    if a >= 1 and b >= 1 and c >= 1:
        if b - a == c - b:
            print('YES')
        else:
            print('NO')
    else:
        print('Invalid input: a, b and c must be integers greater than or equal to 1')