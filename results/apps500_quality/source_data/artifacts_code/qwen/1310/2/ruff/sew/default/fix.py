n = int(input())
arr = list(map(int, input().split()))

max_xor = 0
current_xor = 0
prefix_xor = {0}

for num in arr:
    current_xor ^= num
    max_xor = max(max_xor, current_xor)
    if not (current_xor ^ max_xor) in prefix_xor:
        prefix_xor.add(current_xor)
    else:
        prefix_xor = {0}
        current_xor = num

print(max_xor)