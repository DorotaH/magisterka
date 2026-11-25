def min_turns_to_chess_coloring(n):
    # For an odd-sized grid, it takes (n+1)//2 turns
    # For an even-sized grid, it takes n//2 turns
    return (n + 1) // 2

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    results = []

    for i in range(1, T + 1):
        n = int(data[i])
        results.append(str(min_turns_to_chess_coloring(n)))

    print('\n'.join(results))

if __name__ == "__main__":
    main()
