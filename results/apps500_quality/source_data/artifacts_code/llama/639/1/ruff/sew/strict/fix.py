
n, x = map(int, input().split())
nums = list(map(int, input().split()))

mex = 0
while mex <= x:
    if  mex not  in nums:
        break
    mex += 1

diff = x - mex

if not mex == 0:
    print(n + diff)
else:
    print(max(0, n - 1))
