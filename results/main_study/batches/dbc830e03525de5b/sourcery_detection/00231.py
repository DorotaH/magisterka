def main():
    n = int(input())
    a = [input() for _ in range(n)]

    result = 0
    for i in range(26):
        for j in range(i + 1, 26):
            ci = chr(i + ord('a'))
            cj = chr(j + ord('a'))
            t = sum(len(s) for s in a if s.count(ci) + s.count(cj) == len(s))
            result = max(result, t)

    print(result)



main()
