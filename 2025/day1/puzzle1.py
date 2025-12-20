import re
import sys

def main():
    zero_count = 0
    position = 50
    with open(sys.argv[1], "r") as f:
        for line in f:
            position += process_line(line.rstrip())
            position = position % 100
            if position == 0:
                zero_count += 1

    print(f"Number of zeroes = {zero_count}")

def process_line(line):
    match = re.match(r"^([LR])([0-9]+)$", line)
    assert match is not None
    multiplier = 1 if match.group(1) == "R" else -1
    clicks = int(match.group(2))
    return multiplier * clicks

if __name__ == "__main__":
    main()
