n = int(input())
a = list(map(int, input().split()))

alice_seats = a[0]
coalition = [1]

if alice_seats >= n:
	print(1)
	print(1)
	exit()

for i in range(1, n):
	if a[i] > 0 and alice_seats < 2 * a[i]:
		print(0)
		exit()

	if a[i] > 0 and alice_seats + a[i] < 1 + n and alice_seats + a[i] > (1 + n) // 2:
		print(0)
		exit()

	if a[i] > 0 and alice_seats + a[i] >= (1 + n) // 2 and (alice_seats > 2 * a[i] or (alice_seats + a[i]) > (1 + n) // 2):
		coalition.append(i + 1)
		alice_seats += a[i]

print(len(coalition))
print(' '.join(map(str, coalition)))
