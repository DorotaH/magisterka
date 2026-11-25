from collections import Counter


def max_problems(n, a):
    # Count the number of problems for each topic
    topic_counts = Counter(a)

    # Sort the topics by the number of problems in descending order
    sorted_topics = sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)

    # Initialize the total number of problems
    total_problems = 0

    # Iterate over the sorted topics and add problems to the total
    for topic, count in sorted_topics:
        if count > 0:
            # Add the maximum possible number of problems for this topic
            total_problems = total_problems + min(count, 2 * total_problems + 1)

    return total_problems


# Read input
n, a = int(input()), list(map(int, input().split()))

# Calculate the result
result = max_problems(n, a)

# Print the result
print(result)
