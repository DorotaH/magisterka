MOD = 10**9 + 7


def readints():
    return [int(fld) for fld in input().strip().split()]

def combk(n, k, MOD=MOD, tbl=[]):
    if len(tbl) < k:
        tbl += [0] * k + [1]
    while n >= len(tbl):
        tbl.append(tbl[-1] * len(tbl) * pow(len(tbl) - k, MOD-2, MOD) % MOD)
    return tbl[n]

def main():
    n, k = readints()
    pairs = [readints() for _ in range(n)]
    oplist = [p for l, r in pairs for p in (2*l, 2*r+1)]
    oplist.sort()
    count = total = 0
    pos = oplist[0] // 2
    for op in oplist:
        i, delta = ((op+1)//2, -1) if op & 1 else (op//2, 1)
        total = (total + combk(count, k) * (i - pos)) % MOD
        pos = i
        count += delta
    print(total)

main()