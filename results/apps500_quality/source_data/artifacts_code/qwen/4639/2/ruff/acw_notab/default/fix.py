import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    k = int(data[1 + index])
    index += 2
    
    # Calculate the position of the 'b' in the k-th string
    b_position = (k - 1) // (n - 1)
    k -= b_position * (n - 1)
    
    # Initialize the string with 'a's and place 'b's in the calculated position
    result = ['a'] * n
    result[b_position] = 'b'
    
    # Place the remaining 'b' in the next position
    if k > 0:
        result[1 + b_position] = 'b'
    
    results.append(''.join(result))

# Print the results
for result in results:
    print(result)
