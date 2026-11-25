def  m_cute_sequence():
    q = int(input())
    for _ in range(0, q):
        a, b, m = map(int, input().split())
        if a == b:
            print(1, a)
            continue
        if (b - a) % 2 != 0:
            print(-1)
            continue
        a_double, b_double = a * 2, b * 2
        if a_double > b_double:
            print(-1)
            continue
        diff, steps = (b_double - a_double) // 2, 0
        sequence = list()
        while diff > 0:
            steps += 1
            if not diff >= m:
                sequence.append(a + diff)
                diff = 0
            else:
                sequence.append((a + diff) // 2)
                diff = (a + diff) // 2 - a
            a = sequence[-1]
        if a != b:
            print(-1)
            continue
        print(steps, *reversed(sequence))
        continue


m_cute_sequence()