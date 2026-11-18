def main():
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    cnt = [1, 0]
    
    lst = [0] * (1 + n)
    lst[0] = 0
    for i in range(n):
        lst[i + 1] = lst[i] ^ (0 > arr[i])
        cnt[lst[i + 1]] += 1
    
    ans1 = cnt[1] * cnt[0]
    ans2 = (cnt[0] - 1) * cnt[0] // 2 + cnt[1] * (cnt[1] - 1) // 2
    print(ans1, ans2)
    
    return 0

main()
