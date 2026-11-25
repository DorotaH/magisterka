

def can_build_garland(r, g, b):
    if  r % 2 == g % 2 or  r % 2 == b % 2 or  g % 2 == b % 2:
        return "Yes"
    return "No"

t = int(input())

for  _ in  range(t):
    r, g, b = map(int, input().split())
    print(can_build_garland(r, g, b))
