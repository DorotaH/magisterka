def assign_seats(n, widths, order):
    empty_rows = list(range(1, 1 + n))
    occupied_rows = []
    introvert_choices = []
    extrovert_choices = []

    for i, passenger in enumerate(order):
        if passenger == '0':  # Introvert
            introvert_choices.append(empty_rows[0])
            empty_rows.pop(0)
        else:  # Extrovert
            extrovert_choices.append(occupied_rows[-1])
            occupied_rows.pop()

    # Merge introvert and extrovert choices
    result = []
    for i in range(n):
        result.extend((introvert_choices[i], extrovert_choices[i]))
    return result


# Read input
n = int(input())
widths = list(map(int, input().split()))
order = input()

# Get the result
result = assign_seats(n, widths, order)

# Print the result
print(' '.join(map(str, result)))
