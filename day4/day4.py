def forklift(r, c, graph):
    total = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        rx, cy = dx + r, dy + c
        if 0 <= rx < len(graph) and 0 <= cy < len(graph[0]) and graph[rx][cy] == "@":
            total += 1
    return total < 4
def load(path="day4/day4.txt"):
    with open(path, "r") as f:
        return [list(line.strip()) for line in f if line.strip()]
def main():
    graph, res, unchanged = load(), 0, True
    while unchanged:
        unchanged, graphCopy = False, graph
        for r in range(len(graph)):
            for c in range(len(graph[0])):
                if graph[r][c] == "@":
                    if forklift(r, c, graph):
                        unchanged = True
                        graphCopy[r][c] = "."
                        res += 1
        graph = graphCopy
    print(res)
if __name__ == "__main__":
    main()