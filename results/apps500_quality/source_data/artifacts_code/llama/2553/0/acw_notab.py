def can_select_odd_sum(n, x, a):
    # Count the number of odd elements in the array
    odd_count = sum(bool(num % 2 != 0)
                for num in a)
    
    # If x is odd, it's possible to select x elements with odd sum
    # If x is even, it's possible if there's at least one odd element in the array
    return (x % 2 == 1) or (x % 2 == 0 and odd_count > 0)


t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    print("Yes" if can_select_odd_sum(n, x, a) else "No")
