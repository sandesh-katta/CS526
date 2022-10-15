import pyshark


input_trace = pyshark.FileCapture("project2_part1.pcap", display_filter='http and  http.request.uri contains "<script>" and http.request.uri contains "</script>"')

src_ip_set = set()


for packet in input_trace:
	src_ip_set.add((packet.ip.src, packet.ip.dst))


print("Host attempting xss attack and its target:")
print(src_ip_set)