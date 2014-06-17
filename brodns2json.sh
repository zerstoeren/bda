#!/bin/bash

#docker run -v ~/planx/bro:/ftp:rw -i -t broftp bash
#iptables -t nat -A  PREROUTING -i eth0 -p tcp --dport 42 -j DNAT --to 172.17.0.2:42

#convert pcap using bro
/usr/local/bro/bin/bro -r $1
#start with the DNS
#strip headers we can't use
tail -n +9 dns.log > $2
#oh hey, its NOT a csv even though it says it is...fix it
sed -i 's/\t/,/g' $2
#emit json
python dnsconverter.py $2 $2


