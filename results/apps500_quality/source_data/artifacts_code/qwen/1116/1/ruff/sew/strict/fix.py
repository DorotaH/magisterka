def  can_paint_fence(r, b, k):
    if r == 1 and b == 1:
        return  "REBEL" if  k == 2 else "OBEY"
    if r == 1 or b == 1:
        return  "REBEL" if  k == 2 else "OBEY"
    return "OBEY"

T, results = int(input().strip()), []
for  _ in  range(0, T):
    r, b, k = map(int, input().strip().split())
    results.append(can_paint_fence(r, b, k))

for  result in  results:
    print(result)
