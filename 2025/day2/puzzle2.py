import re
import sys

def main():
    with open(sys.argv[1], "r") as f:
        for line in f:
            ranges = process_line(line.rstrip())

    invalid_sum = 0
    for r in ranges:
        for invalid_id in process_range(r):
            invalid_sum += invalid_id

    print(f"Invalid sum = {invalid_sum}")

# Key is number of digits in the number
DIVISORS = {
    1: [],
    2: [11],
    3: [111],
    4: [101, 1111],
    5: [11111],
    6: [1001, 10101, 111111],
    7: [1111111],
    8: [1010101, 10001, 11111111],
    9: [1001001, 111111111],
    10: [101010101, 100001, 1111111111],
    11: [11111111111],
    12: [10101010101, 1001001001, 100010001, 1000001, 111111111111],
    13: [1111111111111],
    14: [1010101010101, 10000001, 11111111111111],
}

def process_line(line):
    ranges = []
    for r in line.split(","):
        parts = r.split("-")
        assert len(parts) == 2
        ranges.append((int(parts[0]), int(parts[1])))
    return ranges


def process_range(r):
    invalid_ids = []
    for n in range(r[0], r[1] + 1):
        if is_invalid(n):
            invalid_ids.append(n)
    return invalid_ids

def is_invalid(n):
    num_digits = len(str(n))
    divisors = DIVISORS[num_digits]
    for divisor in divisors:
        (q, r) = divmod(n, divisor)
        if q > 0 and r == 0:
            print(f"Invalid = {n}")
            return True
    return False


if __name__ == "__main__":
    main()
