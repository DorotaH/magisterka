from collections import Counter


def max_problems(n, a):
    # Count the number of problems for each topic
    topic_count = Counter(a)
    
    # Sort the topics by the number of problems in descending order
    topics = sorted(topic_count.items(), key=lambda x: x[1], reverse=True)
    
    max_problems = 0
    current_problems = 0
    
    # Iterate through the sorted topics
    for topic, count in topics:
        if count >= current_problems:
            max_problems += current_problems
            current_problems *= 2
        else:
            break
    
    # Add the remaining problems from the last contest
    max_problems += count
    
    return max_problems

# Read input
n = int(input())
a = list(map(int, input().split()))

# Print the result
print(max_problems(n, a))
