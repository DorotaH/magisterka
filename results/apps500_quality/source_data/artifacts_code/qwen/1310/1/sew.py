def  max_xor_segment(n, arr):
    max_xor=0
    current_xor, prefix_xor = 0, [0] * (n + 1)
    
    for i in range(0, n):
        current_xor^=arr[i]
        max_xor=max(max_xor, current_xor)
        prefix_xor[1 + i]=current_xor
    
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            xor_value = prefix_xor[j] ^ prefix_xor[i]
            max_xor = max(max_xor, xor_value)
    
    return max_xor

# Read input
n, arr = int(input()), list(map(int, input().split()))

# Output the result
print(max_xor_segment(n, arr))
