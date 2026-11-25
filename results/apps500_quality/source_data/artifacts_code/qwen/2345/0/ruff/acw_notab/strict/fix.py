

def find_zero_sum_subset(n: int, a: list[int]) -> list[int]:
    prefix_sum = 0
    prefix_map = {0: -1}
    for i, num in enumerate(a):
        prefix_sum += num
        if prefix_sum in prefix_map:
            return [prefix_map[prefix_sum] + 2, i + 1]
        prefix_map[prefix_sum] = i
    return []


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
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        result = find_zero_sum_subset(n, a)
        results.append(result)

    for result in results:
        print(result[0])
        print(' '.join(map(str, result[1])))


if __name__ == "__main__":
    main()
