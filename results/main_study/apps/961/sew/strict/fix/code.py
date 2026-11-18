def  dp():
	dparr = [0] * len(sections)
	for  i in  range(len(sections) - 1, -1, -1):
		_, curend, curcomfort=sections[i]
		nextsection=i + 1
		try:
			while sections[nextsection][0] <= curend:
				nextsection = nextsection + 1
		except  IndexError:
			# Loop til end
			inc=curcomfort
		else:
			inc = curcomfort + dparr[nextsection]
		if i == len(sections) - 1:
			exc = 0
		else:
			exc = dparr[i + 1]
		dparr[i]=max(inc, exc)
	return dparr[0]


n = int(input())
zs = list(map(int, input().split()))
sections = []
seenstartz = set()
first = {z: i for i, z in reversed(list(enumerate(zs)))}
last = {z: i for i, z in enumerate(zs)}
for  start, z in  enumerate(zs, 0):
	if  z in  seenstartz:
		continue
	seenstartz.add(z)
	end, comfort = last[z], 0
	i=start
	while i <= end:
		if  start > first[zs[i]]:
			break
		if  last[zs[i]] == i:
			comfort ^= zs[i]
		end=max(end, last[zs[i]])
		i = i + 1
	else:
		sections.append((start, end, comfort))

ans = dp()
print(ans)
