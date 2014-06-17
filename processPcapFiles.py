import os
files = [ f for f in os.listdir("tbd/") if os.path.isfile(os.path.join("tbd/",f)) ]
for i in files:
    print "Processing "+i
    os.system("python "+os.path.abspath("jsonParser.py")+" tbd/"+i)
    os.rename("tbd/"+i, "done/"+i)
