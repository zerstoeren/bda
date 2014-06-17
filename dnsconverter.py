#!/usr/bin/python

import csv
import json
import sys

#numargs = len(sys.argv)
#if numargs != 3 
cmdargs = str(sys.argv)
print("usage: %s <inputfile> <outputfile>" % str(sys.argv[0]))
#print ("numargs: %d " % numargs)
#print ("Args list: %s " % cmdargs) 
#print ("Script name: %s" % str(sys.argv[0]))
print ("Converting: %s" % str(sys.argv[1]))
print ("Saving as: %s" % str(sys.argv[2]))
inputF = sys.argv[1]
outputF = sys.argv[2]
csvfile = open(inputF,'r') #'file.csv', 'r')
fieldnames = ("tsuid",	"id.orig_h",	"id.orig_p",	"id.resp_h",	"id.resp_p",	"proto",	"trans_id",	"query",	"qclass",	"qclass_name",	"qtype",	"qtype_name",	"rcode",	"rcode_name",	"AA",	"TC",	"RD",	"RA","Z",	"answers",	"TTLs",	"rejected")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
csvfile.close()
jsonfile = open(outputF,'w') #'file.json', 'w')
jsonfile.write(out)
jsonfile.close()

