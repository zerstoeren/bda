from scapy.all import *
import sys
import os.path

if (os.path.isfile(sys.argv[1])):
   print "Parsing..." 
else:
    print "File not found, exiting..."
    sys.exit()

#pcap = rdpcap("capfiles/airportSniffHwGVg3.cap")
pcap = rdpcap(sys.argv[1])
f = open('json', 'w')

for i in pcap:
    f.write("netflow {\n")
    try:
        f.write("\"smac\":\""+i[Dot11].addr1+"\"")
        f.write("\n\"dmac\":\""+i[Dot11].addr2+"\"")
    except:
        pass
    try:
        f.write("\n\"sip\":\""+i[IP].src+"\"")
        f.write("\n\"dip\":\""+i[IP].dst+"\"")
    except:
        pass
    try:
        f.write("\n\"sport\":\""+str(i.sport)+"\"")
        f.write("\n\"dport\":\""+str(i.dport)+"\"")
    except AttributeError:
        pass
    try:
        proto = i.getlayer(6).name
    except:
        proto = ""
    f.write("\n\"protocol\":\""+str(proto)+"\"")
#    try:
#        f.write("\nuser:TBD")
#    except:
#        pass
    try:
        f.write("\n\"time\":\""+str(int(i.time))+"\"")
    except:
        pass
    try:
        f.write("\nbytes:\""+i[IP].len+"\"")
    except:
        pass
    f.write("\n}\n")
f.close()
