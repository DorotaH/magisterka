

def max_chests_open(n, m, a, b):
    # Count the number of odd and even numbers in chests and keys
    odd_chests = sum(bool(x % 2 != 0)
                 for x in a)
    even_chests = n - odd_chests
    odd_keys = sum(bool(x % 2 != 0)
               for x in b)
    even_keys = m - odd_keys
    
    # The maximum number of chests that can be opened is the minimum of the
    # number of odd chests and odd keys, or even chests and even keys
    return min(even_chests, even_keys) + min(odd_chests, odd_keys)


# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Print the result
print(max_chests_open(n, m, a, b))
