#!/usr/bin/python

import csv
import json
import sys
import os
import subprocess

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
fieldnames = ("tsuid",	"id_orig_h",	"id_orig_p",	"id_resp_h",	"id_resp_p",	"proto",	"trans_id",	"query",	"qclass",	"qclass_name",	"qtype",	"qtype_name",	"rcode",	"rcode_name",	"AA",	"TC",	"RD",	"RA","Z",	"answers",	"TTLs",	"rejected")
reader = csv.DictReader( csvfile, fieldnames)
count=1
for row in reader:
   out = json.dumps( row )
   upload = "'" + out + "'"
   #print(upload)
   #args = ("-H","Content-Type: application/json","-d",upload,"codexcom01.cloudapp.net:3000/insert")
   #print("===============\n")
   #print(args)
   #print("\n===================\n")
   #os.execvp("curl", args)   
   os.system("curl -H \"Content-Type: application/json\" -d " + upload + " codexcom01.cloudapp.net:3000/insert")
   #subprocess.call(["curl", "-H","Content-Type: application/json","-d",upload,"codexcom01.cloudapp.net:3000/insert"])
   
   curFile = outputF + str(count)
   #jsonfile = open(curFile,'w') 
   #jsonfile.write(out)
   #jsonfile.close()
   print("count= %s" % str(count))
   count=count+1   
   #if count > 100:
   #   break

csvfile.close()


