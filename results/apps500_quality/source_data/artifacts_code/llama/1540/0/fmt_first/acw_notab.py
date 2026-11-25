def process_input():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    events = []
    for _ in range(k):
        x, y = map(int, input().split())
        events.append((x - 1, y - 1))

    # Initialize a list to store the number of notifications for each employee
    notifications = [0] * n

    # Iterate over each event
    for x, y in events:
        # Find the employees in the chat
        participants = [i for i, chat in enumerate(a[y]) if chat[x]]

        # Increment the notifications count for each participant
        for participant in participants:
            notifications[participant] += len(participants) - 1

    # Print the result
    print(" ".join(map(str, notifications)))


if __name__ == "__main__":
    process_input()
