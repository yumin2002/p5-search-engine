#!/usr/bin/env python3
"""REDUCE: Calculate normalization factor."""
import sys
import itertools
# document_id[TAB]term tf nk idf w


def reduce_one_group(group):
    """Reduce one group."""
    gps = list(group)
    my_sum = 0
    for line in gps:
        # document_id[TAB]term tf nk idf w
        line = line.strip('\n')
        line = line.split("\t")
        line = " ".join(line)
        line = line.split(" ")
        line.pop(0)
        my_w = line[5]
        my_d = float(my_w) ** 2
        my_sum += my_d
    for line in gps:
        line = line.strip("\n")
        line = line.split("\t")
        line = " ".join(line)
        line = line.split(" ")
        line.pop(0)
        docid = line[0]
        term = line[1]
        term_freq = line[2]
        idf = line[4]
        print(f'{term} {idf} {docid} {term_freq} {my_sum}')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    # document_id
    return line.split("\t")[1].split()[0]

# ./inverted_index/pipeline.sh inverted_index/example_input


def main():
    """Divide sorted lines into groups that share a key."""
    for key_group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key_group[1])


if __name__ == "__main__":
    main()
