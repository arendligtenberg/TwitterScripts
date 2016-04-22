#!/bin/bash
while true; do
	python Livetweeter-2.py 
	now=$(date)
	echo "OOPS CRASHED: respawning: $now" >> tweetapicrashes.txt
done
