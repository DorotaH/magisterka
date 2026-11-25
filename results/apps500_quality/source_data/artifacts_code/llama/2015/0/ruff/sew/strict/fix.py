

def is_possible(r, g, b):
    if  r % 2 == 0 and  g % 2 == 0 and  b % 2 == 0 or (r % 2 == 0 and  g % 2 != 0) or  (g % 2 == 0 and  r % 2 != 0) or  (b % 2 == 0 and  r % 2 != 0 and  g % 2 != 0):
        return  True
    return  False

t = int(input())
for  _ in  range(0, t):
    r, g, b = map(int, input().split())
    if is_possible(r, g, b):
        print("Yes")
    else:
        print("No")
