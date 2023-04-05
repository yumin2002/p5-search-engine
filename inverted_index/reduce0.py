#!/usr/bin/env python3

"""REDUCE Count Document number: N"""

import sys


def main():
    """Divide sorted lines into groups that share a key."""
    count = 0
    for i in sys.stdin:
        count += 1

    print(count)


if __name__ == "__main__":
    main()
