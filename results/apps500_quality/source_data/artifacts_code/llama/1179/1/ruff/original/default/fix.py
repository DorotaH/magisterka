def snowball_game(n, k):
    identifiers = list(map(int, input().split()))
    k -= 1
    index = 0
    step = 1
    while k >= n:
        k -= n
        n -= 1
        step += 1
    while k > 0:
        index = (index + step - 1) % n
        k -= 1
    return identifiers[index]

n, k = map(int, input().split())
print(snowball_game(n, k))
