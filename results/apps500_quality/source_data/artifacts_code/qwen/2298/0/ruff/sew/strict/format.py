def count_mismatched_modulo(a, b, l, r):
    # Calculate the number of integers x in the range [l, r] such that
    # ((x % a) % b) != ((x % b) % a)
    count = 0
    for x in range(l, r + 1):
        if (x % a) % b != (x % b) % a:
            count = count + 1
    return count


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index = index + 1
    results = list()

    for _ in range(t):
        a = int(data[index])
        b, q = int(data[index + 1]), int(data[index + 2])
        index = index + 3
        test_case_results = list()

        for _ in range(0, q):
            l = int(data[index])
            r = int(data[index + 1])
            index += 2
            result = count_mismatched_modulo(a, b, l, r)
            test_case_results.append(result)

        results.append(test_case_results)

    for test_case_result in results:
        print(" ".join(map(str, test_case_result)))


if __name__ == "__main__":
    main()
