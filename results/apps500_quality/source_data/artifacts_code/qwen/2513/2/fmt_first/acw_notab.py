def determine_species(N, s):
    if s[0] == s[-1]:
        # If they are the same, the sequence must alternate
        return (
            "".join("WS" for _ in range((N - 1) // 2)) + "S"
            if s[0] == "o"
            else "W" + "".join("SW" for _ in range((N - 1) // 2))
        )
    # If they are different, the sequence must be alternating starting with W or S
    if s[0] == "o":
        # If the first is honest sheep, the sequence must be SWSSWS...
        return "S" + "".join("WS" for _ in range((N - 2) // 2)) + "S"
    else:
        # If the first is lying wolf, the sequence must be WSWSSW...
        return "".join("SW" for _ in range((N - 2) // 2)) + "W" + "S"


# Read input
N = int(input().strip())
s = input().strip()

# Determine and print the result
result = determine_species(N, s)
if result in [N * "S", "W" * N]:
    print(-1)
else:
    print(result)
