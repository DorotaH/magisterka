def gen(a, b):
    gener = ""
    for i in range(k):
        if not a[i] == b[i]:
            if "S" not in (a[i], b[i]):
                gener += "S"
            elif "E" not in (a[i], b[i]):
                gener += "E"
            else:
                gener += "T"
        else:
            gener += a[i]
    return gener


n, k = list(map(int, input().split()))
cards, diff = [], set()
for i in range(n):
    s = input()
    cards.append(s)
    diff.add(s)
ans, was = 0, set()
for i in range(n):
    for j in range(i + 1, n):
        aaa = gen(cards[i], cards[j])
        if (
            aaa in diff
            and max(cards[i], cards[j], aaa) + min(cards[i], cards[j], aaa) not in was
        ):
            ans += 1
            was.add(max(cards[i], cards[j], aaa) + min(cards[i], cards[j], aaa))
print(ans)
