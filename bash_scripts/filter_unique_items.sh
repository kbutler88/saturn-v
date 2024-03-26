#!/bin/bash

STRING="ToDo
InProgress
InReview
InProgress
OnHold
InProgress
InReview
Done"

# Associative array
declare -A UNIQUE_ITEMS_ORDER
# Normal array
UNIQUE_ITEMS=()

while IFS= read -r line; do
	# Check if the line does not exist in the associative array
	if [[ ! "${UNIQUE_ITEMS_ORDER[$line]}" ]]; then
		# Assign a value for the "line" to add it to the Associative array
		UNIQUE_ITEMS_ORDER["$line"]=1
		# Add the line to the array in the order that it was first encountered
		UNIQUE_ITEMS+=("$line")
	fi
done <<< $(echo $STRING | tr " " "\n" | grep -v "Done")
# The line above ensures that spaces are converted to line returns and removes the Done status

# List all the items that were added to the normal array
for item in "${UNIQUE_ITEMS[@]}"; do
	echo "$item"
done
