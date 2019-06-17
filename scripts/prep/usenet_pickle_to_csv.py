#!/usr/bin/env python3

import sys, os, glob, pickle, csv

extract_directory = sys.argv[1]
pickles = glob.glob(os.path.join(extract_directory, "*.pickle"))

keylist = ["Date", "X-Google-Language", "Subject", "Newsgroup", "Organization", "Body"]

with open(os.path.join(extract_directory, extract_directory + ".csv"), 'w') as csv_file:
    writer = csv.DictWriter(csv_file, keylist, delimiter = '\t')
    writer.writeheader()
    for p in pickles:
        with open(p, 'rb') as f:
            data = pickle.load(f)
            for d in data:
                d['Body'] = " ".join(d['Body'].split())
                writer.writerow(d)

