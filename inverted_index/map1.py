#!/usr/bin/env python3
"""MAP Clean String."""
import sys
import csv
import re

csv.field_size_limit(sys.maxsize)

sws = []

with open("stopwords.txt", 'r', encoding="utf-8") as stopwords:
    lines = stopwords.readlines()
    sws = [s.strip('\n') for s in lines]

lines = sys.stdin.readlines()

for line in lines:
    # Combine both document title and document body
    # by concatenating them, separated by a space.
    # print(line+'\n')
    if line == "\n":
        continue
    line = csv.reader([line])
    data = []
    for row in line:
        data.append(row)
        # print(row)
    # Remove non-alphanumeric characters (that also aren’t
    # spaces) like this:
    # import re
    text = data[0][1] + ' ' + data[0][2]
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", text)
    text = text.casefold()
    # print(text)

    words = text.split()
    # print(words)
    res = [w for w in words if w not in sws]
    # print(res)
    print(f"{data[0][0]} {' '.join(res)}")

    # The inverted index should be case insensitive. Convert
    # upper case characters to lower case using casefold().

    # Split the text into whitespace-delimited terms.
    # Remove stop words. We have provided a list of stop words
    # in inverted_index/stopwords.txt.
