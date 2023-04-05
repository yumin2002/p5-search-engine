#!/bin/bash
#
# Example of how to chain MapReduce jobs together.  The output of one
# job is the input to the next.
#
# Hadoop (or Madoop) options
# jar index/hadoop/hadoop-streaming-2.7.2.jar   # Hadoop configuration
# -input <directory>                            # Input directory
# -output <directory>                           # Output directory
# -mapper <exec_name>                           # Mapper executable
# -reducer <exec_name>                          # Reducer executable

# Stop on errors
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail

# Optional input directory argument
PIPELINE_INPUT=input
if [ -n "${1-}" ]; then
  PIPELINE_INPUT="$1"
fi

# Print commands
set -x

# Remove output directories
rm -rf output output[0-9]



# Job 1
madoop \
  -input ${PIPELINE_INPUT} \
  -output output1 \
  -mapper ./inverted_index/map1.py \
  -reducer ./inverted_index/reduce1.py

# Job 2
madoop \
  -input output1 \
  -output output2 \
  -mapper ./inverted_index/map2.py \
  -reducer ./inverted_index/reduce2.py


madoop \
  -input output2 \
  -output output3 \
  -mapper ./inverted_index/map3.py \
  -reducer ./inverted_index/reduce3.py


madoop \
  -input output3 \
  -output output4 \
  -mapper ./inverted_index/map4.py \
  -reducer ./inverted_index/reduce4.py


madoop \
  -input output4 \
  -output output5 \
  -mapper ./inverted_index/map4.py \
  -reducer ./inverted_index/reduce4.py

madoop \
  -input inverted_index/output5 \
  -output inverted_index/output6 \
  -mapper inverted_index/map5.py \
  -reducer inverted_index/reduce5.py
