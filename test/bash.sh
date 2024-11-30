#!/bin/sh

# Variables
HADOOP_STREAMING_JAR="/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar"
INPUT_DIR="input"
OUTPUT_DIR="output"
MAPPER_SCRIPT="mapper.py"
REDUCER_SCRIPT="reducer.py"
POST_PROCESS_SCRIPT="postprocess.py"

#rm extracted/*
#python3 download_pdf.py
#python3 pdfextract.py

hdfs dfs -rm /user/joy/input/*
hdfs dfs -put extracted/* /user/joy/input/



# Step 1: Remove old output directory (if exists)
hdfs dfs -rm -r -f /user/joy/$OUTPUT_DIR
#hdfs dfs -rm -r -f /user/hadoopuser/$INPUT_DIR
#hdfs dfs -mkdir /user/hadoopuser/input
#hdfs dfs -put input/* /user/hadoopuser/input
# Step 2: Run Hadoop Streaming job
start=$(date +%s)

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
-D mapreduce.input.fileinputformat.input.dir.recursive=true \
-files /home/joy/nltk_data/ \
-file  mapper.py -mapper mapper.py \
-file  reducer.py -reducer reducer.py \
-input input -output output

end=$(date +%s)
duration=$((end - start))
echo "Time taken: $duration seconds"

rm -r output
#Step 3: Copy Hadoop output from HDFS to local
hdfs dfs -get /user/joy/$OUTPUT_DIR .

# Step 4: Run the post-processing script
python3 $POST_PROCESS_SCRIPT
