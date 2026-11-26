import sys


def parse(name):
    """Parses the input string to extract the jaws and stomach of the golorp."""
    jaws = []
    stomach = []
    in_jaws = False
    in_stomach = False
    for c in name:
        if c == "(":
            in_jaws = True
        elif c == ")":
            in_jaws = False
        elif c == "[":
            in_stomach = True
        elif c == "]":
            in_stomach = False
        elif c == ":":
            continue
        elif c == ",":
            in_stomach = False
        elif c == "-":
            continue
        elif c == ">":
            in_stomach = False
        elif c == "<":
            in_stomach = True
        elif in_jaws:
            jaws.append(c)
        elif in_stomach:
            stomach.append(c)
        else:
            raise ValueError("Invalid character")
    return jaws, stomach


def get_min_diet(jaws, stomach):
    """Calculates the lexicographically smallest sequence of variable values fit for feeding the golorp."""
    min_diet = []
    for c in jaws:
        if c in ["+", "*"]:
            min_diet.append("1")
        elif c == "-":
            min_diet.append("0")
    for c in stomach:
        if c == ">":
            min_diet.append("9")
        elif c == "<":
            min_diet.append("0")
    return "".join(min_diet)


def main():
    name = input().strip()
    try:
        jaws, stomach = parse(name)
        diet = get_min_diet(jaws, stomach)
        if diet:
            print(diet)
        else:
            print("false")
    except ValueError as e:
        print("false")


if __name__ == "__main__":
    main()
