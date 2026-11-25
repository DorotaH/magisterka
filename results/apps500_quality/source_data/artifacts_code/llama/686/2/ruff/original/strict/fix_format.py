def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve():
    """Solve the problem."""
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        diff = x - y
        for p in range(2, int(diff**0.5) + 1):
            if is_prime(p):
                if diff % p == 0:
                    print("YES")
                    break
        else:
            if is_prime(diff):
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    solve()
