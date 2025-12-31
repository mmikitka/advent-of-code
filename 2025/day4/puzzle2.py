import re
import sys

CELL_ROLL = "@"
CELL_REMOVABLE = "x"
CELL_EMPTY = "."

def main():
    rows = []
    with open(sys.argv[1], "r") as f:
        rows = []
        for line in f:
            rows.append(process_line(line.rstrip()))

    total_rolls = 0
    while True:
        for r in rows:
            print("".join(r))
        iteration_rolls, rows = process_rows(rows)
        print(f"Iteration rolls removed = {iteration_rolls}")
        if iteration_rolls == 0:
            break
        total_rolls += iteration_rolls

    print(f"Total rolls = {total_rolls}")

def process_line(line):
    return [c for c in line]

def process_rows(rows):
    rolls_removable = 0
    num_rows = len(rows)
    for row_idx in range(num_rows):
        row = rows[row_idx]
        num_cells = len(row)
        for cell_idx in range(num_cells):
            adjacent_rolls = 0

            if cell_idx > 0:
                # This cell has adjacent left column
                if row_idx > 0:
                    # Top row has no top-left neighbour
                    adjacent_rolls += (rows[row_idx - 1][cell_idx - 1] != CELL_ROLL)
                elif row_idx < num_rows - 1:
                    # Bottom row has no bottom-left neighbour
                    adjacent_rolls += (rows[row_idx + 1][cell_idx - 1] != CELL_ROLL)

                adjacent_rolls += (rows[row_idx][cell_idx - 1] != CELL_ROLL)

            if cell_idx < num_cells - 1:
                # This cell has adjacent right column
                if row_idx > 0:
                    # Top row has no top-right neighbour
                    adjacent_rolls += (rows[row_idx - 1][cell_idx + 1] != CELL_ROLL)
                elif row_idx < num_rows - 1:
                    # Bottom row has no bottom-right neighbour
                    adjacent_rolls += (rows[row_idx + 1][cell_idx + 1] != CELL_ROLL)

                adjacent_rolls += (rows[row_idx][cell_idx + 1] != CELL_ROLL)

            # Middle column
            if row_idx > 0:
                # Top row has no top neighbour
                adjacent_rolls += (rows[row_idx - 1][cell_idx] != CELL_ROLL)

            if row_idx < num_rows - 1:
                # Bottom row has no bottom neighbour
                adjacent_rolls += (rows[row_idx + 1][cell_idx] != CELL_ROLL)

            if adjacent_rolls < 4:
                # Mark the roll for removal on next iteration
                rows[row_idx][cell_idx] = CELL_REMOVABLE
                rolls_removable += 1

            # Delete "removable" cells from rows 1..N
            if row_idx > 0:
                # 2nd to n-1 rows - remove rolls from the top row
                if cell_idx > 0:
                    if rows[row_idx - 1][cell_idx - 1] == CELL_REMOVABLE:
                        rows[row_idx - 1][cell_idx - 1] = CELL_EMPTY

                    if cell_idx == num_cells - 1:
                        # Last cell in the row - update cell immediately above
                        if rows[row_idx - 1][cell_idx] == CELL_REMOVABLE:
                            rows[row_idx - 1][cell_idx] = CELL_EMPTY

                if row_idx == num_rows - 1:
                    # Bottom row - Remove rolls to the left
                    if cell_idx > 0:
                        if rows[row_idx][cell_idx - 1] == CELL_REMOVABLE:
                            rows[row_idx][cell_idx - 1] = CELL_EMPTY

                        if cell_idx == num_cells - 1:
                            # Last cell in the row - update self
                            if rows[row_idx][cell_idx] == CELL_REMOVABLE:
                                rows[row_idx][cell_idx] = CELL_EMPTY

    return rolls_removable, rows

if __name__ == "__main__":
    main()
