

for i in range(0, int(input())):
	n=int(input())

	count=[0]

	if not n==1:
		for i in range(1,n):

			if i*i>n:
				break

			if i*i<=n:
				count.append(i*i)
			if i*i*i<=n:
				count.append(i*i*i)
			else:
				pass

		print(len(set(count))-1)
	else:
		print(1)

