#!/usr/bin/env python3
"""REDUCE: Calculate normalization factor"""
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
        line.pop(0)
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
        line.pop(0)
        docid = line[0]
        term = line[1]
        tf = line[2]
        idf = line[4]
        # HALO correct now
        # 好耶！！
        # Ithink it is working correctly?
        # you can take a look at output6
        # document_id[TAB]term tf nk idf w
        # term idf docid tf norm-f
        # lets just partition it now and we should be done
        # partition? like dividing it into 3 docs by making the key in map 6 docid%3
        # I have done that part, now output 6 is 3 files,  oghhhh thats why you pop0 nice nice AMAZING
        # xixi hhhhhhhhh
        # I might need to clean our conversation and test it QWQ
        # don wanna clean up

        print(f'{term} {idf} {docid} {tf} {sum}')
        # we also need to take out the nk and those stuff
        # I think just nK? we should't need w either ohhh right
        # final out should look like: term idf docid tf norm-f
# + madoop -input output5 -output output6 -mapper ./inverted_index/map5.py -reducer ./inverted_index/reduce6.py
# Error: Failed executable test: Command '/Users/yuhanmin/Desktop/485p5/inverted_index/reduce6.py' returned non-zero exit status 127.
# just got this error
# looks nice now
# output exactly the same as example
# our big one has some issue for running ./inverted_index/pipeline.sh inverted_index/input
# the output does not match 
# can you paste output here# #
# 0000noemalife 22003515 1 1 0.47712125471966244 0.47712125471966244 0.47712125471966244 0.47712125471966244
# 005800x600jpgthe 1675507 1 1 0.47712125471966244 0.47712125471966244 0.47712125471966244 0.47712125471966244
# lemme verify each stage

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

# current looks totallly correct


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    # document_id
    return line.split("\t")[1].split()[0]

# command for entire pipeline madoop:
# ./inverted_index/pipeline.sh inverted_index/example_input


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
