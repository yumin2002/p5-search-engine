#!/usr/bin/env python3
"""MAP for calculate nk(number of documents containing the term)."""
import sys
import itertools


def reduce_one_group(group):
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
    sort_l = sorted(list(sys.stdin))
    for key_group in itertools.groupby(sort_l, keyfunc):
        reduce_one_group(key_group[1])


if __name__ == "__main__":
    main()
