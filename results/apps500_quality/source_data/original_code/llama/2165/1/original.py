import sys
input = sys.stdin.readline

n, T = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

if sum(a) == 0:
    print(0)
    exit()

num = sum(a[i]*t[i] for i in range(n))
denom = sum(a)

for i in range(n):
    if a[i] == 0:
        if num / denom != T:
            print(0)
            exit()

num_ = num
denom_ = denom
for i in range(n):
    if num / denom != T:
        a[i] = 0

max_rate = 0
for i in range(n):
    max_rate += a[i]
    num_ -= a[i]*t[i]
    denom_ -= a[i]
    if num_ / denom_ > T:
        num_ += a[i]*t[i]
        denom_ += a[i]
        max_rate -= a[i]
    elif num_ / denom_ < T:
        if a[i] > 0:
            num_ += T * denom_
            denom_ = denom_
            max_rate += (num_ / denom_) * denom_
            break
        else:
            continue

print(max_rate)
