#!/bin/bash

n=$(wc -l sub_newsgroups.txt | cut -d' ' -f1)
dir_from="/nfsscratch/tph_myth/data_sets/usenet_data"
dir_to="/nfsscratch/tph_myth/data_sets/usenet_data"

for i in $(seq 0 ${n})
do
    line=$((${i}+1))
    file_name=$(head -${line} sub_newsgroups.txt | tail -1 | sed -r 's/.mbox.zip//')
    file_from="${dir_from}/${i}.pickle"
    file_to="${dir_to}/${file_name}.pickle"
    if [ -f ${file_from} ]
    then
        mv ${file_from} ${file_to}
    fi
done

