def find_m_cute_sequence(a, b, m):
    if a > b:
        return -1
    if a == b:
        return (1, a)
    
    sequence, current = [a], a
    while  b > current:
        next_term=1 + current
        while next_term > b or next_term-current>m:
            next_term -= 1
        sequence.append(next_term)
        current += next_term
    
    if b != current:
        return -1
    
    return (len(sequence), *sequence)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q, index = int(data[0]), 1
    results = list()
    
    for _ in range(0, q):
        a=int(data[index])
        b = int(data[index + 1])
        m = int(data[index + 2])
        index = index + 3
        
        result=find_m_cute_sequence(a, b, m)
        results.append(result)
    
    for result in results:
        if not result == -1:
            k, *sequence = result
            print(k, *sequence)
        else:
            print(-1)

if  __name__ == "__main__":
    main()
