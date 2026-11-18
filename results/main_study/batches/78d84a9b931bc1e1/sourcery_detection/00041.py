MOD = 7 + 10**9

from sys import stderr


def readints():
	return [int(fld) for fld in input().strip().split()]


def combk(n, k, MOD=MOD, tbl=[]):
	if k > len(tbl):
		tbl += [0] * k + [1]
	while len(tbl) <= n:
		tbl.append(len(tbl) * tbl[-1] * pow(len(tbl) - k, MOD - 2, MOD) % MOD)
	return tbl[n]


def main():
	n, k = readints()
	pairs = [readints() for _ in range(n)]
	oplist = [p for l, r in pairs for p in (2 * l, 2 * r + 1)]
	oplist.sort()
	count = total = 0
	pos = oplist[0] // 2
	for op in oplist:
		i, delta = ((1 + op) // 2, -1) if op & 1 else (op // 2, 1)
		total = (total + combk(count, k) * (i - pos)) % MOD
		pos = i
		count += delta
	print(total)


main()
