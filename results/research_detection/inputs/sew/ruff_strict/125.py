def find_length(string, n):
    current_sum = 0
    max_sum = 0
    for i in range(n):
        current_sum = current_sum + (1 if string[i] == "0" else -1)
        current_sum = max(current_sum, 0)
        max_sum = max(current_sum, max_sum)
    return max_sum or 0
