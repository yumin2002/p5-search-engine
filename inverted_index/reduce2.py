#!/usr/bin/env python3
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    word_count = 0
    for line in group:
        count = line.split(" ")[2]
        word_count += int(count)
    print(f"{key} {word_count}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.split(" ")[0] + " " + line.split(" ")[1]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
