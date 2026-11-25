def main():
    import sys
    input=sys.stdin.read
    data=input().split()
    
    n=int(data[0])
    k, a = int(data[1]), list(map(int, data[2:]))
    
    # Convert all denominations to base k and collect the last digits
    last_digits=set()
    for  ai in  a:
        last_digit = ai % k
        last_digits.add(last_digit)
    
    # Collect the values of d for which Natasha can make the Martians happy
    happy_values = []
    for d in range(k):
        if d in last_digits:
            happy_values.append(d)
    
    # Output the number of happy values and the happy values themselves
    print(len(happy_values))
    print(' '.join(map(str, happy_values)))

if  __name__=="__main__":
    main()
