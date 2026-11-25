def make_tourist_friendly(N, E, roads):
    # Check if the graph is Eulerian
    in_degree = [0] * (N + 1)
    out_degree = [0] * (N + 1)
    for a, b in roads:
        in_degree[b] += 1
        out_degree[a] += 1
    
    odd_in = [i for i in range(1, N + 1) if in_degree[i] % 2 != 0]
    odd_out = [i for i in range(1, N + 1) if out_degree[i] % 2 != 0]
    
    if len(odd_in) == 0 or len(odd_in) == 2 and odd_in[0] == odd_out[0] and odd_in[1] == odd_out[1]:
        return "YES", roads
    else:
        return "NO", []

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    E = int(data[1])
    roads = []
    index = 2
    for _ in range(E):
        a = int(data[index])
        b = int(data[index + 1])
        roads.append((a, b))
        index += 2
    
    result, modified_roads = make_tourist_friendly(N, E, roads)
    if result == "YES":
        print(result)
        for a, b in modified_roads:
            print(a, b)
    else:
        print(result)

if __name__ == "__main__":
    main()
