def can_rearrange(a, b, x):
    return all(b_i + a_i <= x for a_i, b_i in zip(a, b))


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        x = int(data[1 + index])
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n
        b = list(map(int, data[index:index + n]))
        index += n
        
        if can_rearrange(a, b, x):
            results.append("Yes")
        else:
            results.append("No")
    
    return "\n".join(results)


# Call the solve function and print the result
print(solve())
