def m_cute_sequence():
    q = int(input())
    for _ in range(q):
        a, b, m = map(int, input().split())
        if a == b:
            print(1, a)
            continue
        if (b - a) % 2 != 0:
            print(-1)
            continue
        a_double = a * 2
        b_double = b * 2
        if a_double > b_double:
            print(-1)
            continue
        diff = (b_double - a_double) // 2
        steps = 0
        sequence = []
        while diff > 0:
            steps += 1
            if diff >= m:
                sequence.append((a + diff) // 2)
                diff = (a + diff) // 2 - a
            else:
                sequence.append(a + diff)
                diff = 0
            a = sequence[-1]
        if a != b:
            print(-1)
            continue
        print(steps, *reversed(sequence))
        continue

m_cute_sequence()
