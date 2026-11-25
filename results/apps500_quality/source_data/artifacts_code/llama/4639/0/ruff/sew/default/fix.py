def kth_string(n, k):
    # Calculate the position of the first 'b'
    pos_b=(k-1)%(n-2)
    # Calculate the number of 'a's to the left of the first 'b'
    a_left=pos_b
    # Calculate the number of 'a's to the right of the first 'b'
    a_right=n-2-pos_b
    # Create the string
    s='a' * a_left+'b'+'a' * a_right+'b' * (n - a_left - a_right - 1)
    return s


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(kth_string(n, k))
