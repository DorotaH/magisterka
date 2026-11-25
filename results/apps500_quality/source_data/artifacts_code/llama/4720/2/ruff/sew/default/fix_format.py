def count_people():
    # Read the number of groups
    N = int(input())

    # Initialize a list to store the occupied seats
    seats = 100001 * [False]

    # Read the groups
    for _ in range(N):
        # Read the start and end seat of the current group
        l, r = map(int, input().split())

        # Mark the occupied seats
        for i in range(l, 1 + r):
            seats[i] = True

    # Count the number of people
    people = sum(1 for seat in seats if seat)

    print(people)


# Call the function
count_people()
