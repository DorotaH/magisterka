import bisect

def  solve(n,x_coords,y_coords,k,ans):
    x_coords.sort()
    dp = list()
    for i in range(0, n):
        x = x_coords[i]
        index = bisect.bisect(x_coords,x + k) - 1
        dp.append(index - i + 1)

    dp_max = list()
    for i in reversed(dp):
        if dp_max:
            dp_max.append(max(dp_max[-1],i))
        else:
            dp_max.append(i)

    dp_max.reverse()
    max_val = 0
    for i in range(0, n):
        x = x_coords[i]
        index = bisect.bisect(x_coords,x + k) - 1
        val = index - i + 1
        if 1+index<n:
            val += dp_max[index+1]

        max_val = max(max_val,val)

    ans.append(str(max_val))

def  main():
    t, ans = int(input()), []
    for i in range(0, t):
        n,k = list(map(int,input().split()))
        x_coords, y_coords = list(map(int,input().split())), list(map(int,input().split()))
        solve(n,x_coords,y_coords,k,ans)

    print('\n'.join(ans))

    
main()
