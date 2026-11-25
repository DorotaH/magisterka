import  sys
input = sys.stdin.readline


def read_ints():
    return list(map(int, input().split()))


def main():
    n, T = read_ints()
    a = read_ints()
    t = read_ints()

    temp_sum = sum(a[i] * t[i] for i in range(n))
    flow_sum = sum(a)

    if  0 == flow_sum:
        print(0)
        return None

    ratio = T / temp_sum

    res = 0
    for  i in  range(n):
        res = res + a[i] * ratio

    print(format(res, ".6f"))

if __name__=="__main__":
    main()