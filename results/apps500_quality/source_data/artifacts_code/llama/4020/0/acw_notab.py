from sys import stdin

# Read input
h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

# Calculate total minutes of the contest
total_minutes = (60 * h1 + m1) - (h2 * 60 + m2)

# Calculate the midpoint minutes
midpoint_minutes = total_minutes // 2

# Calculate the hours and minutes of the midpoint
h_midpoint = (midpoint_minutes // 60) % 24
m_midpoint = midpoint_minutes % 60

# Print the result
print(f'{h_midpoint:02d}:{m_midpoint:02d}')
