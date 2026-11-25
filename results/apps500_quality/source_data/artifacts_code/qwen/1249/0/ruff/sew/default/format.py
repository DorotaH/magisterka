from collections import Counter


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    m, k = int(data[0]), int(data[1])
    n, s = int(data[2]), int(data[3])

    a, b = list(map(int, data[4 : 4 + m])), list(map(int, data[4 + m : 4 + m + s]))

    # Check if the total number of flowers is sufficient
    if m < k * n:
        print(-1)
        return None

    # Count the required flowers in the schematic
    required = Counter(b)

    # Function to check if a given workpiece can be formed
    def can_form_workpiece(workpiece):
        count = Counter(workpiece)
        for flower, count_b in required.items():
            if count[flower] < count_b:
                return False
        return True

    # Iterate over all possible workpieces
    for i in range(0, m - k + 1):
        workpiece = a[i : i + k]
        if can_form_workpiece(workpiece):
            print(0)
            return None

    # If no valid workpiece is found, remove all flowers except the ones needed
    needed_flowers = set(b)
    to_remove = [1 + i for i, flower in enumerate(a) if flower not in needed_flowers]
    if len(to_remove) < m - (n * k):
        print(-1)
        return None

    print(len(to_remove))
    print(*to_remove)


if __name__ == "__main__":
    main()
