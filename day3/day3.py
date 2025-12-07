def extract_voltage(num):
    stack, dropped = [], len(num) - 12
    for n in num:
        while stack and int(n) > int(stack[-1]) and dropped > 0: 
            stack.pop()
            dropped -= 1 
        stack.append(n)
    return int(''.join(stack[:12]))
def load_ids(path="day3/day3.txt"):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]
def main():
    ids = load_ids()
    res = 0
    for i in ids:
        res += extract_voltage(str(i))
    print(res)
if __name__ == "__main__":
    main()