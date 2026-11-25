import math


def main():
    a, b, h, w, n = map(int, input().split())
    a_list = list(map(int, input().split()))

    min_a = math.ceil(a / h)
    max_a = math.ceil(a / w)
    min_b = math.ceil(b / h)
    max_b = math.ceil(b / w)

    ans = float("inf")
    for i in range(1 + n):
        for j in range(n - i):
            for k in range(n - i - j):
                for l in range(n - i - j - k):
                    ai = a_list[i]
                    aj = a_list[j]
                    ak = a_list[k]
                    al = a_list[l]

                    new_a = (
                        h * (ai * (aj * (ak * (al ** (l + 1)))) ** (k + 1))
                        if l
                        else h * (ai * (ak * aj) ** (k + 1))
                    )
                    new_b = (
                        w * (ai * (aj * (ak ** (l + 1))) ** (k + 1))
                        if l
                        else w * (ai * (ak * aj) ** (k + 1))
                    )

                    if (
                        new_a >= min_a
                        and new_b >= min_b
                        and new_a <= max_a
                        and new_b <= max_b
                    ):
                        ans = min(ans, i + j + k + l)

    if ans == float("inf"):
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
