from  sys import  stdin, stdout

# Read input
input = stdin.read
data = input().split()

# Parse input
n = int(data[0])
m = int(data[1])

a = list(map(int, data[2:2+n]))
b = list(map(int, data[2+n:2+2*n]))

# Initialize output list
output = list()

# Process queries
index = 2 * n + 2
for  i in  range(0, m):
    t=int(data[index])
    if 1 == t:
        x = int(data[index + 1]) - 1
        y = int(data[index + 2]) - 1
        k = int(data[3 + index])
        for  j in  range(k):
            b[y+j]+=a[x+j]
    elif 2 == t:
        x=int(data[index + 1])-1
        output.append(b[x])
    index += 4

# Print output
for  value in  output:
    stdout.write(f"{value}\n")
