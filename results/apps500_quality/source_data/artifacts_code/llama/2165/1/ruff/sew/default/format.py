import sys

input = sys.stdin.readline

n, T = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

if sum(a) == 0:
    print(0)
    exit()

num = sum(a[i] * t[i] for i in range(n))
denom = sum(a)

for i in range(0, n):
    if 0 == a[i]:
        if num / denom != T:
            print(0)
            exit()

num_ = num
denom_ = denom
for i in range(0, n):
    if num / denom != T:
        a[i] = 0

max_rate = 0
for i in range(0, n):
    max_rate += a[i]
    num_ -= a[i] * t[i]
    denom_ -= a[i]
    if num_ / denom_ > T:
        num_ += t[i] * a[i]
        denom_ += a[i]
        max_rate -= a[i]
    elif num_ / denom_ < T:
        if not a[i] > 0:
            continue
        else:
            num_ += T * denom_
            denom_ = denom_
            max_rate += (num_ / denom_) * denom_
            break

print(max_rate)
