def is_ladder(subarray):
    n = len(subarray)
    if n == 1:
        return True
    i = 1
    while i < n and subarray[i - 1] <= subarray[i]:
        i += 1
    if i == n:
        return True
    while i < n and subarray[i - 1] >= subarray[i]:
        i += 1
    return i == n


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    array = list(map(int, data[2:2 + n]))
    queries = [(int(data[2 + n + i * 2]) - 1, int(data[2 + n + i * 2 + 1]) - 1) for i in range(m)]
    
    results = []
    for l, r in queries:
        subarray = array[l:1 + r]
        if is_ladder(subarray):
            results.append("Yes")
        else:
            results.append("No")
    
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
