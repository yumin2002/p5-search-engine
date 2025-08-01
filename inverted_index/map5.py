#!/usr/bin/env python3
"""MAP: Calculate normalization factor."""
import sys
import csv

csv.field_size_limit(sys.maxsize)

lines = sys.stdin

for line in lines:  # sys.stdin.readlines():
    # hello document tf nk idf w
    # document[TAB]hello tf nk idf w
    if line == "\n":
        continue
    line = line.strip("\n")
    cols = line.split()
    temp = cols[0]
    cols[0] = cols[1]
    cols[1] = temp
    print(f'{int(cols[0]) % 3}\t{" ".join(cols)}')
