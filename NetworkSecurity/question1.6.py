import pyshark

input_trace = pyshark.FileCapture("project2_part1.pcap", display_filter='dns && dns.flags.response == 0')
host_ips = {}
for packets in input_trace:
	src_ip = packets.ip.src
	src_port = packets.udp.srcport
	if src_ip not in host_ips:
		host_ips[src_ip] = set()
	host_ips[src_ip].add(src_port)


suspicious_hosts = set()
for key in host_ips:
	if (len(host_ips[key]) == 1):
		suspicious_hosts.add(key)
		
print("Hosts that use a static UDP port number for DNS queries:")
print(sorted(suspicious_hosts))