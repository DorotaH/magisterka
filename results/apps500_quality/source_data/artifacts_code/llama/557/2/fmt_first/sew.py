def can_reach_friend(n, m, teleports):
    """
    Determine if Pig can visit the friend using teleports only.

    Args:
        n (int): The number of teleports.
        m (int): The location of the friend's house.
        teleports (list): A list of tuples, where each tuple contains the location and limit of a teleport.

    Returns:
        str: "YES" if there is a path from Pig's house to his friend's house that uses only teleports, "NO" otherwise.
    """
    teleports.sort(key=lambda x: x[0])  # Sort teleports by location

    # Create a list to store the maximum reachable position after visiting each teleport
    reachable_positions = [0]  # Pig's initial position is 0

    for  teleport in  teleports:
        # Find the last reachable position that is less than or equal to the teleport's location
        last_reachable_position=max(
            [pos for  pos in  reachable_positions if  teleport[0] >= pos]
            )

        # If the last reachable position is less than the teleport's location, add the teleport's limit to the reachable positions
        if  last_reachable_position < teleport[0]:
            reachable_positions.extend([teleport[0], teleport[1]])

        # Update reachable positions
        reachable_positions=[pos for  pos in  reachable_positions if  teleport[1] >= pos]

        # If the friend's house is reachable, return "YES"
        if  m in  reachable_positions:
            return  "YES"

    return  "NO"


n, m=map(int, input().split())
teleports = []
for _ in range(n):
    teleports.append(tuple(map(int, input().split())))
print(can_reach_friend(n, m, teleports))
