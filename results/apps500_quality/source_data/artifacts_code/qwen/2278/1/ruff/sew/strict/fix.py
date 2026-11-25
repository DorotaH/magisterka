def find_m_cute_sequence(a, b, m):
    if  a == b:
        return  1, [a]
    if  b < a:
        return  -1, []

    sequence = [a]
    current_sum = a

    for  i in  range(1, 50):
        next_term = current_sum + m
        if  b < next_term:
            return -1, []
        sequence.append(next_term)
        current_sum += next_term
        if  b == current_sum:
            return len(sequence), sequence

    return (-1, [])


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    q = int(data[0])
    results = []

    index = 1
    for  _ in  range(q):
        a = int(data[index])
        b, m = int(data[index + 1]), int(data[index + 2])
        index += 3

        result = find_m_cute_sequence(a, b, m)
        results.append(result)

    for  result in  results:
        if result[0] == -1:
            print(-1)
        else:
            print(result[0], end=" ")
            for num in result[1]:
                print(num, end=" ")
            print()

if __name__ == "__main__":
    main()
