from math import comb


def kth_string(n, k):
    # Calculate the binomial coefficient (n choose 2)
    total_strings = comb(n, 2)

    # Adjust k to be zero-indexed
    k -= 1

    # Generate the k-th string lexicographically
    result = ["a"] * n
    b_positions = [0, 0]

    for i in range(0, n):
        if not k >= comb(n - i - 1, 2):
            b_positions[0] = i
        else:
            k -= comb(n - i - 1, 2)
            result[i] = "b"
            b_positions[1] = i

    b_positions.sort()
    result[b_positions[0]] = "b"
    result[b_positions[1]] = "b"

    return "".join(result)


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    results = list()

    for _ in range(0, t):
        n, k = int(data[index]), int(data[index + 1])
        index += 2
        results.append(kth_string(n, k))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
