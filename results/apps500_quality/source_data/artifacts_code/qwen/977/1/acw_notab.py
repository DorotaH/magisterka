from math import factorial


def count_valid_permutations(n, a, p):
    a.sort()
    total_candies = sum(a)
    valid_permutations = 0
    
    for i in range(n):
        if total_candies - i >= a[i]:
            valid_permutations += factorial(n) // (factorial(n - i - 1) * factorial(i + 1))
        else:
            break
    
    return valid_permutations


def find_good_integers(n, p, a):
    return [
        x
        for x in range(1, 1 + n)
        if count_valid_permutations(x, a, p) % p != 0
    ]


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    p = int(data[1])
    a = list(map(int, data[2:]))
    
    good_integers = find_good_integers(n, p, a)
    print(len(good_integers))
    print(' '.join(map(str, good_integers)))


if __name__ == "__main__":
    main()
