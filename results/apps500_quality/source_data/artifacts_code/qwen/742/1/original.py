def find_minimal_permutation(b):
    n = len(b)
    a = [0] * (2 * n)
    used = [False] * (2 * n + 1)
    stack = []
    
    for i in range(n):
        b_i = b[i]
        if not stack or stack[-1] <= b_i:
            stack.append(b_i)
        else:
            while stack and stack[-1] > b_i:
                a[2 * i - 1] = stack.pop()
            if not stack:
                return -1
            stack.append(b_i)
    
    if len(stack) != 1:
        return -1
    
    a[2 * n - 1] = stack[0]
    for i in range(2 * n - 2, -1, -1):
        for j in range(1, 2 * n + 1):
            if not used[j]:
                a[i] = j
                used[j] = True
                break
    
    return a

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        b = list(map(int, data[index:index + n]))
        index += n
        result = find_minimal_permutation(b)
        if result == -1:
            results.append(-1)
        else:
            results.extend(result)
    
    for result in results:
        if result == -1:
            print(result)
        else:
            print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()
