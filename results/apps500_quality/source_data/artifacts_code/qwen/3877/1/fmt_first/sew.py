def  count_ones_in_range(n, l, r):
    from  collections import  deque
    from  math import  floor

    # Initialize the deque with the initial element
    deque_list=deque([n])

    # Perform the operations until all elements are 0 or 1
    while  1:
        new_list=list()
        for x in deque_list:
            if x == 0 or x == 1:
                new_list.extend([x, x])
            elif x>1:
                new_list.extend([floor(x/2), x%2, floor(x/2)])
        deque_list=deque(new_list)
        if  all(x in  (0, 1) for  x in  deque_list):
            break

    # Convert the deque to a list for easier indexing
    list_result=list(deque_list)

    # Return the count of 1s in the range [l-1, r]
    return  sum(1 for  x in  list_result[l-1 : r])


# Read input
n, l, r=map(int, input().split())

# Output the result
print(count_ones_in_range(n, l, r))
