tshark -i en0 -T fields -e ip.src -e ip.dst -e dns.qry.name -Y "dns.flags.response || dns.qry.name || tcp.port==80 || tcp.port==443 || tcp.port==53 || udp.port==53"
