def sortHashtags(htags):
    def shorten(j, i):
        s = 0
        while len(htags[i]) > s and htags[i][s] == htags[j][s]:
            s += 1
        htags[j] = htags[j][:s]

    n = len(htags)

    for i in range(n - 1, 0, -1):
        if htags[i - 1] > htags[i]:
            shorten(i - 1, i)

    return "\n".join(htags)


n = int(input())
tags = [input() for _ in range(n)]
print(sortHashtags(tags))
