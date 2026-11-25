def find_m_cute_sequence(a, b, m):
    if a > b:
        return -1
    if a == b:
        return 1, a

    sequence = [a]
    current = a
    while current < b:
        next_term = current + 1
        while next_term > b or m < next_term - current:
            next_term -= 1
        sequence.append(next_term)
        current += next_term

    if current != b:
        return -1

    return len(sequence), *sequence


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    q = int(data[0])
    index = 1
    results = []

    for _ in range(q):
        a = int(data[index])
        b = int(data[1 + index])
        m = int(data[2 + index])
        index += 3

        result = find_m_cute_sequence(a, b, m)
        results.append(result)

    for result in results:
        if result == -1:
            print(-1)
        else:
            k, *sequence = result
            print(k, *sequence)


if __name__ == "__main__":
    main()
