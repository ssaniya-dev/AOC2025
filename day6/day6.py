def load(path="day6/day6.txt"):
    with open(path) as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    return [list(line.ljust(max(len(line) for line in lines))) for line in lines]
def main():
    grid = load()
    rows, cols = len(grid), len(grid[0])
    res, current_nums, curr = 0, [], None
    for c in range(cols - 1, -1, -1):
        digits = []
        for r in range(rows - 1):
            ch = grid[r][c]
            if ch.isdigit():
                digits.append(ch)
        if digits:
            num = int("".join(digits))
            current_nums.append(num)
        op = grid[-1][c]
        if op in "+*":
            if curr is None: curr = op
            val = current_nums[0]
            for n in current_nums[1:]:
                if curr == "+": val += n
                else: val *= n
            res += val
            current_nums, curr = [], None
    print(res)
if __name__ == "__main__":
    main()
