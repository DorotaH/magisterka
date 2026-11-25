def is_possible(a, b, c):
    # Calculate the total candies
    total = a + b + c
    
    # Check if total is even
    if total % 2 != 0:
        return False
    
    # Calculate the target number of candies for each student
    target = total // 2
    
    # Check if it is possible to distribute the candies
    return (a >= target and (a - target) % 2 == 0) and (b >= target and (b - target) % 2 == 0) or (target <= c and (c - target) % 2 == 0)


a, b, c = map(int, input().split())
if is_possible(a, b, c):
    print("Yes")
else:
    print("No")
