class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # sort tree heights for each x,y coordinate
        # perform bfs from each location to find distance, or not possible

        def bfs(start, end):
            queue = [(start, 0)]
            visited = set()
            visited.add(start)

            while queue:
                (x, y), steps = queue.pop(0)

                if (x, y) == end:
                    return steps

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # if (nx, ny) in bounds add to q and visited
                    if (
                        0 <= nx < len(forest)
                        and 0 <= ny < len(forest[0])
                        and (nx, ny) not in visited
                        and forest[nx][ny] != 0
                    ):
                        queue.append(((nx, ny), steps + 1))
                        visited.add((nx, ny))

            return -1

        # get a list of (x, y, heights) for the forest and sort from shortest to tallest height
        trees = [
            (x, y, forest[x][y])
            for y in range(len(forest[0]))
            for x in range(len(forest))
            if forest[x][y] > 1
        ]
        trees.sort(key=lambda tree: tree[2])

        total_steps = 0
        current_position = (0, 0)

        for tree in trees:
            destination = (tree[0], tree[1])
            steps = bfs(current_position, destination)

            if steps == -1:
                return -1  # if not possible to reach the destination tree

            total_steps += steps
            current_position = destination

        return total_steps
