#!/usr/bin/env python3
"""MAP: Sort by term."""
import sys
import csv

csv.field_size_limit(sys.maxsize)

lines = sys.stdin

for line in lines:  # sys.stdin.readlines():
    # hello document tf nk idf w
    if line == "\n":
        continue
    line = line.strip("\n")
    cols = line.split()
    print(f'{int(cols[2])%3}\t{" ".join(cols)}')
