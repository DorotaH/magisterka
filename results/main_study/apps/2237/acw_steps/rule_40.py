def size(k):
    return int(math.log2(k))
def v2(k):
    return 0 if k % 2 == 1 else v2(k // 2) + 1
n = int(input())
s = list(map(int, input().split()))
import math
s.sort()
used = []
use = 0
found = {0: 1}
good = 0
for guy in s:
    big = size(guy)
    if guy not in found:
        used.append(guy)
        use += 1
        new = [boi ^ guy for boi in found]
        for guy in new:
            found[guy] = 1
        if use == 1 + big:
            good = use
if good == 0:
    print(0)
    print(0)
else:
    useful = used[:good]
    perm = ["0"]
    curr = 0
    for i in range(2**good - 1):
        curr ^= useful[v2(i + 1)]
        perm.append(str(curr))
    print(good)
    print(" ".join(perm))