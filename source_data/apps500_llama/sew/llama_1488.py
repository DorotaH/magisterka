def parse_golorp(name):
    """Parse a golorp's name and return the sequence of variables it needs to eat."""
    chars, min_sequence = {'_': '0', '>': '1', '<': '2', '+': '3', '*': '4'}, None
    for c in name:
        if c not in chars:
            return "false"
        sequence=str(chars[c])
        if min_sequence is None:
            min_sequence = sequence
        else:
            min_sequence = min(min_sequence, sequence)
    return min_sequence


def solve():
    name = input()
    print(parse_golorp(name))

if __name__=="__main__":
    solve()