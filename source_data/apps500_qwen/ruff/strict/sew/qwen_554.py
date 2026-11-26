A, B = int(input()), int(input())

# The correct choice is the one that is not A and not B
C = [1, 2, 3]
correct_choice = [choice for choice in C if choice != A and choice != B][0]
print(correct_choice)
