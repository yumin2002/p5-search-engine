#!/usr/bin/env python3
"""Doc string."""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    word_count = 0
    for line in group:
        count = line.split("\t")[1]
        word_count += int(count)
    print(f"{key} {word_count}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.split("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
