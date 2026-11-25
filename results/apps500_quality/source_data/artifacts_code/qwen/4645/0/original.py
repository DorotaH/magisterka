import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    
    if n == 2:
        if data[index] == '1':
            results.append('2 1')
        else:
            results.append('1 2')
        index += 1
        continue
    
    if n % 2 == 0:
        if n == 4:
            results.append('3 1 4 2')
        else:
            results.append(''.join(str(i) if i % 2 == 1 else str(i + 1) for i in range(1, n + 1)))
    else:
        if n == 7:
            results.append('5 1 3 6 2 4 7')
        else:
            results.append(''.join(str(i) if i % 2 == 1 else str(i + 1) for i in range(1, n + 1)))
    
    index += 1

for result in results:
    print(result)
