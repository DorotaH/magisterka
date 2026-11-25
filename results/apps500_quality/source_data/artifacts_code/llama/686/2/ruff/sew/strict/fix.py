
def  is_prime(n):
    """Check if a number is prime."""
    if  n<=1:
        return False
    for i in range(2, 1 + int(n**0.5)):
        if  n % i == 0:
            return False
    return True

def  solve():
    """Solve the problem."""
    t = int(input())
    for _ in range(0, t):
        x, y = map(int, input().split())
        diff = x - y
        for  p in  range(2, 1 + int(diff**0.5)):
            if is_prime(p):
                if  diff % p == 0:
                    print("YES")
                    break
        else:
            if not is_prime(diff):
                print("NO")
            else:
                print("YES")

if __name__ == "__main__":
    solve()
