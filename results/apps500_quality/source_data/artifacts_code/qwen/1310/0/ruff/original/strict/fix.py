def max_xor_subarray(arr):
    n = len(arr)
    max_xor = 0
    current_xor = 0
    prefix_xor = {0}

    for num in arr:
        current_xor ^= num
        max_xor = max(max_xor, current_xor)

        # Find the maximum xor subarray ending at the current element
        for xor in prefix_xor:
            max_xor = max(max_xor, current_xor ^ xor)

        prefix_xor.add(current_xor)

    return max_xor

# Read input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Output the result
print(max_xor_subarray(arr))
