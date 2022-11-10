# Task 2. Working with files
import pandas as pd
from tabulate import tabulate
import os

# Part 1
print('Part 1')


def pollutantmean(directory, pollutant, ids):
    if isinstance(ids, int):
        ids = [ids]
    file = pd.concat([pd.read_csv('data/' + directory + '/' + format(i, "03d") + ".csv") for i in ids])
    mean = file[pollutant].mean()
    return mean


print(pollutantmean('specdata', 'sulfate', range(1, 11)))
print(pollutantmean('specdata', 'nitrate', range(70, 73)))
print(pollutantmean('specdata', 'nitrate', 23))

# Part 2
print("Part 2")


def complete(directory, ids):
    if isinstance(ids, int):
        ids = [ids]
    result_data = []
    for i in ids:
        file = pd.read_csv('data/' + directory + '/' + format(i, "03d") + ".csv").dropna()
        result_data.append([i, len(file.index)])
    col_names = ["id", "nobs"]
    print(tabulate(result_data, headers=col_names))


complete('specdata', 1)
complete('specdata', [2, 4, 8, 10, 12])
complete('specdata', range(30, 24, -1))

# Part 3
print("Part 3")


def corr(directory, threshold):
    files = [pd.read_csv('data/' + directory + "/" + file).dropna() for file in os.listdir('data/' + directory)]
    corrs = []
    for file in files:
        if len(file.index) > threshold:
            corrs.append(file['sulfate'].corr(file['nitrate']))
    return corrs


print(corr('specdata', 150))
print(corr('specdata', 400))
print(corr('specdata', 5000))
