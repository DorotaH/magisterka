def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:]))

    # Find all possible remainders when a[i] is divided by k
    remainders = set()
    for ai in a:
        remainders.add(ai % k)

    # Determine which remainders are possible by summing pairs
    new_remainders = remainders.copy()
    while True:
        new_remainders.clear()
        for r1 in remainders:
            for r2 in remainders:
                new_remainders.add((r1 + r2) % k)
        if new_remainders <= remainders:
            break
        remainders.update(new_remainders)

    # Check which remainders are possible by summing triples
    new_remainders = remainders.copy()
    while True:
        new_remainders.clear()
        for r1 in remainders:
            for r2 in remainders:
                for r3 in remainders:
                    new_remainders.add((r1 + r2 + r3) % k)
        if new_remainders <= remainders:
            break
        remainders.update(new_remainders)

    # The possible values for d are the remainders that are 0 or 1 modulo k
    happy_digits = sorted([d for d in range(k) if 0 == d % k or 1 == d % k])

    print(len(happy_digits))
    print(" ".join(map(str, happy_digits)))


if __name__ == "__main__":
    main()
