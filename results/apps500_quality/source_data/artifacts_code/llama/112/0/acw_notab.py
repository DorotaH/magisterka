import sys

# Read the number of cubes
n = int(input())

# Read the faces of each cube
cubes = []
for _ in range(n):
    faces = list(map(int, input().split()))
    cubes.append(faces)

# Function to check if a digit exists in the cubes


def exists(digit):
    return any(digit in faces for faces in cubes)

# Function to check if a digit is available


def available(digit):
    return exists(digit) and not exists(6 if digit == 9 else 9)


# Initialize the maximum number
max_num = 0

# Check all possible numbers from 1 to 99
for num in range(1, 100):
    # Convert the number to a string to easily check each digit
    str_num = str(num)
    
    # Check if all digits of the number are available
    if all(available(int(d)) for d in str_num):
        max_num = num
    else:
        break

# Print the maximum number
print(max_num)
