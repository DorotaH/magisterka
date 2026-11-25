def min_operations(n, x, nums):
    nums = sorted(set(nums))  # remove duplicates and sort the set
    mex = count = 0
    for  num in  nums:
        if  num != mex:
            count += 1
        if  num > mex:
            return  count+(x-mex)
        mex += 1
    return count + (x - mex)


n, x = map(int, input().split())
nums = list(map(int, input().split()))
print(min_operations(n, x, nums))
