
def naiveSolve():
	
	
	
	return



def solve():
	
	
	
	return


from types import GeneratorType


def bootstrap(f, stack=[]):
	def wrappedfunc(*args, **kwargs):
		if stack:
			return f(*args, **kwargs)
		to = f(*args, **kwargs)
		while True:
			if type(to) is GeneratorType:
				stack.append(to)
				to = next(to)
			else:
				stack.pop()
				if not stack:
					break
				to = stack[-1].send(to)
		return to

	return wrappedfunc


def main():
	
	t = int(input())
	allans = []
	for _ in range(t):
		n = int(input())
		adj = [[] for _ in range(1 + n)]
		for __ in range(n - 1):
			u, v = readIntArr()
			adj[u].append(v)
			adj[v].append(u)
		
		
		pruned = [False] * (1 + n)
		budCnts = [0]
		childCnts = [0] * (1 + n)

		@bootstrap
		def dfs(node):
			for nex in adj[node]:
				if not (2 <= len(path) and nex == path[-2]): # not parent
					childCnts[node] += 1
					path.append(nex)
					yield dfs(nex)
					path.pop()
			if len(path) >= 3 and pruned[node] == pruned[path[-2]] == False: # prune here
				budCnts[0] += 1
				pruned[path[-2]] = True
				childCnts[path[-3]] -= 1
			yield None
		path = [1]
		dfs(1)
		
		budCnts = budCnts[0]
		directLeaves = childCnts[1]
		budContribution = n - 1 - directLeaves - 2 * budCnts # for each bud, cover the parent and the parent of parent
		leavesWithoutBud = max(1, directLeaves) # if no leaves, treat root as leave
		ans = leavesWithoutBud + budContribution
		allans.append(ans)
					
	multiLineArrayPrint(allans)
	
	return




import sys
input = sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.


def oneLineArrayPrint(arr):
	print(' '.join([str(x) for x in arr]))


def multiLineArrayPrint(arr):
	print('\n'.join([str(x) for x in arr]))


def multiLineArrayOfArraysPrint(arr):
	print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))


def readIntArr():
	return [int(x) for x in input().split()]
# def readFloatArr():
#     return [float(x) for x in input().split()]


def makeArr(defaultValFactory, dimensionArr): # eg. makeArr(lambda:0,[n,m])
	dv = defaultValFactory; da = dimensionArr
	if len(da) == 1: return [dv() for _ in range(da[0])]
	else: return [makeArr(dv, da[1:]) for _ in range(da[0])]


def queryInteractive(x):
	print('{}'.format(x))
	sys.stdout.flush()
	return int(input())


def answerInteractive(ans):
	print('! {}'.format(ans))
	sys.stdout.flush()


inf = float('inf')
# MOD=10**9+7
# MOD=998244353

from math import gcd, floor, ceil
# from math import floor,ceil # for Python2

for _abc in range(1):
	main()
