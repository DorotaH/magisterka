from sys import stdin, stdout


def main():
    n, m = map(int, stdin.readline().split())
    s = stdin.readline().split()
    t = stdin.readline().split()
    s = list(set(s))
    t = list(set(t))

    s.sort()
    t.sort()

    s_index = {x: i for i, x in enumerate(s)}
    t_index = {x: i for i, x in enumerate(t)}

    q = int(stdin.readline())
    for _ in range(q):
        year = int(stdin.readline())
        s_pointer = (year - 1) % len(s)
        t_pointer = ((year - 1) // len(s)) % len(t)
        name = s[s_pointer] + t[t_pointer]
        while s_pointer + len(t[t_pointer]) > len(s):
            s_pointer = (s_pointer + 1) % len(s)
            t_pointer = (t_pointer + 1) % len(t)
            name += s[s_pointer]
        if len(s) - s_pointer < len(t[t_pointer]):
            t_pointer = (t_pointer + 1) % len(t)
            while s_pointer > 0:
                s_pointer = (s_pointer - 1) % len(s)
                name = s[s_pointer] + name
            name += t[t_pointer]
        stdout.write(name + '\n')

if __name__ == "__main__":
    main()
