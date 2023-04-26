
from scapy.all import *
from scapy.layers import http
from collections import Counter
import sys


# Read the pcap file
pkts = rdpcap(sys.argv[1])

# Create a dictionary to keep track of flows
flows = {}
http_bytes = 0
hostnames = []

# Loop through each packet in the pcap file
for pkt in pkts:
    # Parse the captured packets to extract the hostname
    if pkt.haslayer('HTTPRequest'):
        hostname = pkt['HTTPRequest'].Host.decode()
        hostnames.append(hostname)
    # Check if the packet has HTTP layer
    if pkt.haslayer('HTTP'):

        http_bytes += len(pkt)
        # Get the source and destination IP addresses
        src = pkt[IP].src
        dst = pkt[IP].dst
        # Check if there is already a flow between the source and destination
        if (src, dst) in flows or (dst, src) in flows:
            if 'HTTP' in flows[(src, dst)]:
                flows[(src, dst)]['HTTP'] += 1
            elif 'HTTP' in flows[(dst, src)]:
                flows[(dst, src)]['HTTP'] += 1
        else:
            # If there isn't, create a new flow and set the flow count to 1           
            if pkt[TCP].sport == 80:
                flows[(src, dst)] = {'HTTP': 1}
                flows[(dst, src)] = {'HTTP': 0}
            else:
                flows[(dst, src)] = {'HTTP': 1}
                flows[(src, dst)] = {'HTTP': 0}         


# Print the number of HTTP flows
print("HTTP Traffic Flows: ",len([flow for flow in flows.values() if 'HTTP' in flow]) / 2)
print("HTTP Traffic Bytes: ", http_bytes)

hostname_counts = Counter(hostnames)
print("Top HTTP Hostname: ", hostname_counts.most_common(1)[0][0])

