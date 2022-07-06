#!/bin/bash
n=0

for dir in $(ls filterLists) 
do
	if [ -z $(ls filterLists/$dir) ]
	then
		echo $dir
		((n=n+1))
	elif [[ $(head -n1 filterLists/$dir/* | tr ' ' '_') == "404:_Not_Found" ]]
	then
		echo "$dir 404"
		rm filterLists/$dir/*
		((n=n+1))
	fi
done
echo $n

