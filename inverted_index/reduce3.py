#!/usr/bin/env python3
"""MAP for calculate nk(number of documents containing the term)"""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    gps = list(group)
    word_count = len(gps)
    for line in gps:
        line = line.strip('\n')
        line = line.split("\t")
        line = " ".join(line)
        print(f"{line} {word_count}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.split("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
