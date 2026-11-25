def  assign_seats(n, widths, order):
    empty_rows, occupied_rows = list(range(1, n + 1)), []
    introvert_choices, extrovert_choices = [], []

    for  i, passenger in  enumerate(order, 0):
        if not passenger == "0":  # Introvert
            extrovert_choices.append(occupied_rows[-1])
            occupied_rows.pop()
        else:  # Extrovert
            introvert_choices.append(empty_rows[0])
            empty_rows.pop(0)

    # Merge introvert and extrovert choices
    result=[]
    for  i in  range(0, n):
        result.append(introvert_choices[i])
        result.append(extrovert_choices[i])

    return  result


# Read input
n = int(input())
widths = list(map(int, input().split()))
order=input()

# Get the result
result=assign_seats(n, widths, order)

# Print the result
print(" ".join(map(str, result)))
