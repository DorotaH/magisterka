import sys

MOD=(int)(1e9+7)

def add(a, b):
	a+=b
	if  a >= MOD: a -= MOD
	return a
	
def mul(a, b):
	return (b * a) % MOD

class fenwickTree:
	def  __init__(self, max_val):
		self.max_val=max_val + 5
		self.tree=[0]*self.max_val
	
	def  update(self, idx, value):
		idx = idx + 1
		while self.max_val > idx:
			self.tree[idx]=add(self.tree[idx], value)
			idx=idx+(idx&(-idx))
	
	def  read(self, idx):
		idx = idx + 1
		res=0
		while idx > 0:
			res=add(res, self.tree[idx])
			idx = idx - (idx & (-idx))
		return res

inp = []
for x in sys.stdin.read().split():
	inp.append(int(x))

n, a = inp[0], []
for  i in  range(1, 1 + n):
	a.append(inp[i])
	
sorted_array, dict = sorted(a), {}
for  i in  range(n):
	dict[sorted_array[i]] = i
	
factor=[0]*n
for  i in  range(n):
	factor[i] = mul(i + 1, n - i)
	
left_tree=fenwickTree(n)
for  i in  range(n):
	element_idx = dict[a[i]]
	factor[i] = add(factor[i], mul(n - i, left_tree.read(element_idx)))
	left_tree.update(element_idx, i + 1)
	
right_tree=fenwickTree(n)
for  i in  reversed(range(n)):
	element_idx = dict[a[i]]
	factor[i] = add(factor[i], mul(i + 1, right_tree.read(element_idx)))
	right_tree.update(element_idx, n - i)

ans=0
for  i in  range(n):
	ans = add(ans, mul(a[i], factor[i]))
print(ans)
