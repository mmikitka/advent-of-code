import re
import sys

def main():
    if sys.argv[1] == "tests":
        run_tests()
        sys.exit(0)

    total_joltage = 0
    with open(sys.argv[1], "r") as f:
        for line in f:
            total_joltage += process_line(line.rstrip())

    print(f"Total joltage = {total_joltage}")

def process_line(line):
    desired_batteries = 12
    digits = [0] * desired_batteries
    num_digits = len(line)
    window_size = num_digits - desired_batteries
    assert window_size >= 0
    eligible = [0]
    i = 0
    print(f"line = {line}, num_digits = {num_digits}, window_size = {window_size}")
    while i < num_digits:
        cur_digit = int(line[i])

        # Iterate over eligible digits, breaking on the first selection
        for e in eligible:
            if cur_digit > digits[e]:
                digits[e] = cur_digit
                break

        # Reset remaining eligible digits to 0
        for r in range(e + 1, desired_batteries):
            digits[r] = 0

        # print(f"i = {i}, cur_digit = {cur_digit}, eligible = {eligible}, digits = {digits}")

        # Add the next eligible digit, if under the desired_batteries threshold
        remaining_digits = num_digits - (i + 1)
        if remaining_digits >= desired_batteries:
            if len(eligible) < desired_batteries:
                eligible.append(i + 1)
        else:
            _ = eligible.pop(0)

        i += 1

    result = 0
    for d in range(0, desired_batteries):
        result += digits[d] * (10 ** (11 - d))

    print(f"Line joltage = {result}")

    return result


def run_tests():
    print("Running tests")
    TESTS = [
        ("2215452689925244273244333436189317446384838478525478824435233342352236255624326767355438753493222423", 999893222423),
        # ("4324221311332133124311141233224134334423134124444233221233312314231241241143121423121121431142256789", 444444456789),
    ]
    for (line, want) in TESTS:
        got = process_line(line)
        if got == want:
            print(f"PASS: line = {line}, want = {want}, got = {got}")
        else:
            print(f"FAIL: line = {line}, want = {want}, got = {got}")


if __name__ == "__main__":
    main()
