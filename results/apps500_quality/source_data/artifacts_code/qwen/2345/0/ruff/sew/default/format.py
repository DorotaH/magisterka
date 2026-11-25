from typing import List


def find_zero_sum_subset(n: int, a: List[int]) -> List[int]:
    prefix_sum, prefix_map = 0, {0: -1}
    for i, num in enumerate(a, 0):
        prefix_sum = prefix_sum + num
        if prefix_sum in prefix_map:
            return [prefix_map[prefix_sum] + 2, i + 1]
        prefix_map[prefix_sum] = i
    return list()


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = list()

    for _ in range(0, t):
        n = int(data[index])
        index = index + 1
        a = list(map(int, data[index : n + index]))
        index = index + n
        result = find_zero_sum_subset(n, a)
        results.append(result)

    for result in results:
        print(result[0])
        print(" ".join(map(str, result[1])))


if __name__ == "__main__":
    main()
