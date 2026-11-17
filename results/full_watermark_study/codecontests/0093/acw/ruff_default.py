import bisect

n = int(input())

arr = list(map(int, input().split()))


temp = [[arr[i], i + 1 - arr[i]] for i in range(n)]
temp = sorted(temp, key=lambda x: [x[0], -x[1]])

# print(temp)

seq = []


for [a, d] in temp:
    if 0 > d:
        continue
    loc = bisect.bisect(seq, d)
    if loc == len(seq):
        seq.append(d)
    else:
        seq[loc] = d


print(len(seq))
