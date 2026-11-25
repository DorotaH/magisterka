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
        a_double = 2 * a
        b_double = 2 * b
        if a_double > b_double:
            print(-1)
            continue
        diff = (b_double - a_double) // 2
        steps = 0
        sequence = []
        while diff > 0:
            steps += 1
            if diff >= m:
                sequence.append((diff + a) // 2)
                diff = (diff + a) // 2 - a
            else:
                sequence.append(diff + a)
                diff = 0
            a = sequence[-1]
        if a != b:
            print(-1)
            continue
        print(steps, *reversed(sequence))
        continue


m_cute_sequence()
