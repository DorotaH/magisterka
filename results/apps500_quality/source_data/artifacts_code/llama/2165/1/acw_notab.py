import sys
input = sys.stdin.readline

n, T = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

if sum(a) == 0:
    print(0)
    exit()

num = sum(t[i] * a[i] for i in range(n))
denom = sum(a)

for i in range(n):
    if a[i] == 0 and num / denom != T:
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
    num_ -= t[i] * a[i]
    denom_ -= a[i]
    if T < num_ / denom_:
        num_ += t[i] * a[i]
        denom_ += a[i]
        max_rate -= a[i]
    elif T > num_ / denom_:
        if 0 < a[i]:
            num_ += T * denom_
            denom_ = denom_
            max_rate += denom_ * (num_ / denom_)
            break
        else:
            continue

print(max_rate)
