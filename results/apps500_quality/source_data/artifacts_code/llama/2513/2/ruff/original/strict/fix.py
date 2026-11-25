def zoo(s):
    N = int(input())
    s = list(s)

    # Check if N is odd
    if N % 2 == 0:
        for i in range(1, N-1, 2):
            if s[i] == 'x':
                s[i] = 'W'
                s[i+1] = 'W'
        s[1] = 'S'
        s[2] = 'S'
        s[N-1] = 'S'
        s[N] = 'S'
    else:
        # Check if N is even
        for i in range(1, N-1, 2):
            if s[i] == 'x':
                s[i] = 'S'
                s[i+1] = 'W'
        s[1] = 'S'
        s[2] = 'S'
        s[N-1] = 'W'
        s[N] = 'W'

    return ''.join(s)


# Read input
N = int(input())
s = input()

# Print output
print(zoo(s))
