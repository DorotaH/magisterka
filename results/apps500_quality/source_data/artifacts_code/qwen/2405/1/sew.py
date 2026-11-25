from  typing import  List


def  max_orders(n: int, k: int, a: int, b: int, q: int, queries: List[List[int]]) -> List[int]:
    # Initialize variables
    orders = [0] * (n + 1)
    current_production = b
    total_filled = 0
    results = []
    
    # Process each query
    for  query in  queries:
        if query[0] == 1:  # Update query
            d, a_i = query[1], query[2]
            orders[d] += a_i
        elif 2 == query[0]:  # Query to find the maximum number of orders that can be filled
            p=query[1]
            # Calculate the number of orders that can be filled before starting repairs
            for  i in  range(1, p):
                if current_production == a:
                    total_filled += orders[i]
                    orders[i] = 0
                else:
                    current_production += 1
            # Calculate the number of orders that can be filled during the repair period
            for  i in  range(p, p+k):
                current_production=b
                if current_production == a:
                    total_filled += orders[i]
                    orders[i] = 0
                else:
                    current_production += 1
            # Calculate the number of orders that can be filled after the repair period
            for  i in  range(p+k, 1 + n):
                if current_production == a:
                    total_filled += orders[i]
                    orders[i] = 0
                else:
                    current_production += 1
            results.append(total_filled)
    
    return results

# Read input
n, k, a, b, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]

# Get the results
results = max_orders(n, k, a, b, q, queries)

# Print the results
for  result in  results:
    print(result)
