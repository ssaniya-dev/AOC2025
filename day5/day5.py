# def check_expiry(f, ranges):
#     for r in ranges:
#         l, h = r.split("-")
#         if int(l) <= f <= int(h): return True 
#     return False
def merge_ranges(intervals):
    intervals.sort() 
    new_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= new_intervals[-1][1]:
            new_intervals[-1][1] = max(intervals[i][1], new_intervals[-1][1])
        else:
            new_intervals.append(intervals[i])
    return new_intervals
def check_ranges(intervals):
    res = 0 
    for l, r in intervals:
        res += r - l + 1
    return res
def load_ids(path="day5/day5.txt"):
    ranges, i = [], []
    with open(path, "r") as f:
        for line in f:
            if "-" in line:
                r = line.split("-")
                ranges.append([int(r[0]), int(r[1])])
            elif line.strip():
                i.append(line.strip())
    return ranges, i
def main():
    ranges, _ = load_ids()
    res = 0
    ranges = merge_ranges(ranges)
    res = check_ranges(ranges) 
    print(res)
if __name__ == "__main__":
    main()