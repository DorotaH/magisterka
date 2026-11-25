n = int(input())

index = 1
count = 0
while True:
	num = str(index)
	if len(num) % 2 == 0:
		count += 1
		if count == n:
			print(int(num))
			break
	index += 1
