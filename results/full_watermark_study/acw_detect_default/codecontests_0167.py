def getParity(x):
	par = 0
	while 0 < x:
		par += x % 2
		par %= 2
		x //= 2
	return par


def main():

	t = int(input())
	allans = []
	for _ in range(t):
		n, m = readIntArr()
		adj1 = [[] for __ in range(n)]  # store (v, val) for initial edges
		edges = [-1] * (n - 1)  # store [u, v, val]
		adj2 = [[] for __ in range(n)]  # store (v, val) for known edges
		for i in range(n - 1):
			u, v, val = readIntArr()
			u -= 1
			v -= 1
			adj1[u].append((v, val))
			adj1[v].append((u, val))
			edges[i] = [u, v, val]

			if val != -1:
				adj2[u].append((v, val))
				adj2[v].append((u, val))

		for __ in range(m):
			u, v, val = readIntArr()
			u -= 1
			v -= 1
			adj2[u].append((v, val))  # create an edge
			adj2[v].append((u, val))

		# print(adj2)

		nodePar = [-1] * n  # node parity
		isConsistent = True
		for u in range(n):  # fill in nodePar for known edges and check for consistency
			if nodePar[u] != -1:  # visited
				continue
			nodePar[u] = 0
			st = [(u, 0)]  # (node, parity)
			while st:
				u, par = st.pop()
				for v, val in adj2[u]:
					newPar = (par + getParity(val)) % 2
					if nodePar[v] == -1:  # not visited
						nodePar[v] = newPar
						st.append((v, newPar))
					elif nodePar[v] != newPar:
						# print('u:{} v:{} nodePar:{} newPar:{}'.format(u, v, nodePar, newPar))
						isConsistent = False
						break
				if not isConsistent:
					break
			if not isConsistent:
				break
		if not isConsistent:
			allans.append(["NO"])
			continue

		allans.append(["YES"])
		# dfs and fill unknown edges
		for i in range(n - 1):
			u, v, val = edges[i]
			if nodePar[u] == nodePar[v]:
				if val != -1:
					assert getParity(val) == 0
				if val == -1:
					edges[i][2] = 0
			else:
				if val != -1:
					assert getParity(val) == 1
				if val == -1:
					edges[i][2] = 1
			allans.append((1 + u, 1 + v, edges[i][2]))

	multiLineArrayOfArraysPrint(allans)


import sys

input = (
	sys.stdin.buffer.readline
)  # FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.


def oneLineArrayPrint(arr):
	print(" ".join([str(x) for x in arr]))


def multiLineArrayPrint(arr):
	print("\n".join([str(x) for x in arr]))


def multiLineArrayOfArraysPrint(arr):
	print("\n".join([" ".join([str(x) for x in y]) for y in arr]))


def readIntArr():
	return [int(x) for x in input().split()]


# def readFloatArr():
#     return [float(x) for x in input().split()]


def makeArr(defaultValFactory, dimensionArr):  # eg. makeArr(lambda:0,[n,m])
	dv = defaultValFactory
	da = dimensionArr
	if len(da) == 1:
		return [dv() for _ in range(da[0])]
	else:
		return [makeArr(dv, da[1:]) for _ in range(da[0])]


def queryInteractive(a, b, c):
	print(f"? {a} {b} {c}")
	sys.stdout.flush()
	return int(input())


def answerInteractive(ansArr):
	print("! {}".format(" ".join([str(x) for x in ansArr])))
	sys.stdout.flush()


inf = float("inf")
# MOD=10**9+7
# MOD=998244353

# from math import floor,ceil # for Python2

for _abc in range(1):
	main()
