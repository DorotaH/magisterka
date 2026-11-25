import sys


def max_difference_array(n, m):
    if n == 1:
        return 0

    num_equal_elements = n // 2
    num_elements_difference = n % 2

    return (
        num_equal_elements * (num_equal_elements + 1 - num_equal_elements)
    ) * 2 + 2 * (num_elements_difference - 1) * num_equal_elements


def main():
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        print(max_difference_array(n, m))


if __name__ == "__main__":
    main()
