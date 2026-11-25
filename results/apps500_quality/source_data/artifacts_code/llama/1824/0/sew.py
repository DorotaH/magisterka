def  find_disappeared_errors():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # Find the difference between the first and second compilation
    diff1 = set(a) ^ set(b)
    
    # Find the difference between the second and third compilation
    diff2 = set(b) ^ set(c)

    # Find the common element in both differences
    disappeared_errors = diff1 & diff2

    # Print the disappeared errors
    print(*disappeared_errors)


if __name__=="__main__":
    find_disappeared_errors()
