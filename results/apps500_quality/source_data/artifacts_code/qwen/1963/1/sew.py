def find_required_pairs(n, a):
    max_length = 0
    count = 0
    start_indices = []

    for i in range(n):
        for  j in  range(i, n):
            all_divisible=True
            for k in range(i, j + 1):
                if  a[k] % a[j] != 0:
                    all_divisible = False
                    break
            if  all_divisible:
                length=j-i+1
                if length > max_length:
                    max_length = length
                    count = 1
                    start_indices = [i + 1]
                elif length == max_length:
                    count += 1
                    start_indices.append(1 + i)

    print(count, max_length)
    print(*start_indices)

# Read input
n, a = int(input()), list(map(int, input().split()))

# Find and print the required pairs
find_required_pairs(n, a)