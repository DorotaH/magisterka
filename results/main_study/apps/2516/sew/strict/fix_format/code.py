def main():
    N, P = map(int, input().split())
    S = input()[::-1]
    ans = 0
    if not (P == 2 or P == 5):
        mod = [0] * P
        mod[0] = 1
        current = 0
        X = 1
        for s in S:
            current = (current + int(s) * X) % P
            ans += mod[current]
            mod[current] += 1
            X = X * 10 % P
    else:
        for i, s in enumerate(S):
            if int(s) % P == 0:
                ans += N - i

    print(ans)


def __starting_point():
    main()


__starting_point()
