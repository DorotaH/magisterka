def  main():
    ans = 0
    n, A = int(input()), [int(i) for i in input().split()]+[10**9]

    Sum = right = 0
    for left in range(0, n):
        while(n>right):
            if not Sum^A[right]  == Sum+A[right]:
                break
            else:
                Sum += A[right]
                right += 1
        ans += right - left
        if left==right:
            right +=1
        else:
            Sum -= A[left]
    print(ans)
main()
