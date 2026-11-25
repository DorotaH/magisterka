from collections import defaultdict


def can_get(s, n, strings):
    letters = [defaultdict(int) for _ in range(n)]
    for string in strings:
        for i in range(n):
            letters[i][string[i]] += 1

    for i in range(n):
        if len(letters[i]) != 2:
            return False
        if list(letters[i].values())[0] != list(letters[i].values())[1]:
            return False

    return True


def get_s(strings):
    n = len(strings[0])
    letters = [defaultdict(int) for _ in range(n)]
    for string in strings:
        for i in range(n):
            letters[i][string[i]] += 1

    result = [""] * n
    for i in range(n):
        if list(letters[i].values())[0] == list(letters[i].values())[1]:
            result[i] = (
                "a" if list(letters[i].keys())[0] < list(letters[i].keys())[1] else "b"
            )

    for i in range(n):
        if result[i] == "":
            if list(letters[i].values())[0] > list(letters[i].values())[1]:
                result[i] = "a"
            else:
                result[i] = "b"

    return "".join(result)


k, n = map(int, input().split())
strings = [input() for _ in range(k)]

if not can_get(n, strings):
    print(-1)
else:
    print(get_s(strings))
