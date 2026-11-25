a, b, c = map(int, input().split())
total_candies = a + b + c
if total_candies % 2 == 0:
    print("Yes")
else:
    print("No")
