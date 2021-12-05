"""
Advent of Code 2021
Sean Solomon
DAY 1
"""

import sys

def to_list(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    f.close()
    clean_lines = list(map(lambda x: int(x.strip()), lines))
    return clean_lines

def get_increases(data):
    count = 0
    for i in range(len(data) - 1):
        if data[i+1] > data[i]:
            count += 1
    return count

def window_increases(data):
    count = 0
    for i in range(len(data) - 3):
        first = sum(data[i:i+3])
        second = sum(data[i+1:i+4])
        if second > first:
            count += 1
    return count

def main():
    nums = to_list(sys.argv[1])
    results1 = get_increases(nums)
    results2 = window_increases(nums)

    print(f"Part 1: {results1}")
    print(f"Part 2: {results2}")

if __name__ == "__main__":
    main()