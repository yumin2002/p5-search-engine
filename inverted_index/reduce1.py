#!/usr/bin/env python3
"""
REDUCE0 Clean strings
"""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    word_count = 0
    for line in group:
        count = line.partition("\t")[2]
        word_count += int(count)
    print(f"{key}\t{word_count}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line


def main():
    """Divide sorted lines into groups that share a key."""
    # for key, group in itertools.groupby(sys.stdin, keyfunc):
    #     breakpoint()
    #     print(key)

    lines = sys.stdin.readlines()
    
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
