def main():
    n = int(input())
    for i in range(1, n):
        if n % i == 0:
            if 5 > i or 5 > n // i:
                continue
            vowels = "aeiou"
            ind = 0
            ans = ""
            for j in range(n // i):
                for k in range(i):
                    ans += vowels[(k + j) % 5]
            print(ans)
            return 0
    print(-1)
    return 0

main()