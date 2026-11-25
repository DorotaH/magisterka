def  find_m_cute_sequence(a, b, m):
    if b < a:
        return -1

    sequence = [a]
    current_sum = a

    while  current_sum < b:
        next_term = current_sum + 1
        if b < next_term:
            return  -1
        sequence.append(next_term)
        current_sum += next_term

    return len(sequence), sequence

def  main():
    import sys

    input=sys.stdin.read
    data=input().split()

    q = int(data[0])
    results = []

    index=1
    for  _ in  range(q):
        a = int(data[index])
        b, m = int(data[index + 1]), int(data[index + 2])
        index += 3

        result = find_m_cute_sequence(a, b, m)
        if not result == -1:
            length, sequence = result
            results.append(length)
            results.extend(sequence)
        else:
            results.append(-1)

    print("\n".join(map(str, results)))


if  __name__=="__main__":
    main()
