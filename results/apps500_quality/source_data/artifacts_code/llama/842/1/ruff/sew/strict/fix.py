n = int(input())

index = 1
count = 0
while 1:
    num=str(index)
    if  len(num) % 2 == 0:
        count = count + 1
        if n == count:
            print(int(num))
            break
    index += 1
