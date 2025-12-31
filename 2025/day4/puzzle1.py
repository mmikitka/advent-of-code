import re
import sys

def main():
    total_rolls = 0
    with open(sys.argv[1], "r") as f:
        rows = []
        for line in f:
            row = process_line(line.rstrip())
            if len(rows) == 0:
                # Top 0 row to make calculations easier
                rows.append([0] * len(row))
            rows.append(row)
            if len(rows) == 3:
                total_rolls += count_accessible_rolls(rows)
                _ = rows.pop(0)

        # Last roll. Append 0 row to make calulcations easier.
        rows.append([0] * len(row))
        total_rolls += count_accessible_rolls(rows)

    print(f"Total rolls = {total_rolls}")

def process_line(line):
    row = []
    for c in line:
        if c == "@":
            row.append(1)
        else:
            row.append(0)
    return row

def count_accessible_rolls(rows):
    print(f"Counting rolls in {rows}")
    num_accessible = 0
    assert len(rows) == 3
    top = rows[0]
    middle = rows[1]
    bottom = rows[2]
    num_cells = len(middle)
    for i in range(num_cells):
        if middle[i] != 1:
            continue

        num_rolls = 0

        # Left column
        if i > 0:
            num_rolls += top[i-1]
            num_rolls += middle[i-1]
            num_rolls += bottom[i-1]

        # Right column
        if i < num_cells - 1:
            num_rolls += top[i+1]
            num_rolls += middle[i+1]
            num_rolls += bottom[i+1]

        # Current column
        num_rolls += top[i]
        num_rolls += bottom[i]

        if num_rolls < 4:
            print(f"Selecting roll in cell {i}")
            num_accessible += 1

    return num_accessible

if __name__ == "__main__":
    main()
