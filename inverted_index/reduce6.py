#!/usr/bin/env python3
"""REDUCE: Calculate normalization factor"""
import sys
import itertools
import math
# document_id[TAB]term tf nk idf w


def reduce_one_group(key, group):
    """Reduce one group."""
    gps = list(group)
    term = ""
    idf = ""
    myline = []
    for line in gps:
        # document_id[TAB]term tf nk idf w
        line = line.strip('\n')
        line = line.split("\t")[1]
        line = line.split()
        term = line[0]
        idf = line[1]
        myline = myline + line[2:]

    print(f'{term} {idf} {" ".join(myline)}')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    # document_id
    return line.split("\t")[1].split()[0]

# ./inverted_index/pipeline.sh inverted_index/example_input


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
