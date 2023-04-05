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

# Job 0
madoop \
  -input ${PIPELINE_INPUT} \
  -output output0 \
  -mapper ./map0.py \
  -reducer ./reduce0.py

mv output0/part-00000 total_document_count.txt

# Job 1
madoop \
  -input ${PIPELINE_INPUT} \
  -output output1 \
  -mapper ./map1.py \
  -reducer ./reduce1.py

# Job 2
madoop \
  -input output1 \
  -output output2 \
  -mapper ./map2.py \
  -reducer ./reduce2.py


madoop \
  -input output2 \
  -output output3 \
  -mapper ./map3.py \
  -reducer ./reduce3.py


madoop \
  -input output3 \
  -output output4 \
  -mapper ./map4.py \
  -reducer ./reduce4.py



madoop \
  -input output4 \
  -output output5 \
  -mapper ./map5.py \
  -reducer ./reduce5.py

# but first I need to remname those files
# which files


# madoop concated all the occurance into the same line
# ummm weird u
# reconvenedmeans 4422313 1 1 0.47712125471966244 0.47712125471966244 0.47712125471966244 0.47712125471966244
# reconstruction 3987467 4 67 -1.348953547981164 -5.395814191924656 -1.348953547981164 -5.395814191924656

# term idf (docid tf norm-f)
# our output looks fine, is it because we strip the new line?
# 4422313 doesn't look like an idf
# can you paste the command to run the test here
# ./inverted_index/pipeline.sh inverted_index/input 
# i was juct checking the big input
# I was trying to run the pytest and get the following error
#         # Verify inverted index file are copied to
#         # ./index_server/index/inverted_index
#         inverted_index_dir = Path("index_server/index/inverted_index")
# >       assert inverted_index_dir.is_dir()
# E       AssertionError: assert False
# E        +  where False = <bound method Path.is_dir of PosixPath('index_server/index/inverted_index')>()
# E        +    where <bound method Path.is_dir of PosixPath('index_server/index/inverted_index')> = PosixPath('index_server/index/inverted_index').is_dir

# tests/test_pipeline_public.py:359: AssertionError

# HALO WENQIAN, where did you find the sample output?
# sample output? for which files?
# for the input (large)
# i think the error disapper if the shell scipt is correct
# let me trytry
# i dont think there is sample output
