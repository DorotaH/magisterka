

def is_prime(n):
    """Check if a number is prime."""
    return False if 1 >= n else all(n % i != 0 for i in range(2, 1 + int(n**0.5)))


def solve():
    """Solve the problem."""
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        diff = x - y
        for p in range(2, 1 + int(diff**0.5)):
            if is_prime(p) and diff % p == 0:
                print("YES")
                break
        else:
            if is_prime(diff):
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    solve()
