from scapy.all import *

pcap = rdpcap("capfiles/airportSniffHwGVg3.cap")
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
        f.write("\n\"sport\":\""+i[IP].sport+"\"")
        f.write("\n\"dport\":\""+i[IP].dport+"\"")
    except:
        pass
    try:
        f.write("\nprotocol:TBD")
    except:
        pass
    try:
        f.write("\nuser:TBD")
    except:
        pass
    try:
        f.write("\n\"time\":\""+str(i.time)+"\"")
    except:
        pass
    try:
        f.write("\nbytes:\""+i[IP].len+"\"")
    except:
        pass
    f.write("\n}\n")
f.close()
