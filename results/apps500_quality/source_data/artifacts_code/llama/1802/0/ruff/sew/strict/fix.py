n = int(input())
arr = list(map(int, input().split()))

min_height = min(arr)
max_buns = 0
diff = float('inf')
for i in range(n):
    if  arr[i] - min_height < diff:
        diff = arr[i] - min_height
        max_buns = 1
    elif  arr[i] - min_height == diff:
        max_buns += 1

avg = (sum(arr) - min_height * n) // n
step = (max(arr) - min_height) // n
print(max_buns)
print(min_height, step)
