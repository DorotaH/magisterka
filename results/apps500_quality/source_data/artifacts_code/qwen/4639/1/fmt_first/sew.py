from  math import  comb

def  kth_string(n, k):
    # Calculate the number of strings with exactly k-1 'b's before the k-th string
    count=0
    for i in range(n-1, 0, -1):
        count += comb(n - 2, i - 1)
        if  count >= k:
            # Construct the k-th string
            result = "a" * (n - i - 1) + "b" * 2 + "a" * i
            return  result


# Read input
t, results = int(input()), []
for _ in range(0, t):
    n, k=map(int, input().split())
    results.append(kth_string(n, k))

# Print results
for result in results:
    print(result)
