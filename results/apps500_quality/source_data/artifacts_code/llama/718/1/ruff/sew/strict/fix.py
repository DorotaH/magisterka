def  is_lucky(n):
    """Check if a number is lucky."""
    return  '8' in  str(abs(n))

def  find_lucky_floor(n):
    """Find the minimum positive integer b such that n + b is a lucky floor number."""
    if not is_lucky(n):
        n = abs(n)
        while True:
            n += 1
            if is_lucky(n):
                return n - abs(n)
    else:
        return 0

def  main():
    n=int(input())
    print(find_lucky_floor(n))

if  __name__=="__main__":
    main()
