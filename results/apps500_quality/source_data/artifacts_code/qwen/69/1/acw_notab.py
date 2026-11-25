from collections import defaultdict


def count_prefixes(n, x, s):
    balance = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    count = 0

    for i in range(n):
        balance += 2 * int(s[i]) - 1
        if balance == x:
            count += prefix_count[balance]
        prefix_count[balance] += 1

    if balance == x:
        return count + 1
    return count if balance < x else -1


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        x = int(data[1 + index])
        s = data[2 + index]
        index += 3
        results.append(count_prefixes(n, x, s))
    
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
