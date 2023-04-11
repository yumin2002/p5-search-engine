#!/usr/bin/env python3
"""MAP for calculate nk(number of documents containing the term)."""
import sys
import csv

csv.field_size_limit(sys.maxsize)

lines = sys.stdin

# 1 document document mike made cool

for line in lines:  # sys.stdin.readlines():
    if line == "\n":
        continue
    line = line.strip()
    cols = line.split()
    temp = cols[0]
    cols[0] = cols[1]
    cols[1] = temp
    print(f'{cols[0]}\t{" ".join(cols[1:])}')
