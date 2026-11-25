def process_slimes(n):
    slimes=[1]
    for  _ in  range(1, n):
        slimes.append(slimes[-1])
        while  len(slimes) >= 2 and  slimes[-2] == slimes[-1]:
            slimes=slimes[0:-2]+[slimes[-1] + 1]
    return slimes

# Read input
n = int(input().strip())

# Process and print the result
result = process_slimes(n)
print(" ".join(map(str, result)))
