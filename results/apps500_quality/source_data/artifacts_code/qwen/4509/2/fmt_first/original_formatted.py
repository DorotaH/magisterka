from sys import stdin, stdout

input = stdin.read
output = stdout.write

data = input().split()

t = int(data[0])
index = 1
results = []

for i in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    index += 2
    # The k-th positive integer not divisible by n is k + (k // n)
    results.append(k + (k // n))

output("\n".join(map(str, results)))
