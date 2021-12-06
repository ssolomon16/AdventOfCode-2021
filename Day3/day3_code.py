"""
Advent of Code 2021
Sean Solomon
DAY 3
"""

import sys
import pandas as pd

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

def oxygen_rating(df):
    for col in df:
        try:
            if len(df) == 1:
                return df
            num_zeros = df[col].value_counts()[0]
            num_ones = df[col].value_counts()[1]

            if num_ones >= num_zeros:
                df = df[df[col] == 1]
            else:
                df = df[df[col] == 0]
        
        except:
            continue

    return df

def co2_rating(df):
    for col in df:
        try:
            if len(df) == 1:
                return df
            num_zeros = df[col].value_counts()[0]
            num_ones = df[col].value_counts()[1]

            if num_ones < num_zeros:
                df = df[df[col] == 1]
            else:
                df = df[df[col] == 0]

        except:
            continue
    
    return df

def main():
    df = collect_data(sys.argv[1])
    gamma_binary = calculate_gamma(df)
    epsilon_binary = calculate_epsilon(gamma_binary)
    
    gamma = int(gamma_binary, 2)
    epsilon = int(epsilon_binary, 2)

    o2 = oxygen_rating(df).to_string(index=False, header=False)
    co2 = co2_rating(df).to_string(index=False, header=False)
    o2 = o2.replace(" ", "")
    co2 = co2.replace(" ", "") 

    print(f"Multipled = {int(o2, 2) * int(co2, 2)}")

if __name__ == "__main__":
    main()
