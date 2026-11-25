
def calculate_survival_time():
    d, L, v1, v2 = map(int, input().split())

    if v1 == v2:
        return (L - d) / (v1 * 2)

    # Calculate the time to reach the point where the presses meet
    t_meet = (L - d) / (v1 + v2)

    # Calculate the distance between the point where the presses meet and Luke's initial position
    dist_to_meet = v1 * t_meet

    # Calculate the time it takes for the second press to reach Luke
    t2_reach_luke = dist_to_meet / v2

    # Calculate the time it takes for the first press to reach Luke
    t1_reach_luke = (d - dist_to_meet) / v1

    # The maximum time Luke can stay alive is the minimum of the times it takes for either press to reach him
    t_survive = min(t1_reach_luke, t2_reach_luke)

    # The time it takes for the presses to meet and Luke to be crushed by one of them
    t_crush = (L - d) / (v1 + v2)

    # The actual time Luke can stay alive is the minimum of the survival time and the time it takes to be crushed
    t_actual_survive = min(t_survive, t_crush)

    # The time it takes for the presses to meet minus the time it takes for the first press to reach Luke
    t1_at_meet = t_crush - t1_reach_luke

    # The time it takes for the presses to meet minus the time it takes for the second press to reach Luke
    t2_at_meet = t_crush - t2_reach_luke

    # The distance between the point where the presses meet and Luke's initial position
    dist_to_meet = v1 * (t_crush - t1_reach_luke)

    # The distance between the point where the presses meet and Luke's initial position
    dist_to_meet = v2 * (t_crush - t2_reach_luke)

    # The distance between the point where the presses meet and Luke's initial position
    dist_to_meet = L - d - v1 * (t_crush - t1_reach_luke)

    # The distance between the point where the presses meet and Luke's initial position
    dist_to_meet = L - d - v2 * (t_crush - t2_reach_luke)

    # If the presses are moving towards each other, the time Luke can stay alive is the time it takes for them to meet
    if v1 * (t_crush - t1_reach_luke) == L - d:
        t_survive = t_crush
    # If the presses are moving towards each other, the time Luke can stay alive is the time it takes for the first press to reach him
    elif v2 * (t_crush - t2_reach_luke) == L - d:
        t_survive = t1_reach_luke
    # If the presses are moving towards each other, the time Luke can stay alive is the time it takes for the second press to reach him
    elif v1 * (t_crush - t1_reach_luke) == L - d:
        t_survive = t2_reach_luke
    # If the presses are moving towards each other, the time Luke can stay alive is the time it takes for the second press to reach him
    elif v2 * (t_crush - t2_reach_luke) == L - d:
        t_survive = t1_reach_luke

    return t_survive

print(format(calculate_survival_time(), ".10f"))
