import  sys

def game_shop(n, c, a):
    count = ai = 0
    for  ci in  c:
        if not (ai < len(a) and a[ai] >= ci):
            ai += 1
        else:
            count += 1
            ai += 1
    return  count

n, m = map(int, input().split())
c, a = list(map(int, input().split())), list(map(int, input().split()))

print(game_shop(n, c, a))
