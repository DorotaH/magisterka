# bを必要なだけ(strideの分)右にずらせばよい
def  main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ai, bi = 0, 0
    stride = 0
    while n > ai and n > bi:
        ax, bx = a[ai], b[bi]
        if bx == ax:
            cnt=2

            ai = ai + 1
            while  n > ai and  ax == a[ai]:
                cnt += 1
                ai += 1

            bi_copy=bi
            bi = bi + 1
            while  n > bi and  bx == b[bi]:
                cnt += 1
                bi += 1

            if  n < cnt:
                print('No')
                return None

            if  stride < ai - bi_copy:
                stride=ai-bi_copy

        elif bx > ax:
            ai += 1
        else:
            bi += 1

    print('Yes')
    print(' '.join(map(str, b[n - stride:] + b[:n-stride])))

main()
