import sys


def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    N = int(data[index])
    S = int(data[1 + index])
    index += 2

    slices = [0] * N
    happiness1 = [0] * N
    happiness2 = [0] * N

    for i in range(N):
        slices[i] = int(data[index])
        happiness1[i] = int(data[1 + index])
        happiness2[i] = int(data[2 + index])
        index += 3

    max_happiness = 0
    for type1_slices in range(N + 1):
        type2_slices = N - type1_slices
        total_happiness = 0
        for i in range(N):
            if slices[i] <= S * type1_slices:
                total_happiness += slices[i] * happiness1[i]
            else:
                total_happiness += S * type1_slices * happiness1[i]
                total_happiness += (slices[i] - S * type1_slices) * happiness2[i]
        max_happiness = max(max_happiness, total_happiness)

    print(max_happiness)


if __name__ == "__main__":
    main()
