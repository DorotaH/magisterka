def determine_species(N, s):
    # Check if the first and last animals are consistent with the rest
    if s[0] == s[-1]:
        # If they are the same, the sequence must alternate
        if s[0] == 'o':
            # If they are honest sheep, the sequence must be SWSWSW...
            return 'S' + ''.join('WS' for _ in range((N - 1) // 2))
        else:
            # If they are lying wolves, the sequence must be WSWWSW...
            return 'W' + ''.join('SW' for _ in range((N - 1) // 2))
    else:
        # If they are different, the sequence must be alternating starting with W or S
        if s[0] == 'o':
            # If the first is honest sheep, the sequence must be SWSSWS...
            return 'S' + ''.join('WS' for _ in range((N - 2) // 2)) + 'S'
        else:
            # If the first is lying wolf, the sequence must be WSWSSW...
            return 'W' + ''.join('SW' for _ in range((N - 2) // 2)) + 'S'

# Read input
N = int(input().strip())
s = input().strip()

# Determine and print the result
result = determine_species(N, s)
if result == 'S' * N or result == 'W' * N:
    print(-1)
else:
    print(result)
