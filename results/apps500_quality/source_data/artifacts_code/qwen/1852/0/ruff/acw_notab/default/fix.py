def find_possible_parents(n, edges):
    # Create an adjacency list representation of the tree
    adj = [[] for _ in range(2**n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    # Check if the tree can be made by McDic's generation
    def can_be_mcdic(root):
        if len(adj[root]) != 2:
            return False
        left, right = adj[root]
        return can_be_mcdic(left) and can_be_mcdic(right)
    
    # Find all possible root vertices
    possible_roots = []
    for i in range(1, 2**n - 2):
        if len(adj[i]) == 2:
            left, right = adj[i]
            if can_be_mcdic(left) and can_be_mcdic(right):
                possible_roots.append(i)
    
    # Find the parent vertex of the removed vertex
    def find_removed_parent(root, parent):
        if len(adj[root]) != 2:
            return []
        left, right = adj[root]
        if left == parent:
            return [right]
        if right == parent:
            return [left]
        return find_removed_parent(right, root) + find_removed_parent(left, root)
    
    # Find all possible answers
    possible_answers = []
    for root in possible_roots:
        removed_parent = find_removed_parent(root, None)
        if removed_parent:
            possible_answers.append(removed_parent[0])
    
    # Return the number of answers and the answers themselves
    return len(possible_answers), sorted(possible_answers)


# Read input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(2**n - 3)]

# Find possible parents and answers
num_answers, answers = find_possible_parents(n, edges)

# Print output
print(num_answers)
if answers:
    print(' '.join(map(str, answers)))
