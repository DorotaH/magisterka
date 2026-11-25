def can_rearrange(a, b, x):
    for i in range(len(a)):
        if a[i]+b[i]>x:
            return  False
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n, x = int(data[index]), int(data[index + 1])
        index += 2
        a = list(map(int, data[index:n + index]))
        index += n
        b = list(map(int, data[index:n + index]))
        index += n

        if can_rearrange(a, b, x):
            results.append("Yes")
        else:
            results.append("No")

    print("\n".join(results))

if __name__=="__main__":
    main()
