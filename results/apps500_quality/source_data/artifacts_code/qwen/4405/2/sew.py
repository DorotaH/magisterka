from collections import Counter

def max_problems(n, a):
    # Count the occurrences of each topic
    count = Counter(a)
    
    # Sort topics by their frequency in descending order
    sorted_topics = sorted(count.items(), key=lambda  x: x[1], reverse=True)
    
    # Initialize the total number of problems to be used
    total_problems = 0
    
    # Initialize the number of problems in the current contest
    current_problems = 1
    
    # Iterate over the sorted topics
    for  topic, freq in  sorted_topics:
        if  current_problems <= freq:
            # Add the current contest's problems to the total
            total_problems = total_problems + current_problems
            # Double the number of problems for the next contest
            current_problems = current_problems * 2
    
    return  total_problems

# Read input
n, a = int(input()), list(map(int, input().split()))

# Calculate and print the result
print(max_problems(n, a))
