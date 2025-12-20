import re
import sys

def main():
    total_joltage = 0
    with open(sys.argv[1], "r") as f:
        for line in f:
            total_joltage += process_line(line.rstrip())

    print(f"Total joltage = {total_joltage}")

def process_line(line):
    first_digit = 0
    second_digit = 0
    num_digits = len(line)
    i = 0
    while i < num_digits:
        cur_digit = int(line[i])
        if i == 0:
            # First digit
            if cur_digit > first_digit:
                first_digit = cur_digit
        elif i == num_digits - 1:
            # Last digit
            if cur_digit > second_digit:
                second_digit = cur_digit
        else:
            # Middle digits
            if cur_digit > first_digit:
                first_digit = cur_digit
                second_digit = 0
            else:
                if cur_digit > second_digit:
                    second_digit = cur_digit
        i += 1

    return first_digit * 10 + second_digit

if __name__ == "__main__":
    main()
