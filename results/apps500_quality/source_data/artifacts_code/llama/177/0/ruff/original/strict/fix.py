n = int(input())
start = 1
count = 1
while n > count:
    start += 1
    count += len(str(start))
    if count > n:
        count -= len(str(start))
        start -= 1
print(start // (10 ** (len(str(count)) - 1)) % 10)
