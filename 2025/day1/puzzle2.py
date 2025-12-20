import re
import sys

def main():
    zero_count = 0
    position = 50
    with open(sys.argv[1], "r") as f:
        for line in f:
            prev_position = position
            move = process_line(line.rstrip())
            position += move

            if position * prev_position < 0:
                zero_count += 1

            if position < -100:
                (q, r) = divmod(abs(position), 100)
                zero_count += q
                position = r * -1
            elif position == -100:
                zero_count += 1
                position = 0
            elif position == 0:
                if prev_position != 0:
                    zero_count += 1
            elif position == 100:
                zero_count += 1
                position = 0
            elif position > 100:
                (q, r) = divmod(position, 100)
                zero_count += q
                position = r

            print(f"prev_position = {prev_position}, move = {move}, position = {position}, zero_count = {zero_count}")

    print(f"Number of zeroes = {zero_count}")

def process_line(line):
    match = re.match(r"^([LR])([0-9]+)$", line)
    assert match is not None
    multiplier = 1 if match.group(1) == "R" else -1
    clicks = int(match.group(2))
    return multiplier * clicks

if __name__ == "__main__":
    main()
