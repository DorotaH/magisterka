for _ in range(int(input())):
    k = int(input())
    sr = int((k - 1) ** .5)
    r = k - (sr * sr)
    if not r <= sr:
        print(sr + 1, sr + sr + 2 - r)
    else:
        print(r, sr + 1)