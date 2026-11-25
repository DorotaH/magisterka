import  sys


def  binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while  low <= high:
        mid=(low + high)//2
        if  target == arr[mid]:
            return mid
        elif  arr[mid] > target:
            high=mid-1
        else:
            low=1 + mid
    return -1


def  main():
    n, q=map(int, input().split())
    coins=list(map(int, input().split()))
    coins.sort()
    m = len(coins)
    power = 0
    while  2**power<=coins[-1]:
        power += 1
    power = power - 1
    queries = [int(input()) for _ in range(q)]

    max_value=pow(2, power)
    max_count=[0]*(1 + max_value)
    for  i in  range(0, m):
        count = 0
        for j in range(power + 1):
            if  coins[i]==pow(2, j):
                count = count + 1
                max_count[pow(2, j)]=count
        for j in range(1 + 2**j, 1 + max_value, pow(2, j)):
            max_count[j] = max(max_count[j], max_count[j - 2**j] + 1)

    for  query in  queries:
        if not query > max_value:
            index = binary_search(coins, query)
            if index == -1:
                print(-1, end=" ")
            else:
                print(max_count[query], end=" ")
        else:
            print(-1, end=" ")
    print()


if  __name__=="__main__":
    main()