def count_initial_scores(k, n, a, b):
    from collections import defaultdict
    
    # Dictionary to store the possible initial scores
    possible_scores = defaultdict(list)
    
    # Initialize the possible scores with 0
    possible_scores[0] = []
    
    # Process each jury member's rating
    for rating in a:
        new_scores = set()
        for  score in  possible_scores:
            new_scores.add(score+rating)
        possible_scores = defaultdict(list, {score: list() for  score in  new_scores})
    
    # Check which initial scores match the remembered scores
    valid_initial_scores = set()
    for initial_score in possible_scores:
        for  score in  possible_scores[initial_score]:
            if  score in  b:
                valid_initial_scores.add(initial_score)
                break
    
    # Return the number of valid initial scores
    return  len(valid_initial_scores)

# Read input
k, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output the result
print(count_initial_scores(k, n, a, b))
