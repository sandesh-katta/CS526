
import pyshark

trace_input = pyshark.FileCapture("project2_part1.pcap", display_filter='udp and not dns and not browser and not mdns and not cups and not nbns and not auto_rp and not smb_netlogon')

ip_dict = {}

for packet in trace_input:
        ip_src = packet.ip.src
        ip_dst = packet.ip.dst
        ip_endpoints = (ip_src, ip_dst)
        
        if ip_endpoints in ip_dict:
            ttl_dict = ip_dict[ip_endpoints]
            ttl = int(packet.ip.ttl)
            if ttl not in ttl_dict:
                ttl_dict.add(ttl)
        else:
            ip_dict[ip_endpoints] = set()
            ip_dict[ip_endpoints].add(int(packet.ip.ttl))

for endpoint in ip_dict:
    if len(ip_dict[endpoint]) > 60:
        print (endpoint)