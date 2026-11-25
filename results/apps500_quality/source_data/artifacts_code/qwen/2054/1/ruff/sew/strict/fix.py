t = int(input())
results = []
for _ in range(0, t):
    a, b=map(int, input().split())
    # Calculate the maximum number of shovels Polycarp can craft
    shovels=min(a//2, b)
    # Calculate the maximum number of swords Polycarp can craft
    swords=min(a, b//2)
    # The total number of emeralds is the maximum of shovels and swords
    emeralds=max(shovels, swords)
    results.append(emeralds)
# Print all results
for result in results:
    print(result)
