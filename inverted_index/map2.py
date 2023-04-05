#!/usr/bin/env python3
"""MAP for count tf in document d"""
import sys
import csv

csv.field_size_limit(sys.maxsize)

lines = sys.stdin
sys.stdin = open("/dev/tty")  # Temporary addition

# 1 document document mike made cool

for line in lines:  # sys.stdin.readlines():
    if line == "\n":
        continue
    # convert document document mike made cool to
    words = line.split()
    docID = words[0]
    for w in words[1:]:
        # print(docID, w, 1)
        print(f'{docID} {w}\t1')
