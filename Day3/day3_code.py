"""
Advent of Code 2021
Sean Solomon
DAY 3
"""

import sys
import pandas as pd

"""
data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data)
"""

def collect_data(fname):
    with open(fname, "r") as f:
        all_lines = f.readlines()
    f.close

    cols = "ABCDEFGHIJKL"
    data = {key:[] for key in cols}
    for line in all_lines:
        line = line.strip()
        pos = 0
        for num in range(len(line)):
            to_add = int(line[num])
            key = cols[pos]
            data[key].append(to_add)
            pos += 1

    df = pd.DataFrame.from_dict(data)
    return df

def calculate_gamma(df):
    binary_str = ""
    for col in df:
        binary_str += df[col].mode().to_string(index=False)
    
    return binary_str

def calculate_epsilon(gamma):
    binary_str = ""
    for num in gamma:
        if num == "1":
            binary_str += "0"
        else:
            binary_str += "1"
    
    return binary_str

def main():
    df = collect_data(sys.argv[1])
    gamma_binary = calculate_gamma(df)
    epsilon_binary = calculate_epsilon(gamma_binary)
    
    gamma = int(gamma_binary, 2)
    epsilon = int(epsilon_binary, 2)

    print(f"Product of gamma and epsilon is {gamma * epsilon}")    

if __name__ == "__main__":
    main()