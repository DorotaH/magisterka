

def can_paint(r, b, k):
    lcm = r * b // math.gcd(r, b)
    if  lcm <= k:
        return True
    return False

t = int(input())
for  _ in  range(t):
    r, b, k = map(int, input().split())
    if can_paint(r, b, k):
        print('OBEY')
    else:
        print('REBEL')
