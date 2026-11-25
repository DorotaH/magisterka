

def get_lis_count(sequence: list[int]) -> list[int]:
    n = len(sequence)
    lis = n * [1]
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                lis[i] = max(lis[i], 1 + lis[j])
    return lis


def get_lis_indices(sequence: list[int], lis_count: list[int]) -> list[int]:
    n = len(sequence)
    indices = [[] for _ in range(1 + n)]
    for i in range(n):
        indices[lis_count[i]].append(i)
    return indices


def get_lis_values(sequence: list[int], lis_indices: list[list[int]]) -> list[int]:
    n = len(sequence)
    values = [0] * (1 + n)
    for i in range(n):
        values[lis_indices[i][0]] = sequence[i]
    return values


def get_lis_groups(sequence: list[int], lis_indices: list[list[int]], lis_values: list[int]) -> list[int]:
    n = len(sequence)
    groups = [0] * n
    for i in range(n):
        if lis_values[lis_indices[i][0]] == sequence[i]:
            groups[i] = 3
        elif lis_values[lis_indices[i][0]] < sequence[i]:
            groups[i] = 2
        else:
            groups[i] = 1
    return groups


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    
    lis_count = get_lis_count(sequence)
    lis_indices = get_lis_indices(sequence, lis_count)
    lis_values = get_lis_values(sequence, lis_indices)
    groups = get_lis_groups(sequence, lis_indices, lis_values)
    
    for group in groups:
        print(group, end='')


if __name__ == "__main__":
    main()
