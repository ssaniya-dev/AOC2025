def invalid(num):
    length = len(num) 
    middle = length // 2 
    for i in range(1, middle + 1):
        if length % i == 0:
            if num[:i] * (length // i - 1) == num[i:]: 
                return True 
    return False
def load_ids(path="day2/day2.txt"):
    with open(path, "r") as f:
        return f.read().split(',')
def main():
    ids = load_ids()
    res = 0
    for i in ids:
        start, end = i.split("-")
        for j in range(int(start), int(end) + 1):
            if invalid(str(j)): res += j
    print(res)
if __name__ == "__main__":
    main()