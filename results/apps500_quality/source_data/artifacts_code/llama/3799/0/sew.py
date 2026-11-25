s=input()

def  can_win(s):
    stack = []
    for  i in  range(len(s) - 1):
        if s[i + 1] == s[i]:
            return  False
        stack.append(s[i])
    return  True

print("First" if can_win(s) else "Second")