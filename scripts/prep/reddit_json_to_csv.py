#!/usr/bin/env python3

import sys, pandas
from usenet_clean import *

def clean_text(text):
    try:
        text = find_replace_url(text)
    except:
        text = text
    text = text = " ".join(text.split())
    return text

#Reads in JSON file

filename = sys.argv[1]
df = pandas.read_json(filename, lines=True)

#Drops columns not in the keepcols list
#Should handle messages/files that don't have all the columns

keepcols = ['id', 'subreddit', 'downs', 'body', 'subreddit_id','created_utc', 'parent_id', 'ups', 'link_id']
df.drop(df.columns.difference(keepcols), 1, inplace=True)

#Drops rows that contain NSFW in either the subreddit or body text

df = df[~df.subreddit.str.contains("NSFW")]
df = df[~df.body.str.contains("NSFW")]

#Encrypts the urls and cleans whitespace

df["body"] = df["body"].map(lambda body: clean_text(body))

#Exports to filename.tsv

df.to_csv(filename+'.tsv',sep='\t',encoding='utf-8')

