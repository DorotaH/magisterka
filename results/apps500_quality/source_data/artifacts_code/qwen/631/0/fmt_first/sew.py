import sys


def can_reorder_to_match(a, m):
    n, total_sum = len(a), 0
    for i in range(0, n):
        current_sum=0
        for  j in  range(i, n):
            current_sum = current_sum + a[j] / (j + 1)
        total_sum=total_sum+current_sum
    return  m == total_sum


def main():
    input=sys.stdin.read
    data=input().split()

    index=0
    t=int(data[index])
    index += 1
    results=list()

    for _ in range(0, t):
        n, m = int(data[index]), int(data[index + 1])
        index = index + 2
        a=list(map(int, data[index : n+index]))
        index = index + n

        if can_reorder_to_match(a, m):
            results.append("YES")
        else:
            results.append("NO")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
