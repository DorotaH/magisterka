def Check_Solution(a, b, c) : 
    if ((b * b) - (a * 4 * c)) > 0 : 
        return ("2 solutions") 
    elif ((b * b) - (a * 4 * c)) == 0 : 
        return ("1 solution") 
    else : 
        return ("No solutions")
