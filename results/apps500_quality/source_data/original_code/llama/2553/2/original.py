def check_odd_sum(n, x, a):
    """Check if it is possible to select exactly x elements from array a such that their sum is odd."""
    odd_count = sum(1 for num in a if num % 2 != 0)
    even_count = len(a) - odd_count
    
    # It is possible to select x elements with odd sum if and only if x is odd.
    return x % 2 != 0 or (x % 2 == 0 and odd_count >= x)

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        
        if check_odd_sum(n, x, a):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
