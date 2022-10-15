import pyshark

input_trace = pyshark.FileCapture("project2_part1.pcap", display_filter='http and http.request.uri contains "../.."')

src_host = set()
for packet in input_trace:
	src_host.add(packet.ip.src)

print(sorted(src_host))