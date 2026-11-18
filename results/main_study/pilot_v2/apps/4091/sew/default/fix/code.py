
def  mi():
	return  map(int, input().split())

n, k=mi()
a=list(mi())
for  i in  range(n):
	a[i]=[a[i],i]

a.sort(reverse= True)

a=a[:k]
s, ind = 0, []
for  i in  a:
	s+=i[0]
	ind.append(i[1])
ind.sort()
for  i in  range(k):
	ind[i]+=1
ind1=ind.copy()
for  i in  range(1,len(ind)):
	ind[i]-=ind1[i-1]
ind[-1]=n-sum(ind[:k-1], 0)
print (s)
for  i in  ind:
	print (i, end = ' ')