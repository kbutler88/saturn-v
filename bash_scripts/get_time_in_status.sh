#!/bin/bash -x

var1=""
var2=""
#SGD=$(echo '{"id": "123"}' | jq -r '. | select(.id == "999")')
SGD=$(echo '{"id": "123"}' | jq -r '. | select(.id == "123")')

for TEXT in $(echo "In Progress=2024-03-01T14:00:00;In Review=2024-03-05T03:40:00;In Progress=2024-03-07T10:30:00;On Hold=2024-03-07T21:00:00" | sed 's/ //g' | tr ';' '\n'); do
	var2=$var1
	var1=$(echo $TEXT | cut -d= -f2)
	status=$(echo $TEXT | cut -d= -f1)
	# Must load var2 before performing first calculation
	if [ "$var2" != "" ]; then
		# Debugging
		#echo "var2 = $var2"
		#echo "var1 = $var1"
		
		# Convert date to Unix time
		date1=$(date -d "$var1" +%s)
		date2=$(date -d "$var2" +%s)
		
		# Calculate the difference
		diff=$(($date1 - $date2))
		# Calculate the number of days, hours, and mins
		echo "  Days:   $(($diff / 86400))"
		echo "  Hours:  $((($diff % 86400) / 3600))"
		echo "  Mins:   $((($diff % 3600) / 60))"
	fi
	# echo status here so the time reflects the correct status time
	echo "STATUS: $status"
done

# As long as the status isn't empty and the status is not "Done"
if [ "$SGD" != "" -a "$status" != "Done" ]; then
	echo "I am in"
fi
