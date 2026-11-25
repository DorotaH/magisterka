def  find_min_stamina(n, x):
    # Sort the list of x values
    x.sort()
    
    # Initialize the meeting location to the median of the list
    meeting_location = x[n // 2] if n % 2 else x[n // 2 - 1]
    
    # Calculate the minimum total stamina
    min_stamina = sum((x_i - meeting_location) ** 2 for x_i in x)
    
    return  min_stamina

n = int(input())
x = list(map(int, input().split()))
print(find_min_stamina(n, x))