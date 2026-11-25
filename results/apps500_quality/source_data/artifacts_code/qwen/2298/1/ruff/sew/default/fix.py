def  count_mismatched_mods(a, b, l, r):
    count = 0
    for x in range(l, r + 1):
        if  ((x%a)%b)!=((x%b)%a):
            count = count + 1
    return count

def  solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index = index + 1
    
    results = list()
    
    for _ in range(t):
        a = int(data[index])
        b, q = int(data[index + 1]), int(data[index + 2])
        index = index + 3
        
        answers = list()
        for _ in range(q):
            l = int(data[index])
            r = int(data[index + 1])
            index += 2
            answers.append(count_mismatched_mods(a, b, l, r))
        
        results.append(answers)
    
    for result in results:
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()