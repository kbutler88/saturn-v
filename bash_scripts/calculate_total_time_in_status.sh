#!/bin/bash
# This script groups the matching statuses and adds the time.
# It also requires recalculating the minutes and hours to display correctly.
# Over 60 minutes adds to hours; over 24 hours adds to days.

MYDATA="ToDo:10 Days;3 Hrs;42 Mins|InProgress:0 Days;21 Hrs;0 Mins|InReview:0 Days;0 Hrs;45 Mins|InProgress:2 Days;23 Hrs;22 Mins|InReview:2 Days;4 Hrs;24 Mins|Done"

for THISSTATUS in $(echo "ToDo"; echo $MYDATA | tr "|" "\n" | sort | grep -Ev "Done|ToDo" | cut -d: -f1 | uniq); do
	DAYS=0
	MINS=0
	HRS=0
	for TEMPDAYS in $(echo $MYDATA | tr "|" "\n" | grep "$THISSTATUS" | cut -d: -f2 | cut -d\; -f1 | cut -d" " -f1); do
		DAYS=$(( $TEMPDAYS + $DAYS ))
	done
	for TEMPHRS in $(echo $MYDATA | tr "|" "\n" | grep "$THISSTATUS" | cut -d: -f2 | cut -d\; -f2 | cut -d" " -f1); do
		HRS=$(( TEMPHRS + $HRS ))
	done
	for TEMPMINS in $(echo $MYDATA | tr "|" "\n" | grep "$THISSTATUS" | cut -d: -f2 | cut -d\; -f3 | cut -d" " -f1); do
                MINS=$(( $TEMPMINS + $MINS ))
        done
	echo "$THISSTATUS Total:$DAYS Days;$HRS Hrs;$MINS Mins"
done
