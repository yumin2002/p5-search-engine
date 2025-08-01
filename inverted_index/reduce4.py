#!/usr/bin/env python3
"""REDUCE: Calculate idf and w."""
import sys
import math


def reduce_one_group(line, total_doc):
    """Reduce one group."""
    line = line.strip('\n')
    # hello document tf nk
    line = line.split(" ")
    # hello document tf nk idf w
    idf = math.log10(int(total_doc)/int(line[3]))
    w_param = idf * int(line[2])
    line = " ".join(line)
    print(f"{line} {idf} {w_param}")


# def keyfunc(line):
#     """Return the key from a TAB-delimited key-value pair."""
#     print(line.split(" ")[0])
#     return line.split(" ")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    total_doc = 0
    with open("total_document_count.txt", "r", encoding="utf-8") as file:
        total_doc = int(file.readline().strip("\n"))
        # print(total_doc)
    for line in sys.stdin:
        # print(line)
        reduce_one_group(line, total_doc)


if __name__ == "__main__":
    main()
