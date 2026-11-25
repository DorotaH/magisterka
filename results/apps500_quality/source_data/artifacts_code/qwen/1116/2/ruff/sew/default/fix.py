def  can_paint_fence(r, b, k):
    if r == 1 and b == 1:
        return  "REBEL"
    if r == 1:
        return  "OBEY" if  k>1 else "REBEL"
    if b == 1:
        return  "OBEY" if  k>1 else "REBEL"
    if b == r:
        return  "OBEY" if  k>1 else "REBEL"
    if r % b == 0 or b % r == 0:
        return  "OBEY" if  k>1 else "REBEL"
    return "OBEY"

T = int(input())
results = []
for  _ in  range(T):
    r, b, k = map(int, input().split())
    results.append(can_paint_fence(r, b, k))
print(*results, sep='\n')