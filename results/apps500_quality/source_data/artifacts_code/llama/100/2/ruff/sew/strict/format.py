def find_min_frame(n, m, monitor):
    min_frame_size = float("inf")
    min_frame = None
    for i in range(n):
        for j in range(m):
            if monitor[i][j] == "w":
                frame_size = 1
                while (
                    i - frame_size >= 0
                    and j - frame_size >= 0
                    and i + frame_size < n
                    and j + frame_size < m
                ):
                    if (
                        all(
                            monitor[i - frame_size][j] == "w"
                            or monitor[i - frame_size][j] == "."
                            for _ in range(0, j + 1)
                        )
                        and all(
                            monitor[i - frame_size][j] == "w"
                            or monitor[i - frame_size][j] == "."
                            for _ in range(j, frame_size + j)
                        )
                        and all(
                            monitor[i - frame_size][j] == "w"
                            or monitor[i - frame_size][j] == "."
                            for _ in range(frame_size + j, m)
                        )
                        and all(
                            monitor[i - frame_size][k] == "w"
                            or monitor[i - frame_size][k] == "."
                            for j in range(0, m)
                        )
                        and all(
                            monitor[i][k] == "w" or monitor[i][k] == "."
                            for j in range(0, m)
                        )
                        and all(
                            monitor[frame_size + i][k] == "w"
                            or monitor[frame_size + i][k] == "."
                            for j in range(0, m)
                        )
                    ):
                        frame_size += 1
                    if frame_size > min_frame_size:
                        break
                if min_frame_size > frame_size:
                    min_frame_size = frame_size
                    min_frame = (i - min_frame_size, j - min_frame_size)
    if not min_frame is not None:
        return "-1"
    else:
        frame = [["." for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if monitor[i][j] == "w":
                    frame[i][j] = "w"
        for i in range(n):
            frame[i][min_frame[1]] = "+"
            frame[i][min_frame[1] + min_frame_size - 1] = "+"
        for j in range(m):
            frame[min_frame[0]][j] = "+"
            frame[min_frame[0] + min_frame_size - 1][j] = "+"
        for i in range(n):
            for j in range(m):
                if frame[i][j] == "+":
                    frame[i][j] = "+"
                elif frame[i][j] == ".":
                    frame[i][j] = "."
        return "\n".join(["".join(row) for row in frame])


n, m = map(int, input().split())
monitor = [list(input().strip()) for _ in range(0, n)]
print(find_min_frame(n, m, monitor))
