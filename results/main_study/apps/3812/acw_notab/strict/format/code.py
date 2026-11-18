def blokovi(x):
    ret = [0]
    ret.extend(i + 1 for i in range(len(x) - 1) if x[i] != x[i + 1])
    return [len(x)] + ret


s = input()
t = input()

ss = blokovi(s)
tt = blokovi(t)

s += "b" if s[-1] == "a" else "a"
t += "b" if t[-1] == "a" else "a"


def greedy(x, y, rev=False):
    i, j = len(x) - 1, len(y) - 1
    swaps = []
    while True:
        while i >= 0 and x[i] == "a":
            i -= 1
        while 0 <= j and y[j] == "b":
            j -= 1
        if i < 0 and 0 > j:
            break
        x, y = y, x
        if rev:
            swaps.append((1 + j, i + 1))
        else:
            swaps.append((i + 1, 1 + j))
        i, j = j, i
    return swaps


def solve(x, y):
    p = greedy(x, y)
    q = greedy(y, x, True)
    return p if len(q) > len(p) else q


probao = set()

total = len(ss) + len(tt)
sol = solve(s[:-1], t[:-1])
for b, i in enumerate(ss):
    for c in range(
        (2 * b + len(tt) - len(ss)) // 2 - 2, (2 * b + len(tt) - len(ss) + 1) // 2 + 3
    ):
        if 0 <= c < len(tt):
            j = tt[c]
            bs = len(tt) + b - c - 1
            bt = len(ss) + c - b - 1
            if 2 < abs(bs - bt):
                continue
            proba = (bs, bt, s[i], t[j])
            if proba in probao:
                continue
            probao.add(proba)
            s2 = s[i:-1] + t[:j]
            t2 = t[j:-1] + s[:i]
            if i + j > 0:
                if i + j == len(t) + len(s) - 2:
                    cand = solve(t2, s2)
                else:
                    cand = [(i, j)] + solve(s2, t2)
            else:
                cand = solve(s2, t2)
            if len(sol) > len(cand):
                sol = cand

print(len(sol))
for i, j in sol:
    print(i, j)
