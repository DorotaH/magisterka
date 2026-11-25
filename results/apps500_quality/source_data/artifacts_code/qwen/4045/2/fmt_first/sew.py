def  generate_string(n, s, t):
    if  t == s:
        if s == "ab":
            return "NO"
        else:
            res = "a" * n + "b" * n + "c" * n
            if s not in res:
                return "YES\n" + res
            else:
                return "NO"

    if  s == "ab":
        if  t == "bc":
            res="cacb"*n
        elif  t=="ca":
            res = "cabc" * n
        elif  t=="ac":
            res = "abca" * n
        elif  t=="cb":
            res = "acba" * n
    elif  s == "bc":
        if  t=="ab":
            res="cacb"*n
        elif  t=="ca":
            res="cbac"*n
        elif  t=="ac":
            res="baca"*n
        elif  t=="cb":
            res="bacb"*n
    elif  s == "ca":
        if  t=="ab":
            res="cacb"*n
        elif  t=="bc":
            res="cbac"*n
        elif  t=="ac":
            res="abac"*n
        elif  t=="cb":
            res="babc"*n

    if s not in res and t not in res:
        return "YES\n" + res
    else:
        return "NO"


# Read input
n, s = int(input()), input()
t=input()

# Generate and print the result
result=generate_string(n, s, t)
print(result)