"""
Advent of Code 2021
Sean Solomon
DAY 2
"""

import sys

def collect_data(fname):
    with open(fname, "r") as f:
        all_lines = f.readlines()
    f.close()
    
    instructions = {"forward": 0, "down": 0, "up": 0}
    for line in all_lines:
        line = line.strip()
        if "forward" in line:
            instructions["forward"] += int(line[8:])
        elif "down" in line:
            instructions["down"] += int(line[5:])
        else:
            instructions["up"] += int(line[3:])
    
    return instructions

def calculate_total(data):
    net_total = data["down"] - data["up"]
    return net_total * data["forward"] 

def calculate_aim(fname):
    with open(fname, "r") as f:
        all_lines = f.readlines()
    f.close

    aim = depth = pos = 0
    for line in all_lines:
        line = line.strip()
        if "forward" in line:
            x = int(line[8:])
            pos += x
            depth += (aim * x)
        elif "down" in line:
            aim += int(line[5:])
        else:
            aim -= int(line[3:])

    return depth * pos

def main():
    direction_dict = collect_data(sys.argv[1])
    result1 = calculate_total(direction_dict)
    result2 = calculate_aim(sys.argv[1])

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")
    
if __name__ == "__main__":
    main()
