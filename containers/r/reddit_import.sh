#!/bin/bash
pg_ctl -D /nfsscratch/tph_myth/reddit_db -l logfile start
for i in /nfsscratch/tph_myth/data_sets/reddit_10-2007_03-2015/*
do
    filename=$(basename "$i")
    echo "== working on $filename"
    cat $i | sed 's/\\\+u0000//g'\
           | sed 's,\\,\\\\,g'\
           | psql -h localhost -p 5432 --username=acambre\
                  -c "COPY reddit (comment) FROM STDIN;" reddit
    echo "doing something with $filename"
done
pg_ctl -D /nfsscratch/tph_myth/reddit_db stop

