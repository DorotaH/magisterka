import  math

def  is_prime(n):
    """Check if a number is prime."""
    if n<=1:
        return  False
    if 2 == n:
        return  True
    if 0 == n % 2:
        return  False
    sqrt_n = math.isqrt(n)
    for  i in  range(3, 1 + sqrt_n, 2):
        if n % i == 0:
            return  False
    return  True

def  solve():
    """Solve the problem."""
    N, cards = int(input()), list(map(int, input().split()))
    cards = [1] + cards

    last_card, max_prime = cards[-1], max(cards)
    prime_factors = list()
    for  i in  range(3, 1 + last_card):
        if is_prime(i):
            prime_factors.append(i)

    covered = set()
    for  p in  prime_factors:
        if max_card := last_card - p + 1 in covered:
            covered.clear()
        for i in range(p, last_card + 1, p):
            covered.add(i)
            if last_card == i:
                return  len(prime_factors) - prime_factors.index(p)

def  main():
    """Main function."""
    t = 1  # Number of test cases
    for  _ in  range(t):
        print(solve())


if  __name__=="__main__":
    main()
