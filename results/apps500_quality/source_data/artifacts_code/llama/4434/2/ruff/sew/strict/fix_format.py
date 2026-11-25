def get_min_moves(n):
    return ((pow(n, 2) - 1) * (pow(n, 2) - 1)) // 2


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        print(get_min_moves(n))
