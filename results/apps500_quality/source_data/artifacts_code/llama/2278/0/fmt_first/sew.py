def solve(a, b, m):
    if  a == b:
        return  f"{1} {a}"
    if  a > b:
        return  "-1"
    if  (a + 1)*(b-a)<=m:
        return  "-1"
    for i in range(a, b // 2 + 1):
        if  b-i>m and  (b - i) % m == 0:
            return  f"{b-i} {i} {a}"
    return "-1"


def main():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        print(solve(a, b, m))


if  __name__=="__main__":
    main()