def compute_next_values(p, q, a_values, b_values, d_values, initial_values):
    # Compute the next 10 values in the sequence
    n = len(initial_values)
    next_values = [0] * 10
    for i in range(10):
        x = 0
        for j in range(p + 1):
            if a_values[j] != 0:
                x += a_values[j] * initial_values[i - j - 1]
        for j in range(q + 1):
            if b_values[j] != 0:
                x += b_values[j] * (d_values[j] ** (n + i))
        next_values[i] = x % (10**6)
    return next_values


def main():
    p, q = map(int, input().split())
    a_values = list(map(int, input().split()))
    b_values = list(map(int, input().split()))
    d_values = list(map(int, input().split()))
    initial_values = list(map(int, input().split()))

    next_values = compute_next_values(
        p, q, a_values, b_values, d_values, initial_values
    )
    print(" ".join(map(str, next_values)))


if __name__ == "__main__":
    main()
