n = int(input())


def max_presents(n):
    if n == 1 or n == 2:
        return 1
    else:
        return n - 1


print(max_presents(n))
