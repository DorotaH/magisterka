def  is_valid_garland(r, g, b):
    if  r % 2 == g % 2 == b % 2:
        return False
    if  r % 2 == g % 2:
        return b <= r
    if  g % 2 == b % 2:
        return r <= g
    return  b>=g + r

t = int(input())

for _ in range(t):
    r, g, b = map(int, input().split())
    if is_valid_garland(r, g, b):
        print("Yes")
    else:
        print("No")
