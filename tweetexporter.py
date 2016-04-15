#!/usr/bin/python

# Arend Ligtenberg / Wageningen University / Jan. 2013
# simpel scriptje om even snel postgres records te exporteren naar tab delim. file

import string, json, pprint
from datetime import datetime
import string, os, sys, subprocess, time
import psycopg2

dt_postfix = datetime.now().strftime("%Y%m%d-%H%M%S")
output_file = "export_result_"+dt_postfix+".csv"

#open file for output
target = open(output_file,"w")

# Connect to the twitter database
conn = psycopg2.connect("dbname=gis user=postgres password=Entrada001")

# Open a cursor to perform database operations
cur = conn.cursor()

#             where (longitude > 4.76326 AND longitude < 5.033112) and (latitude > 52.295042 AND latitude < 52.431065)"""

query = """Select
             tweet_id,
             tweet_text,
             tweet_datetime,
             latitude,
             longitude,
             tweet_name from geotweets"""
#where (longitude > 4.76326 AND longitude < 5.033112) and (latitude > 52.295042 AND latitude < 52.431065)
print "Starting query..."
cur.execute(query)
print "done query"
number_of_rows = cur.rowcount

print "start writing to file..."
count = 0.0
for row in cur.fetchall():
    output_string = "%s \t %s \t %s \t  %s \t %f \t %f \n" % (row[0],row[1],row[2],row[5], row[3], row[4])
    #print output_string
    pg = round((count / number_of_rows)*100,2)
    sys.stdout.write("\n{0}%".format(pg))
    #sys.stdout.flush()
    target.write(output_string)
    count = count + 1

cur.close()
conn.close()
target.close()
            












