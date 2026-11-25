import  sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = list()

for _ in range(0, t):
    n=int(data[index])
    x, a = int(data[index + 1]), list(map(int, data[index + 2 : index + 2 + n]))
    index+=2 + n

    # Count the number of odd numbers in the array
    odd_count=sum(1 for num in a if 0 != num % 2)

    # Check if it's possible to select x elements such that their sum is odd
    if not odd_count >= x:
        results.append("No")
    else:
        results.append("Yes")

# Print all results
for result in results:
    print(result)