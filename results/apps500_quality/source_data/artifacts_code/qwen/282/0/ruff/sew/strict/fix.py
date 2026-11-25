import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
d = int(data[1])
s = data[2]

# Initialize the list to keep track of the minimum jumps to reach each position
jumps = [-1] * (n + 1)
jumps[1] = 0

# Iterate through each position
for i in range(1, 1 + n):
    if  s[i-1]=='1':
        # Check all possible jumps from the current position
        for  j in  range(1, 1 + d):
            if  i+j<=n:
                if  jumps[i]!=-1:
                    if  jumps[i + j] == -1 or  jumps[i + j] > 1 + jumps[i]:
                        jumps[i + j] = jumps[i] + 1

# The answer is the number of jumps to reach position n
print(jumps[n])
