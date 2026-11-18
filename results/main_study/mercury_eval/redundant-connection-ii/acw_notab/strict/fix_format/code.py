class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        in_degree = {v: 0 for v in range(1, len(edges) + 1)}

        adj_list = defaultdict(set)
        for edge in edges:
            in_degree[edge[1]] += 1
            adj_list[edge[0]].add(edge[1])

        def check_degrees():
            root = -1
            zero_in = 0
            for v, degree in in_degree.items():
                if degree > 1:
                    return -1
                if degree == 0:
                    zero_in += 1
                    root = v
            return root if zero_in == 1 else -1

        def dfs(v):
            if v in visited:
                return
            visited.add(v)
            for adj_v in adj_list[v]:
                dfs(adj_v)

        root = check_degrees()

        for edge in reversed(edges):
            if root == -1 or in_degree[edge[1]] > 1:
                adj_list[edge[0]].remove(edge[1])
                in_degree[edge[1]] -= 1
                found_root = check_degrees()
                if found_root != -1:
                    visited = set()
                    dfs(found_root)
                    if len(visited) == len(edges):
                        return edge
                in_degree[edge[1]] += 1
                adj_list[edge[0]].add(edge[1])
