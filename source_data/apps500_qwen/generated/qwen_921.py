def max_number(n, cubes):
    from collections import defaultdict
    
    # Create a dictionary to store all possible rotations of each digit
    rotations = defaultdict(set)
    for i in range(n):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    for m in range(6):
                        for o in range(6):
                            faces = [cubes[i][j], cubes[i][k], cubes[i][l], cubes[i][m], cubes[i][o], cubes[i][(j + 1) % 6]]
                            faces.sort()
                            rotations[tuple(faces)].add(cubes[i][j])
    
    # Find the maximum number that can be formed
    max_num = 0
    for num in range(1, 1000000):
        used_digits = set()
        for digit in str(num):
            found = False
            for faces in rotations.values():
                if digit in faces:
                    used_digits.add(digit)
                    found = True
                    break
            if not found:
                break
        else:
            max_num = max(max_num, num)
    
    return max_num

# Read input
n = int(input())
cubes = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_number(n, cubes))
