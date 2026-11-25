def can_select_odd_sum(n, x, a):
    count_odd = sum(1 for num in a if num % 2 != 0)
    if x % 2 == 0:
        return count_odd >= x
    else:
        return count_odd >= 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        x = int(data[index + 1])
        a = list(map(int, data[index + 2:index + 2 + n]))
        index += 2 + n
        results.append("Yes" if can_select_odd_sum(n, x, a) else "No")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
