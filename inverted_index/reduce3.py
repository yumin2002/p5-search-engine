#!/usr/bin/env python3
"""MAP for calculate nk(number of documents containing the term)"""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    word_count = 0
    for line in group:
        print("Everything in the group : ", group)
        # for i in group:
        #     print(i)
        # count = line.split(" ")[2]
        word_count += 1
        line = line.strip('\n')
        print(f"{line} {word_count}")
    # print(f"{line} {word_count}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    # 1 mike 1 3
    print(line.split(" ")[1])
    return line.split(" ")[1]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
