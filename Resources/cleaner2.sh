for dir in $(ls filterLists)
do

	mv filterLists/$dir/$(ls filterLists/$dir) filterLists/$dir/$dir.txt
#	if [[ $(ls filterLists/$dir) == *"\'"* ]]
#	then
#		echo $(ls filterLists/$dir)
#	fi
done

