#!/usr/bin/env python3


def main():
    try:
        while True:
            s, x1, x2 = list(map(int, input().split()))
            t1, t2 = list(map(int, input().split()))
            p, d = list(map(int, input().split()))

            def travel(src, trg):
                nonlocal d
                if src == trg:
                    return 0
                if trg > src:
                    if 0 < d:
                        return trg - src
                    d = 1
                    return trg + src
                else:
                    if 0 > d:
                        return src - trg
                    d = -1
                    return s - src + s - trg

            a = travel(p, x1)
            b = travel(x1, x2)
            print("%d" % min(t2 * abs(x1 - x2), (a + b) * t1))

    except EOFError:
        pass


main()
