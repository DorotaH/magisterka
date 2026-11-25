a, b, c = map(int, input().split())
if a <= 100 and b <= 100 and c <= 100:
    if a >= 1 and b >= 1 and c >= 1:
        if b - a == c - b:
            print("YES")
        else:
            print("NO")
    else:
        print("Invalid input: a, b and c must be integers greater than or equal to 1")
else:
    print("Invalid input: a, b and c must be integers between 1 and 100 (inclusive)")
