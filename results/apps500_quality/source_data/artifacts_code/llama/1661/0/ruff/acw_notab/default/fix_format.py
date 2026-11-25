def game_shop(n, c, a):
    count = 0
    ai = 0
    for ci in c:
        if ai < len(a) and a[ai] >= ci:
            count += 1
        ai += 1
    return count


n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

print(game_shop(n, c, a))
