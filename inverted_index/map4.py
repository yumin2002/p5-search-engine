#!/usr/bin/env python3
"""MAP: Calculate idf and w."""
import sys
import csv

csv.field_size_limit(sys.maxsize)

lines = sys.stdin

for line in lines:  # sys.stdin.readlines():
    if line == "\n":
        continue
    print(line.strip("\n"))
