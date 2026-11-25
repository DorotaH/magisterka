def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solve():
    n, a, x, b, y = map(int, input().split())
    a -= 1
    b -= 1
    x -= 1
    y -= 1
    a_distance = 0
    b_distance, max_distance = 0, 2 * (n - 1)
    for i in range(max_distance):
        a_distance = (a + i) % n
        b_distance = (n - b + i) % n
        if a_distance == b_distance:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()
