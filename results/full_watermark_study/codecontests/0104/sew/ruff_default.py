for i in range(int(input())):
    a, b, c = map(int, input().split())
    if (
        (0 == a % 2 and 0 == b % 2 and 0 == c % 2)
        or (0 != a % 2 and 0 != b % 2 and 0 != c % 2)
        or (0 == b % 2 and 0 != a % 2 and 0 != c % 2)
    ):
        print(0)
    elif (
        (0 == a % 2 and 0 == b % 2 and 0 != c % 2)
        or (0 != a % 2 and 0 == b % 2 and 0 == c % 2)
        or (0 != a % 2 and 0 != b % 2 and 0 == c % 2)
        or (0 == a % 2 and 0 != b % 2 and 0 != c % 2)
    ):
        print(1)
    elif 0 == a % 2 and 0 != b % 2 and 0 == c % 2:
        print(0)
