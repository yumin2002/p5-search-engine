#!/usr/bin/env python3
"""REDUCE: Calculate normalization facor"""
# working on it copied from job3
import sys
import itertools
import math
# HALO now map is correct as the following
# document_id[TAB]term tf nk idf w


def reduce_one_group(key, group):
    """Reduce one group."""
    gps = list(group)
    sum = 0
    for line in gps:
        # document_id[TAB]term tf nk idf w
        line = line.strip('\n')
        line = line.split("\t")
        line = " ".join(line)
        line = line.split(" ")
        w = line[5]
        d = float(w) ** 2
        sum += d
        # print("my curr sum:", sum)
    for line in gps:
        # making it space separated
        # also we do not need nk yes yes
        line = line.strip("\n")
        line = line.split("\t")
        line = " ".join(line)
        line = line.split(" ")
        docid = line[0]
        term = line[1]
        tf = line[2]
        idf = line[4]

        # document_id[TAB]term tf nk idf w
        # term idf docid tf norm-f

        print(f'{term} {idf} {docid} {tf} {sum}')
        # we also need to take out the nk and those stuff
        # I think just nK? we should't need w either ohhh right
        # final out should look like: term idf docid tf norm-f

        # i think i found how to segment
        # To produce segments that match the instructor solution,
        # the last map.py should output doc_id % 3 as the key.
        # i think its determined based on the key in map stage
        # cuz map should produce key-val pair
        # so we might be able to just write another map that produce docid%3 : our original line
        # great idea
        # let me commit the current version
        # maybe also test maddoop
        
# map command:
# cat inverted_index/example_input/input.csv | inverted_index/map1.py | sort | inverted_index/reduce1.py | inverted_index/map2.py | sort | inverted_index/reduce2.py | inverted_index/map3.py | sort | inverted_index/reduce3.py | inverted_index/reduce4.py | inverted_index/map5.py > out
# reduce command for this stage:
# cat inverted_index/example_input/input.csv | inverted_index/map1.py | sort | inverted_index/reduce1.py | inverted_index/map2.py | sort | inverted_index/reduce2.py | inverted_index/map3.py | sort | inverted_index/reduce3.py | inverted_index/reduce4.py | inverted_index/map5.py | inverted_index/reduce5.py > out


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    # document_id
    return line.split("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
