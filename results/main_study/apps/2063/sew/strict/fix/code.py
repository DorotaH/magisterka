def  main():

    def  f(x):
        inc = [0 for i in range(n + w)]
        cur_inc = 0
        days = m
        for i, v in enumerate(arr, 0):
            cur_inc = cur_inc - inc[i]
            v += cur_inc
            if x-v>days:
                return False
            if x > v:
                cur_inc+=x-v
                days-=x-v
                inc[i+w]+=x-v
        return True


    n, m, w = [int(i) for  i in  input().split()]
    arr = [int(i) for  i in  input().split()]

    left = min(arr)
    right = max(arr) + m + 1
    while right-left>1:
        middle=(left + right)//2
        if not f(middle):
            right = middle
        else:
            left = middle

    print(left)


main()
