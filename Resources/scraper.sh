for line in $(cat list_filters.csv | tr ' ' '_' )
do
	filterLists="filterLists/"
	dir=$(echo $line | tr '.' '_' | tr '/' '_'| sed -e 's/\([^\;]*\)\;.*/\1/')
	#echo "$dir"
	echo $(echo $line | sed -e 's/.*;\([^;]*\)/\1/')
	curl -k $(echo $line | sed -e 's/.*;\([^;]*\)/\1/') -o $filterLists$dir/$dir.txt
done

# dir creation kdir `cat list_filters.csv | sed -e 's/\([^\;]*\)\;.*/\1/' | tr ' ' '_' | tr '.' '_' | tr '/' '_' | sed -e 's/\(.*\)/filterLists\/\1/'`
