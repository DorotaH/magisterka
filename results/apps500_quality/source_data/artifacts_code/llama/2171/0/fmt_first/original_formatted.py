def can_reach_point(n):
    sequence = [i for i in range(1, 4)]
    while True:
        next_sequence = []
        for i in sequence:
            next_sequence.append(i + 1)
            if i + 1 <= n:
                next_sequence.append(i + 2)
            if i + 2 <= n:
                next_sequence.append(i + 3)
        if set(next_sequence).issubset(set(sequence)):
            return "yes"
        sequence = next_sequence


n = int(input())
print(can_reach_point(n))
