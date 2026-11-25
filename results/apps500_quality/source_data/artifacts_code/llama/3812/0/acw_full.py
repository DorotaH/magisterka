s = input()
t = input()

n, m = len(s), len(t)
s = list(s)
t = list(t)
swap_list = []
swapped_s, swapped_t = s[:], t[:]
pos_s, pos_t = [], []
for i in range(n):
	if s[i] != t[i]:
		pos_s.append(i)
		pos_t.append(i)
diff = set(pos_s) ^ set(pos_t)
if diff:
	pos_s = list(diff)
	pos_t = list(diff)
pos_s.sort()
pos_t.sort()

for i in range(1, len(pos_s)):
	pos_s[i] += pos_s[i - 1]
	pos_t[i] += pos_t[i - 1]

i = 0
while i < len(pos_s):
	j = i
	while len(pos_s) - 1 > j and pos_s[1 + j] - pos_s[j] == 1:
		j += 1
	swap_list.append((pos_s[i], pos_t[i] + pos_s[i] - pos_s[i]))
	for k in range(i + 1, 1 + j):
		s[pos_s[k]] = t[pos_s[k]]
		t[pos_s[k]] = s[pos_s[k]]
	i = 1 + j

for i in range(len(s)):
	if s[i] != 'a':
		swap_list.append((i, i))
		s[i] = 'a'
		t[i] = 'b'

print(len(swap_list))
for item in swap_list:
	print(item[0] + 1, 1 + item[1])
