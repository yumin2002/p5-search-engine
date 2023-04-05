#!/usr/bin/env python3
"""MAP for calculate nk(number of documents containing the term)"""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    gps = list(group)
    # print(gps)
    word_count = len(gps)

    for line in gps:
        # print("Everything in the group : ", line)
        # for i in group:
        #     print(i)
        # count = line.split(" ")[2]
        # word_count += 1
        line = line.strip('\n')
    print(f"{line} {word_count}")
    # print(f"{line} {word_count}")0


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    # 1 mike 1 3
    return line.partition(" ")[0]


def main():
    l = sorted(list(sys.stdin))
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(l, keyfunc):
        # print(group)
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
