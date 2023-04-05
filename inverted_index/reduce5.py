#!/usr/bin/env python3
"""REDUCE: Calculate normalization factor"""
# working on it copied from job3
import sys
import itertools
import math
# document_id[TAB]term tf nk idf w


def reduce_one_group(key, group):
    """Reduce one group."""
    gps = list(group)
    sum = 0
    for line in gps:
        # document_id[TAB]term tf nk idf w
        line = line.strip('\n')
        line = line.split("\t")
        line = " ".join(line)
        line = line.split(" ")
        line.pop(0)
        w = line[5]
        d = float(w) ** 2
        sum += d
        # print("my curr sum:", sum)
    for line in gps:
        # making it space separated
        # also we do not need nk yes yes
        line = line.strip("\n")
        line = line.split("\t")
        line = " ".join(line)
        line = line.split(" ")
        line.pop(0)
        docid = line[0]
        term = line[1]
        tf = line[2]
        idf = line[4]

        print(f'{term} {idf} {docid} {tf} {sum}')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    # document_id
    return line.split("\t")[1].split()[0]

# command for entire pipeline madoop:
# ./inverted_index/pipeline.sh inverted_index/example_input


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
