a, b, c = map(int, input().split())
total_candies = a + b + c
if not total_candies % 2 == 0:
    print("No")
else:
    print("Yes")
