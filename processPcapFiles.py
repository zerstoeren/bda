import os
import glob
files = [ f for f in glob.glob("tbd/*.pcap") ]
for i in files:
    print "Processing "+i
    os.system("python "+os.path.abspath("jsonParser.py") +" "+i)
    print i
    os.rename(i, "done/"+i.split("/")[-1])
