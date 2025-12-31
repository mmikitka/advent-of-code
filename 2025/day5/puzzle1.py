import re
import sys

def main():
    fresh_id_ranges = []
    in_ranges_section = True
    num_fresh = 0
    with open(sys.argv[1], "r") as f:
        for line in f:
            if in_ranges_section:
                range = process_range_line(line.rstrip())
                if range is not None:
                    fresh_id_ranges.append(range)
                else:
                    in_ranges_section = False
            else:
                num_fresh += (1 if process_ingredient_line(line.rstrip(), fresh_id_ranges) else 0)

    print(f"Number of fresh ingredients = {num_fresh}")

def process_range_line(line):
    match = re.match(r"^(\d+)\-(\d+)$", line)
    if match is None:
        return None
    return (int(match.group(1)), int(match.group(2)))

def process_ingredient_line(line, fresh_id_ranges):
    ingredient_id = int(line)
    for (start_id, end_id) in fresh_id_ranges:
        if ingredient_id >= start_id and ingredient_id <= end_id:
            return True
    return False

if __name__ == "__main__":
    main()
