def calc(op, grid, idx):
    res = int(grid[0][idx])
    for row in range(1, len(grid)-1):
        if op == "+":
            res += int(grid[row][idx])
        elif op == "*":
            res *= int(grid[row][idx])
    return res
def load(path="day6/day6.txt"):
    with open(path, "r") as f:
        return [list(line.strip().split()) for line in f if line.strip()]
def main():
    grid = load()
    res = 0
    for idx in range(len(grid[0])): 
        res += calc(grid[-1][idx], grid, idx)
    print(res)
if __name__ == "__main__":
    main()