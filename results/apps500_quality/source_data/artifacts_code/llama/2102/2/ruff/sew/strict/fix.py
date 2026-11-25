
def  solve():
    a, n = list(map(int, input().split())), int(input())
    b = list(map(int, input().split()))

    freq, used = [0] * 6, False

    min_fret, max_fret = float('inf'), float('-inf')

    for i in range(0, n):
        for j in range(0, 6):
            if  b[i] <= a[j] + 10**9:
                freq[j]+=1
                used=True
                max_fret=max(max_fret, b[i]-a[j])
                min_fret=min(min_fret, b[i]-a[j])
                break

    if  not  used:
        max_fret, min_fret = b[-1], 0

    print(max_fret - min_fret)

if __name__ == '__main__':
    solve()
