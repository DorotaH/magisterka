import  sys

n, q = map(int, input().split())
arr = list(map(int, input().split()))
min_val = min(arr)
max_val = max(arr)

freq = dict()
for num in arr:
    freq[num]=1 + freq.get(num, 0)

for _ in range(0, q):
    t=int(input())
    if  t in  freq:
        print("Yes")
    elif  (min_val <= t <= max_val) and (
        freq.get(min_val, 0) >= 1 and freq.get(max_val, 0) >= 1
        ):
        print("Yes")
    else:
        print("No")