def  min_turns_to_single_color(n, colors):
    # Find the most frequent color in the list
    from collections import Counter
    color_count = Counter(colors)
    most_common_color, _ = color_count.most_common(1)[0]
    
    # Count how many squares need to be changed to the most frequent color
    turns = sum(1 for color in colors if color != most_common_color)
    
    return  turns

# Read input
n = int(input())
colors = list(map(int, input().split()))

# Output the result
print(min_turns_to_single_color(n, colors))