
n = int(input())
q = [list(map(int, input().split())) for _ in range(n - 2)]

first = []
second = []
third = []
for i in range(n - 2):
	first.append(q[i][0])
	second.append(q[i][1])
	third.append(q[i][2])

first_set = set(first)
second_set = set(second)
third_set = set(third)

first = list(first_set)
second = list(second_set)
third = list(third_set)

first.sort()
second.sort()
third.sort()

first_dict = {}
second_dict = {}
third_dict = {}

for i in range(n - 2):
	first_dict[first[i]] = i
	second_dict[second[i]] = i
	third_dict[third[i]] = i

p = [0] * n
i = 0
j = 0
k = 0
for i in range(n - 2):
	p[i] = first[i]
	p[i + 1] = second[i]
	p[i + 2] = third[i]
	j += 1
	while n - 2 > j and first_dict[first[j]] == i:
		j += 1
	if n - 2 > j and first_dict[first[j]] == i:
		p[n - 2] = first[j]
		p[n - 1] = second[j]
		p[n] = third[j]
	else:
		k = j
		while n - 2 > k and second_dict[second[k]] == i:
			k += 1
		if n - 2 > k and second_dict[second[k]] == i:
			p[n - 2] = second[k]
			p[n - 1] = third[k]
			p[n] = first[k]
		else:
			l = k
			while l < n - 2 and third_dict[third[l]] == i:
				l += 1
			p[n - 2] = third[l]
			p[n - 1] = first[l]
			p[n] = second[l]

print(*p)
