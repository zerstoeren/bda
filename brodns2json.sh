#!/bin/bash

#docker run -v ~/planx/bro:/ftp:rw -i -t broftp bash
#iptables -t nat -A  PREROUTING -i eth0 -p tcp --dport 42 -j DNAT --to 172.17.0.2:42

#transform the pcap to something bro can process
./airdecap-ng $1
#new file format is $1-dec.$1ext
coreName=`echo $1 | awk -F. '{print $1}'`
coreExt=`echo $1 | awk -F. '{print $2}'`
newName=`echo $coreName-dec.$coreExt`
echo $newName
#convert pcap using bro
/usr/local/bro/bin/bro -r $newName
#start with the DNS
#strip headers we can't use
tail -n +9 dns.log > $newName
#oh hey, its NOT a csv even though it says it is...fix it
sed -i 's/\t/,/g' $newName
#emit json
python dnsconverter.py $newName $2


