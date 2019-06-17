#!/bin/bash



wget -H -nc -np -nH --cut-dirs=1 -A .html -e robots=off -l1 -i ../search.csv -B 'http://archive.org/download/'


find . -type f -name "usenet*" -exec sh -c "grep zip {} | cut -d'\"' -f2" \; > sub_newsgroups.txt

while read line 
	do
	baseurl='http://archive.org/download/usenet-'
	subgroup=${line%%\.*zip}

	url="${baseurl}${subgroup}/${line}"

	wget -nc $url

done <sub_newsgroups.txt
