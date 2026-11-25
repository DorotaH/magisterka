

def  count_valid_permutations(n: int, a: list[int]) -> int:
    # Sort the array a to simplify the problem
    a.sort()
    
    # Initialize the count of valid permutations
    valid_permutations=0
    
    # Iterate over all possible values of x
    for x in range(1, 1 + n):
        # Check if there is a valid permutation for the current value of x
        if all(x >= a[i] for i in range(n)):
            valid_permutations += 1
    
    return  valid_permutations


def  find_good_integers(n: int, p: int, a: list[int]) -> list[int]:
    # Count the number of valid permutations for each x
    valid_counts = []
    for i in range(1, n + 1):
        valid_counts.append(count_valid_permutations(n, a[:i]))
    
    # Find all good integers x
    good_integers = []
    for x, count in enumerate(valid_counts, start=1):
        if count % p != 0:
            good_integers.append(x)
    
    return  good_integers


def  main():
    import sys
    input=sys.stdin.read
    data=input().split()
    
    n=int(data[0])
    p, a = int(data[1]), list(map(int, data[2:]))
    
    good_integers=find_good_integers(n, p, a)
    
    print(len(good_integers))
    print(' '.join(map(str, good_integers)))

if __name__=="__main__":
    main()
