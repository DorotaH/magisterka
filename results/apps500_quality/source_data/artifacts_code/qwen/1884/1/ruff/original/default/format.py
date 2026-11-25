def deploy_services(n, x1, x2, c):
    from fractions import Fraction

    def can_deploy(k1, k2):
        used = set()
        for i in range(n):
            if c[i] >= Fraction(x1, k1):
                used.add(i + 1)
                k1 -= 1
                if k1 == 0:
                    break
        if k1 != 0:
            return False
        for i in range(n):
            if c[i] >= Fraction(x2, k2) and i + 1 not in used:
                used.add(i + 1)
                k2 -= 1
                if k2 == 0:
                    break
        return k2 == 0

    for k1 in range(1, n + 1):
        for k2 in range(1, n + 1):
            if can_deploy(k1, k2):
                print("Yes")
                print(k1, k2)
                print(*[i for i in range(1, n + 1) if i in used and i <= k1])
                print(*[i for i in range(1, n + 1) if i in used and i > k1])
                return
    print("No")


# Read input
n, x1, x2 = map(int, input().split())
c = list(map(int, input().split()))

# Deploy services
deploy_services(n, x1, x2, c)
