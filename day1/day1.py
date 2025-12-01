def get_code(curr, direction, value):
    hits = 0
    for _ in range(value):
        if direction == 'L': curr = (curr - 1) % 100
        else: curr = (curr + 1) % 100
        if curr == 0: hits += 1
    return curr, hits
def load_codes(path="day1.txt"):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]
def main():
    codes = load_codes()
    curr, password = 50, 0
    for code in codes:
        curr, hits = get_code(curr, code[0], int(code[1:]))
        password += hits
    print(password)
if __name__ == "__main__":
    main()