for line in $(cat list_filters.csv)
do
	dir="filterLists/"`echo $line | sed -e 's/\([^\;]*\)\;.*/\1/' | tr ' ' '_' | tr '.' '_' | tr '/' '_'`
	echo "$dir"
	#wget $(echo $line | sed -e 's/.*;\([^;]*\)/\1/')
done
