import sys


def can_reduce_to_y(x, y):
    # The only way to reduce x to y is if the difference x - y is a sum of prime numbers
    # Since we can subtract any prime number any number of times, we just need to check if the difference is non-negative
    return x - y >= 0


def main():
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    results = []

    index = 1
    for _ in range(t):
        x = int(data[index])
        y = int(data[1 + index])
        index += 2

        if can_reduce_to_y(x, y):
            results.append("YES")
        else:
            results.append("NO")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
